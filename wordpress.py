from __future__ import print_function
import json
import feedparser
# from lxml import html
from bs4 import BeautifulSoup
from newspaper import Article
import nltk

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names

def fetch_RSS(rss_url):
  d = feedparser.parse(rss_url)
  for entry in d.get('entries'):
    # print(entry.title)
    # print(entry.author)
    # print(entry.updated)
    a = Article(entry.link)
    a.download()
    a.parse()
    # print(a.text)
    # print()

    sentences = nltk.sent_tokenize(a.text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)

    # entity names
    entity_names = []
    for tree in chunked_sentences:
        entity_names.extend(extract_entity_names(tree))
    print(entity_names)


url = 'http://blog.enigma.io/feed/'
# url = 'http://newsroom.fb.com/feed/'
fetch_RSS(url)





