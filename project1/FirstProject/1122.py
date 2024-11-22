import csv
import requests
from bs4 import BeautifulSoup
import os

# 드라마 정보가 있는 페이지 접근 및 시리즈 수 찾기
url="https://www.imdb.com/title/tt1796960/episodes/?season=1"
#hdr = {'User-Agent':'Mozilla/5.0'}
hdr={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
res=requests.get(url, headers=hdr)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")
print(soup)

season =soup.find_all("a", attrs={"data-testid":"tab-season-entry"})
nums_season = len(season)
text_season=[]
for s in season:
    print(s)
    text_season.append(s.get_text())

print(f"총 시즌 수:{nums_season}")
print(f"시즌 타이틀:{text_season}")

# 각 시리즈 페이지에서 원하는 데이터 수집과 저장
filename = "홈랜드 시즌 정보.csv"