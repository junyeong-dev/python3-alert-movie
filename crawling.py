import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=02&theatercode=0012&date=20210729'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
# 특정 영화만 가져와보기
# print(soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong'))
title_list = soup.select('div.info-movie')
for i in title_list:
    print(i.select_one('a > strong').text.strip())