from pyquery import PyQuery as pq




link = "https://www.spdfraktion.de/presse/pressemitteilungen/wir-verneigen-uns-opfern-nationalsozialismus"

raw_data = pq(url=link)
raw_data = raw_data('body')
raw_data = raw_data('.content')
#raw_data = raw_data('p > strong')


data_File = open("article.txt", "w")
data_File.write(str(raw_data))
data_File.close()