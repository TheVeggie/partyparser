import feedparser as fd
import time
import json as js
from pyquery import PyQuery as pq


def getArticle(link):

    data = pq(url=link)
    data = re.sub(r'<.*?>', '', data)

    data_File = open("spd_data", "w")
    data_File.write(str(data))
    data_File.close()


def getFeed(dateOfLastEntry):    


    feed = fd.parse("https://www.spdfraktion.de/presse/pressemitteilungen/feed")
    entry = feed.entries[0]
    entry_published = time.mktime(entry['published_parsed'])
    print
    if entry_published > dateOfLastEntry:

        article_link = js.dumps(entry.links[0]['href'])
        print(article_link)
        #text = extractSPDContent(article_link)
        #text = getArticle(article_link)


        content = {
             "party": "afd",
             "title": entry['title'],
             "published": entry_published,
             "summary": entry['summary']
             #"text": text

              }

        print(content)

        data_File = open("spd_data", "w")
        data_File.write(str(entry))
        data_File.close()

        return entry_published, content

getFeed(0)





