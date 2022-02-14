from requests_html import HTMLSession
from bs4 import BeautifulSoup


s = HTMLSession()

url = 'http://cse.iubat.edu/faculty/'

def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

print(getdata(url))
#prints out the entire DOM element of the webpage