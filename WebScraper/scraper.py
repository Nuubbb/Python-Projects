import requests
from bs4 import BeautifulSoup
import random

maxLimit=5
def Scraper(url,limit=0):
    if limit>=maxLimit:
        return
        
    headers = {
    "User-Agent": "LearningBot/1.0 (contact: youremail@example.com)"
    }
    response=requests.get(url,headers=headers)

    soup=BeautifulSoup(response.text,"html.parser")
    title=soup.find(id="firstHeading")
    #print(title.string +"\n")
    print(title.get_text(strip=True)+"\n")

    allLinks=soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape=None

    for link in allLinks:
        if link['href'].find("/wiki/")==-1:
            continue

        linkToScrape=link
        break

    Scraper("https://en.wikipedia.org" + linkToScrape['href'],limit+1)

Scraper("https://en.wikipedia.org/wiki/Web_scraping")