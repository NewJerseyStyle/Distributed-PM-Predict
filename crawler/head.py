import time
import random
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
from tinydb import TinyDB, Query
from tqdm import tqdm
import ray

from .model import nltk_sent
from .model import deep_sent
from .model import Engine

if __name__ == '__main__':
    ray.init('auto')


async def download_all_mps():
    print('[download_all_mps] Start')
    with TinyDB('db.json') as db:
        mp_db = db.table('mps')
        if len(mp_db):
            print('[download_all_mps] Skip')
            return
        browser = await launch(headless=True)
        page = await browser.newPage()
        await stealth(page)
        print('[download_all_mps] Page loading')
        await page.goto('https://members.parliament.uk/members/commons')
        continue_flag = True
        mp_link_list = []
        while continue_flag:
            await page.waitForSelector('.card-member')
            mp_list = await page.querySelectorAll('.card-member')
            for element in mp_list:
                href = await page.evaluate('(element) => element.href', element)
                mp_link_list.append(href)
            print(f'[download_all_mps] Added {len(mp_list)} MP record')

            await asyncio.sleep(random.randint(1, 6))

            try:
                mp_name_selector = '#main-content > div > article > div > div > div:nth-child(3) > div > div.col-md-7 > div > ul > li.next > a'
                await page.waitForSelector(mp_name_selector)
                await page.querySelectorEval(mp_name_selector, '(element) => element.click()')
            except:
                print('[download_all_mps] Cannot find next page, end loop')
                continue_flag = False
        await browser.close()

        print(f'[download_all_mps] Crawling {len(mp_link_list)} MP pages')
        # proxies = get_proxy_list()
        browser = await launch(headless=True)
        page = await browser.newPage()
        await stealth(page)
        for url in tqdm(mp_link_list):
            # ip, port = random.choice(proxies).split(':')
            # browser = await launch({'args': [f'--proxy-server={ip}:{port}'], 'headless': True })
            await asyncio.sleep(random.randint(2, 7))
            await page.goto(url)
            mp_name_selector = '#main-content > div.hero-banner.hero-banner-brand > div > div > div.col-md-8.col-no-spacing > h1'
            await page.waitForSelector(mp_name_selector)
            name = await page.querySelectorEval(mp_name_selector, '(element) => element.textContent')
            await page.waitForSelector('.card-contact-info')
            contact = await page.querySelector('.card-contact-info')
            contact_url = await page.evaluate('(element) => element.href', contact)
            mp_data = {'name': name, 'twitter': None}
            if contact_url is not None and 'twitter' in contact_url:
                mp_data['twitter'] = contact_url
            mp_db.insert(mp_data)
        await browser.close()
        print('[download_all_mps] End...')


async def download_all_candidates():
    print('[download_all_candidates] Start')
    with TinyDB('db.json') as db:
        pc_db = db.table('pcs')
        if len(pc_db):
            print('[download_all_candidates] Skip')
            return
        browser = await launch(headless=True)
        page = await browser.newPage()
        await stealth(page)
        print('[download_all_candidates] Page loading')
        await page.goto('https://www.oddschecker.com/politics/british-politics/next-prime-minister')
        await page.waitForSelector('.selTxt')
        pc_list = await page.querySelectorAll('.selTxt')
        for element in pc_list:
            name = await page.evaluate('(element) => element.innerText', element)
            pc_db.insert({'name': name})
        print(f'[download_all_candidates] Added {len(pc_list)} PM candidates')
        await asyncio.sleep(1)
        print('[download_all_candidates] End...')
        await browser.close()


def get_all_powers():
    power_list = ['John Gore',
                 'Peter Hargreaves',
                 'Lubov Chernukhin',
                 'Ann Rosemary Said',
                 'Lakshmi',
                 'Usha Mittal',
                 'Aquind.Ltd',
                 'Unite',
                 'Len McCluskey',
                 'Ecotricity',
                 'Harold Immanuel',
                 'Christopher Harborne',
                 'Jeremy Hosking',
                 'AML Global',
                 'Sherriff Group',
                 'Noel Hayden',
                 'Davide Serra',
                 'Julian Dunkerton']
    return power_list


