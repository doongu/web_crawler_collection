# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib3
import json

urllib3.disable_warnings()
for page in range(1, 2):
    select_url = f"https://www.coupang.com/np/search?q=핸드워시&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=salePriceAsc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={page}&rocketAll=false&searchIndexingToken=&backgroundColor="
    data = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    request = requests.get(select_url, headers = data)
    soup = BeautifulSoup(request.text, "html.parser")

    #이렇게 찾으면 깔끔하게 다 찾아줌
    select_rocket = soup.find_all("li", {"class":"search-product"})

    find_url_temp = soup.find_all("a", {"class": "search-product-link"})
    # 배송 처리
    # print(select_rocket[11].find("span", {"class" : "badge rocket"}))
    find_url = []
    for i in range(len(select_rocket )):
        try:
            print(i)
            check_rocket = None
            check_global = None
            check_rocket =  select_rocket[i].find("span", {"class" : "badge rocket"})
            print(check_rocket) #현재 페이지의 리스트에서 로켓부분을 가져온다 없으면 NONE
            check_global = select_rocket[i].find("span", {"class" : "badge global"})
            parse_url = select_rocket[i].find("a", {"class": "search-product-link"})["href"]
            print(select_rocket[i].find("a", {"class": "search-product-link"})["href"])
            print(select_rocket[i].find("strong", {"class": "price-value"}).text) #여기서의 가격은 의미 x
            if check_rocket == None and check_global == None:

                find_url.append("https://www.coupang.com" + parse_url)
            else:
                find_url.append("None")

            #.find("span", {"class" : "badge rocket"})
        except:
            pass

for url in find_url:
    if url != "None":
        select_url =  url
        data = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
        request = requests.get(select_url, headers=data)
        soup = BeautifulSoup(request.text, "html.parser")

        select_title = soup.find("h2", {"class":"prod-buy-header__title"})
        select_price = soup.find("span", {"class": "total-price"})
        find_delivery = soup.find("div", {"class": "prod-shipping-fee-message"})
        print(len(select_title), len(select_price), len(find_delivery))



        temp = find_delivery.text.replace("\n", "")
        if temp == "무료배송":
            temp_delivery = "무료배송"
            print("배송비", temp_delivery)
        else:

            temp_delivery = ""
            for i in range(len(temp) - 1, -1, -1):
                temp_delivery += temp[i]
                if temp[i] == " ":
                    break
            temp_delivery = temp_delivery[::-1]
            # temp_delivery.replace(",", "")[:-1]
            print("배송비", temp_delivery.replace(",", ""))

        print(select_title.text.replace("\n", "") + " / " + select_price.text.replace("\n",  "") + " / " + temp_delivery.replace(",", "").replace("원", ""))
        print(url)
        print("\n\n")
        #배송비 처리

    # for j in range(len(soup.find_all("div", {"class": "name"}))):
    #     find_name = soup.find_all("div", {"class": "name"})
    #     if "화이트" not in find_name[j].text:
    #         print("화이트 없는 제품")
    #     else:
    #         print(find_name[j].text)