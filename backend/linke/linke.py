import feedparser as fd
import re
import time
import json as js


def getFeed(dateOfLastEntry):


    feed = fd.parse("https://www.linksfraktion.de/presse/pressemitteilungen/feed.rss")
    
    
    entry = feed.entries[0]
    entry_published = time.mktime(entry['published_parsed'])
    if entry_published > dateOfLastEntry:

        print(entry_published)

        content = {

            "title": entry['title'],
            "published": entry_published,
            "summary": entry['summary'], # just for testing
            "text": js.dumps(feed.entries[0].content[0].value, indent="\t")
        }

        data_File = open("linke_done.txt", "w")
        data_File.write(str(entry['content']))
        data_File.close()

    return entry_published, content


getFeed(0)
