import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

#print(data)

soup = BeautifulSoup(data.text, 'html.parser')
#print(soup)

musics = soup.select('div.newest-list > div> table > tbody > tr> td')
#print(musics)

for music in musics:
    rank_a = music.select('td.number')
    title_a = music.select_one('td.info > a.title.ellipsis')
    singer_a = music.select_one('td.info > a.artist.ellipsis')

    if rank_a is not None and title_a is not None and singer_a is not None:
        #rank =  rank_a.text
        title = title_a.text
        singer = singer_a.text
        print(rank_a,title,singer)

        #RANK 값을 부르지못함 , RANK_A가 가지고있는 TEXT를 불러야함..