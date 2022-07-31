import os
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
from tinydb import TinyDB, Query


async def tw_poster(url, u, p, filename):
  browser = await launch(headless=True)
  page = await browser.newPage()
  await stealth(page)
  # chrome goto tw, login
  await page.goto(url)
  await waitForSelector('input[autocomplete="username"]')
  await page.type('input[autocomplete="username"]', u)
  element = await page.querySelectorAll('div[role="button"]')[2]
  await page.evaluate('(element) => element.click()', element)
  await waitForSelector('input[autocomplete="current-password"]')
  await page.type('input[autocomplete="current-password"]', p)
  element = await page.querySelectorAll('div[role="button"]')[2]
  await page.evaluate('(element) => element.click()', element)
  await asyncio.sleep(6)
  # post with image
  await page.goto('https://twitter.com/compose/tweet')
  await waitForSelector('div[role="textbox"]')
  await page.type('div[role="textbox"]',
    f'''#MAGI_SYS\n 
    Lets guess, most protential candidate of the next Prime Minister 
    of UK today seems to be...\n 
    {filename.split('.')[0]}''')
  basepath = os.getcwd()
  element = await page.querySelector('input[type="file"]')
  element.uploadFile(os.path.join(basepath, filename))
  element = await page.querySelector('div[data-testid="tweetButton"]')
  await page.evaluate('(element) => element.click()', element)
  await asyncio.sleep(6)
  # clean up
  await browser.close()

def main(filename):
  with TinyDB('db.json') as db:
    config = db.table('config')
    for site in config:
      if 'twitter' in site['url']:
        # read tinydb config twitter user&pass
        asyncio.get_event_loop().run_until_complete(tw_poster(site['url'], site['user'], site['pass'], filename))
