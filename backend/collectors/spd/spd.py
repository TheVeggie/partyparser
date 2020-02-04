import feedparser as fd
import time
import json as js
import requests as rq #
from pyquery import PyQuery as pq
from getArticleContent import extractSPDContent


def getFeed(dateOfLastEntry):



    


    feed = fd.parse("https://www.spdfraktion.de/presse/pressemitteilungen/feed")
    entry = feed.entries[0]
    entry_published = time.mktime(entry['published_parsed'])

    article_link = js.dumps(entry.links[0]['href'])
    print(article_link)
    text = extractSPDContent(article_link)

    if entry_published > dateOfLastEntry:

        content = {

             "title": entry['title'],
             "published": entry_published,
             "summary": 
             "text": text



              }

        print(content)

        data_File = open("spd_data", "w")
        data_File.write(str(entry))
        data_File.close()

        #return entry_published, content






