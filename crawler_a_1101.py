from BeautifulSoup import BeautifulSoup
import urllib2

# example url 
url = 'http://www.ema2u.com/'
# grab url with BeautifulSoup
graburl = urllib2.urlopen(url).read()
soup = BeautifulSoup(graburl)

# grab all link
alllinks = soup.findAll('a')

# print Data 
for showlink in alllinks:
    print(showlink["href"])