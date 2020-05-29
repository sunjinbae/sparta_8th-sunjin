# 웹 스크래밍 = 웹 크롤링
# 웹 사이트의 정보를 긁어오는 기술 ex) 지그재그 , 뱅크샐러드, 토스 
# requests => API 또는 HTML 페이지 요청
# bs4 (beautuful soup 4) => 받아온 html 파일을 읽기 쉽게 파싱(parsing)
import requests
from bs4 import BeautifulSoup

#크롤링 : 데이터를 훔치는 작업
#크롤링 방어 : 창 vs 방패
# 요청을 날리는걸 웹 브라우저가 날리는것처럼 속이는 작업 
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

#print(data)

soup = BeautifulSoup(data.text, 'html.parser') #가지고 온 data.txt를 html 파일로 파싱한다는 뜻
#print(soup)

movies = soup.select('#old_content > table > tbody > tr') 
#print(movies)

for movie in movies:
    # a_tag = movie.select_one('td.title > div > a')

    # if a_tag is not None:
    #     print(a_tag.text)
    title_tag = movie.select_one('td.title > div > a')
    rate_tag = movie.select_one('td.point')
    rank_tag = movie.select_one('td.ac > img')

    if title_tag is not None and rate_tag is not None and rank_tag is not None:
        title = title_tag.text
        rate = rate_tag.text
        rank = rank_tag["alt"]
        print(rank, rate, title)
#select : 결과값이 항상 리스트
#select_one : 결과값이 항상 html 태그