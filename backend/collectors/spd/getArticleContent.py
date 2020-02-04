from pyquery import PyQuery as pq


def extractSPDContent(link):


    raw_data = pq(filename='source.html')
    raw_data = raw_data('body')
    raw_data = raw_data('.content')
    raw_data = raw_data('section > div')
    raw_data = raw_data('.article-body')
    raw_data = raw_data('.maintext')
    raw_data = raw_data('#maintext')
    #raw_data = raw_data('text-intro')
    #raw_data = raw_data('p > strong')


    data_File = open("article.html", "w")
    data_File.write(str(raw_data))
    data_File.close()

    return raw_data


def extractSPDContent("https://www.spdfraktion.de/presse/pressemitteilungen/wir-verneigen-uns-opfern-nationalsozialismus")
