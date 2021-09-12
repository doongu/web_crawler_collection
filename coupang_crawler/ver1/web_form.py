# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib3
import json

urllib3.disable_warnings()
for page in range(1, 2):
    select_url = f"https://www.coupang.com/np/search?q=핸드워시&190*2&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={page}&rocketAll=false&searchIndexingToken=&backgroundColor="
    data = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    request = requests.get(select_url, headers = data)
    soup = BeautifulSoup(request.text, "html.parser")

    #이렇게 찾으면 깔끔하게 다 찾아줌
    select_rocket = soup.find_all("li", {"class":"search-product"})
    # 배송 처리
    for i in range(len(select_rocket )):
        try:
            print(i)
            print(select_rocket[i])
        except:
            break
    #
    # for j in range(len(soup.find_all("div", {"class": "name"}))):
    #     find_name = soup.find_all("div", {"class": "name"})
    #     if "화이트" not in find_name[j].text:
    #         print("화이트 없는 제품")
    #     else:
    #         print(find_name[j].text)