@ray.remote
class AsyncActor:
    async def ask(self, pname, pc_name, engine):
        browser = await launch(headless=True,
                               args=["--disable-gpu",
                                     "--no-sandbox",
                                     "--disable-extensions"],
                                handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False)
        at_db_list = []
        page = await browser.newPage()
        await stealth(page)
        # google pname + pc.name
        await page.goto('https://www.google.com/')
        await page.waitForSelector('input')
        await page.type('input', f'{pname} and {pc_name}')
        await page.keyboard.press('Enter')
        # grap all result of first 2 page
        for i in range(2):
            try:
                await page.waitForSelector('.g')
                article_list = await page.querySelectorAll('.g')
                for element in article_list:
                    article = await page.evaluate('(element) => element.classList.length > 1 ? "" : element.innerText', element)
                    at_db_list.append(article)
                element = await page.querySelector('a#pnnext')
                if element is None:
                    print(f'[ask_google] {pname} + {pc_name} no next page, break')
                    break
                await page.evaluate('(element) => element.click()', element)
            except Exception as e:
                print(f'[ask_google] Google page {i} with {pc_name} got {repr(e)}')
            finally:
                await asyncio.sleep(3)
        await page.close()
        await asyncio.sleep(random.randint(14, 30))
        data = []
        for article in at_db_list:
            if pc_name in article:
                data.append(article)
        if engine == Engine.NLTK:
            supportiveness, _, _ = nltk_sent.sentiment_analysis(data)
        elif engine == Engine.HUGGINGFACE:
            supportiveness, _, _ = deep_sent.sentiment_analysis(data)
        await browser.close()
        return supportiveness, len(data), len(at_db_list)


def ask_google_tasks(pname, engine=Engine.NLTK):
    assert isinstance(engine, Engine)

    print('[ask_google] Start')
    with TinyDB('db.json') as db:
        pc_db = db.table('pcs')
        at_db = db.table('articles')
        User = Query()
        pairs = []
        tasks = []
        actor = AsyncActor.remote()
        for pc in pc_db:
            pc_name = pc['name']
            task = actor.ask_google.remote(pname, pc_name, engine)
            tasks.append(task)
            pairs.append((pname, pc_name))
        return_vals = ray.get(tasks)
        activeness_denominator = max([x for _, _, x in return_vals])
        ds_db = db.table('qips')
        for (supportiveness, activeness_numerator, _), (pname, pc_name) in zip(return_vals, pairs):
            ds = ds_db.search(User.q == pc_name)
            if len(ds) == 0:
                ds = {'q': pc_name, 'i': [], 'p': [], 's': []}
            else:
                ds = ds[0]
            activeness = 100 * activeness_numerator / activeness_denominator
            powerfulness = 50
            if pname in get_all_powers():
                powerfulness = 70
            ds_db.upsert(ds, User.q == pc_name)


def do_search(engine=Engine.NLTK):
    print('[do_search] Start')
    db = TinyDB('db.json')
    mp_db = db.table('mps')
    for mp in tqdm(mp_db, desc='Googleing supporting MPs'):
        ask_google_tasks(mp['name'], engine=Engine.NLTK)
    for name in tqdm(get_all_powers(), desc='Googleing supporting powers'):
        ask_google_tasks(name, engine=Engine.NLTK)
    print('[do_search] End...')


def main(engine=Engine.NLTK):
    # crawl name list
    asyncio.get_event_loop().run_until_complete(download_all_mps())
    asyncio.get_event_loop().run_until_complete(download_all_candidates())
    # make sure Boris Johnson is on the list
    with TinyDB('db.json') as db:
        pc_db = db.table('pcs')
        name = 'Boris Johnson'
        User = Query()
        if not pc_db.contains(User.name == name):
            pc_db.insert({'name': name})
    # crawl + analysis data
    do_search(engine=Engine.NLTK)
