from __future__ import print_function
import json
import feedparser
# from lxml import html
from bs4 import BeautifulSoup
from newspaper import Article

def fetch_RSS(rss_url):
  d = feedparser.parse(rss_url)
  for entry in d.get('entries'):
    print(entry.title)
    print(entry.author)
    print(entry.updated)
    a = Article(entry.link)
    a.download()
    a.parse()
    print(a.text)
    print()


url = 'http://blog.enigma.io/feed/'
fetch_RSS(url)