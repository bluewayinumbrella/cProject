#-*- coding: utf-8 -*-
#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

def extractInfo(addr):
    req = requests.get(addr)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    downloads = soup.select(
    'div > div.det-ins-container.J_Mod > div.det-ins-data > div.det-insnum-line > div.det-ins-num'
    )
    stars = soup.select(
    'div > div.det-ins-container.J_Mod > div.det-ins-data > div.det-star-box > div.com-blue-star-num'
    )
    links = soup.select(
    '#J_DetDataContainer > div > div.det-ins-container.J_Mod > div.det-ins-btn-box > a.det-ins-btn'
    )


    for down in downloads:
        print(down.text)
        print()

    for star in stars:
        print(star.text)
        print()

    for link in links:
        print(link['ex_url'])
    print()


req = requests.get('http://sj.qq.com/myapp/union.htm?orgame=1&page=1')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
appPages = soup.select(
'body > div > div > ul > li > section > div > div > a'
)

for page in appPages:
    addr = str(page['href'])
    if addr[:6] == "detail":
        detailLink = 'http://sj.qq.com/myapp/' + addr
        print(detailLink)
        extractInfo(detailLink)
