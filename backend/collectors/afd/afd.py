import feedparser as fd
import time
import json as js
import re

def getAfDfeed(dateofLastEntry):

    feed = fd.parse("https://www.afdbundestag.de/feed/")
    entry = feed.entries[0]
    entry_published = time.mktime(entry['published_parsed'])
    if entry_published > dateofLastEntry:
        print("published" + entry_published)

        text = js.dumps(entry.content[0].value, indent="\t", ensure_ascii=False).encode('utf-8').decode()
        text = re.sub(r'<.*?>', '', text).replace('\\n', ' ')


        content = {
            "party": "afd",
            "title": entry['title'],
            "published": entry_published,
            "summary": entry['summary'],
            "text": text


        }

    data_File = open("output.txt", "w")
    data_File.write(str(text))
    data_File.close()

    return content


