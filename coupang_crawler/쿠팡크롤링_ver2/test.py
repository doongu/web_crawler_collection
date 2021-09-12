# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib3
import json
import copy

import time

# 인자로 input 리스트를 받는다
def select_data(input, name_check):
    return_list = []

    # input_value[0] => 첫번째 열
    # input_value[1] => 두번째 열
    index_check_num = -1
    for input_value in input:

        index_check_num += 1
        min_value = 9999999999
        flag = 0

        for index in range(1,2):
            # 원하는 페이지 수
            for page in range(1, 4):

                # 크롤러 작동
                find_name = ""
                find_price = ""

                select_url = f"https://www.coupang.com/np/search?q={input_value[index]}&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=salePriceAsc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={page}&rocketAll=false&searchIndexingToken=&backgroundColor="
                data = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

                request = requests.get(select_url, headers=data)
                soup = BeautifulSoup(request.text, "html.parser")
                find_name = soup.find_all("div", {"class": "name"})
                print("확인할 이름입니다. :", find_name)
                print(len(find_name))
                find_price = soup.find_all("strong", {"class": "price-value"})
                print("확인할 가격입니다. :" ,find_price)
                print(len(find_price))
                find_url_temp = soup.find_all("a", {"class": "search-product-link"})
                find_url = []
                # /vp/products/1383883541?itemId=2418536739&vendorItemId=70873528237&sourceType=srp_product_ads
                # url 다 찾음
                for url_print in find_url_temp:
                    parse_url = url_print["href"]
                    find_url.append("https://www.coupang.com/" + parse_url)


                #현재 제품에서 최솟값 찾음
                for i in range(len(find_name)):
                    if index == 1:

                        #190*2이면 190과 20이 들어있는지 확인해본다.
                        for j in range(len(name_check[index_check_num])):
                            print("=================================================")
                            print()
                            print(name_check[index_check_num][j] + "으로 비교")
                            print("쿠팡에 올라와있는  : " + find_name[i].text + " 입니다.")
                            if str(name_check[index_check_num][j]) not in str(find_name[i].text):
                                print("존재하지 않습니다 . 존재하지 않습니다 . 존재하지 않습니다 . 존재하지 않습니다 . 존재하지 않습니다 . 존재하지 않습니다 . ")
                                break

                    print(find_name[i].text)
                    print(find_price[i].text)

                    compare_find_price = find_price[i].text.replace(",", "")
                    if min_value > int(compare_find_price) and int(compare_find_price) > input_value[2] - 3000:
                        min_value = int(compare_find_price)
                        flag = i
                        temp_find_price = find_price[:]
                        temp_find_url = find_url[:]

        # 가격 젤 낮은 것 입력
        return_list.append([temp_find_price[flag].text, temp_find_url[flag]])

    return return_list
#
# print(select_data(["선풍기", "날개 없는 선풍기"]))