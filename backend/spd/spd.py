import feedparser as fd
import re
import time


def getFeed(dateOfLastEntry):


    feed = fd.parse("https://www.spdfraktion.de/presse/pressemitteilungen/feed")
    entry = feed.entries

    data_File = open("spd_done.txt", "w")
    data_File.write(str(entry))
    data_File.close()

    #return entry_published, content


getFeed(0)




