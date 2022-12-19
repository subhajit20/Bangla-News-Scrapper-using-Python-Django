import requests
from bs4 import BeautifulSoup

URL = "https://bengali.abplive.com/news"
daily_news = []


def Scrap_Bangla_News():
    getnews = requests.get(URL)
    content = BeautifulSoup(getnews.content,features="html.parser")

    data = content.findAll('div',attrs={'class':'other_news'})
    imgs = content.findAll('div',attrs={'class':'img4x3'})

    imgLinks = imgs[4:50]
    heading = data[:19]
    i = 0
    while i <= len(imgLinks)-1 and i <= len(heading)-1 and i <= len(heading)-1:

        daily_news.append(
            {
                'link':heading[i].a['href'],
                'heading':heading[i].a.div.text,
                'imglink':imgLinks[i].img['data-src']
            }
        )

        i = i + 1

    return daily_news