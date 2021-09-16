import requests
from bs4 import BeautifulSoup
import telegram
from token import api_key
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token=api_key)
# url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=02&theatercode=0012&date=20210729'
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=02&theatercode=0012&date=20210806'

def scrap_movie():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    # 특정 영화 제목만 가져와보기
    # print(soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong'))

    # 모든 영화 제목 가져오기
    # title_list = soup.select('div.info-movie')
    # for i in title_list:
    #     print(i.select_one('a > strong').text.strip())

    imax = soup.select('span.imax')
    if(imax):
        for i in imax:
            imax_title = i.find_parent('div', class_='col-times').select_one('div.info-movie > a > strong').text.strip()
            bot.send_message(chat_id=1955432261, text=imax_title + ' IMAX 예매가 열렸습니다.')
        # 메시지 그만 보내기
        sched.pause()


# 스케줄러
sched = BlockingScheduler()
# 30초마다 메시지 보내기
sched.add_job(scrap_movie(), 'interval', seconds=30)