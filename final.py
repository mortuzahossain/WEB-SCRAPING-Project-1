from bs4 import BeautifulSoup
import urllib2

url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250_6'

openurl = urllib2.urlopen(url)
html = openurl.read()
openurl.close()

soup = BeautifulSoup(html,'lxml')
heading = soup.find('h1',class_ = 'header').text + '\n'
table = soup.find('tbody',class_ = 'lister-list')
movie_names = table.find_all('td',class_ = 'titleColumn')
all_rating = table.find_all('td',class_ = 'imdbRating')

f = open('final.txt','w+')
f.write(heading)

for x in xrange(len(movie_names)):
	movie_name = movie_names[x].text.replace('      ','').replace('\n','').encode('utf-8')
	ratings = all_rating[x].text.replace('\n','').encode('utf-8')
	write_in_file = movie_name + ' : ' + ratings + '\n'
	f.write(write_in_file)

f.close()
