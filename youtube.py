import urllib.request
from bs4 import BeautifulSoup

def search_tube(textToSearch):
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    bruhv = []
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        bruhv.append('https://www.youtube.com' + vid['href'] )
    return bruhv[0]