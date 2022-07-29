import time
import random
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
from tinydb import TinyDB, Query
from tqdm import tqdm

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


async def ask_google(pname):
    print('[ask_google] Start')
    with TinyDB('db.json') as db:
        pc_db = db.table('pcs')
        at_db = db.table('articles')
        User = Query()
        browser = await launch(headless=True,
                               args=["--disable-gpu",
                                     "--no-sandbox",
                                     "--disable-extensions",
                                     "--disable-dev-shm-usage",
                                     "--no-first-run",
                                     "--single-process"])
        for pc in tqdm(pc_db):
            pc_name = pc['name']
#             tqdm.write(f'[ask_google] Googling with {pc_name}')
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
                        tqdm.write(f'[ask_google] {pname} + {pc_name} no next page, break')
                        break
                    await page.evaluate('(element) => element.click()', element)
                except Exception as e:
                    tqdm.write(f'[ask_google] Google page {i} with {pc_name} got {repr(e)}')
                finally:
                    await asyncio.sleep(3)
            await page.close()
            await asyncio.sleep(random.randint(30, 40))
        # store data to db
        at_db.upsert({'name': pname, 'pc': pc_name, 'texts': at_db_list}, (User.name == pname) & (User.pc == pc_name))
        await browser.close()


def do_search():
    print('[do_search] Start')
    db = TinyDB('db.json')
    mp_db = db.table('mps')
    for mp in tqdm(mp_db, desc='Googleing supporting MPs'):
        asyncio.get_event_loop().run_until_complete(ask_google(mp['name']))
    for name in tqdm(get_all_powers(), desc='Googleing supporting powers'):
        asyncio.get_event_loop().run_until_complete(ask_google(name))
    print('[do_search] End...')


def main():
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
    # crawl data
    do_search()
