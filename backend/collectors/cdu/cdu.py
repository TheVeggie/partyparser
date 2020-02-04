import feedparser as fd
import time
import json as js
from pyquery import PyQuery as pq



dateOfLastEntry = 0

feed = fd.parse("https://www.cducsu.de/rss_cdu_artikel.xml")
entry = feed.entries[0]
entry_published = time.mktime(entry['published_parsed'])

if entry_published > dateOfLastEntry:
    print(entry_published)

    article_link = js.dumps(entry.links[0]['href'])
    print(article_link)
    
    text = extractCDUContent(article_link)


    content = {

             "title": entry['title'],
             "published": entry_published,
             "summary": entry['summary'],
             "text": text

    }

data_File = open("feed.txt", "w")
data_File.write(str(content))
data_File.close()