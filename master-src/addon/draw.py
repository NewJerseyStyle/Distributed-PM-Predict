from html2image import Html2Image
from pyppeteer import launch
from tinydb import TinyDB
import asyncio

from .css import get_css
from .html import get_html

async def draw():
  hti = Html2Image()
  db = TinyDB('db.json')
  rs_db = db.table('ranks')
  for ds in rs_db:
    css = get_css()
    html = get_html(data_melchior=ds['a'],
                    data_balthasar=ds['b'],
                    data_casper=(ds['a'] + ds['b']) / 2)
    hti.screenshot(html_str=html, css_str=css, save_as=f'{ds["name"]}.png')


def main():
  asyncio.get_event_loop().run_until_complete(draw())
