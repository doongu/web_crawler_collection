# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

#첫번쨰 제품부터 꼭 들어가야할 키워드를 적어준다
coffee_manual_keyword= [["프렌치카페", "카페믹스"], ["네스카페", "수프리모", "골드", "마일드"], ["맥심", " 모카", "골드", "마일드"], ["맥심", "화이트", "골드"], ["맥심", "카누", "미니"], ["카누", "바닐라", "라떼"], ["커피빈", " 캡틴", "아메리카노 미니", "미니"], ["인터내셔널", "로스트", "커피스틱"], ["커클랜드", "그라운드"], ["커클랜드", " 에티오피아", "원두커피"], ["커클랜드", "에스프레소"], ["커클랜드", "하우스", "블렌드"], ["테라로사", "올데이", "블렌드"], ["룰리", "스페셜", "블랙원두커피"], ["커클랜드", "원두"], ["폴바셋", "시그니처", "블렌드"], ["커피명가", "올굿", " 블렌드"], ["스타벅스", "카페", "베로나"], ["스타벅스", "브렉퍼스트", "블렌드"], ["스타벅스", "by" ], ["스타벅스", "네스카페", "돌체", "캡슐"], ["best", "moment", "돌체", "호환", "캡슐"], ["네스카페", "돌체구스토", "멀티팩", "캡슐"]]
#크롤러 함수 crawler_data_for_coupang(크롤링 할 요소, 인덱스, 페이지):
def crawler_data_for_coupang(Element, index, page):

    select_url = f"https://www.coupang.com/np/search?q={Element[index]}&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=salePriceAsc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={page}&rocketAll=false&searchIndexingToken=&backgroundColor="
    data = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

    request = requests.get(select_url, headers=data)
    soup = BeautifulSoup(request.text, "html.parser")

    #쿠팡의 물품 리스트
    find_name = soup.find_all("div", {"class": "name"})

    #쿠팡의 가격 list
    find_price = soup.find_all("strong", {"class": "price-value"})

    #쿠팡의 url_list
    find_url_temp = soup.find_all("a", {"class": "search-product-link"})
    find_url = []
    for url_print in find_url_temp:
        parse_url = url_print["href"]
        find_url.append("https://www.coupang.com" + parse_url)

    return find_name, find_price, find_url


# 인자로 input 리스트를 받는다
def select_data(category_n, name_check):
    return_list = []

    index_check_num = -1
    print(category_n)
    #n번째 카테고리의 Elemnet
    for Element in category_n:

        index_check_num += 1
        min_value = 9999999999
        flag = 0

        #index는 Element의 0번째, 1번째 요소를 보기 위함 ['프렌치카페카페믹스', '프렌치카페카페믹스 190*2', 32990] 여기서 '프렌치, 프렌치카페믹스로 된 결과값
        for index in range(0,2):

            # 원하는 페이지 수 1page부터 ~까지  page수를 동적으로 해야할 것 같은데 or try, except
            for page in range(1, 8):

                # 크롤러 작동
                find_name, find_price, find_url = crawler_data_for_coupang(Element, index, page)
                print(find_name)

                print(len(find_name))
                print(len(find_price))
                #찾은 제품을 순회한다. #여기서 인덱스 해결해야함
                for i in range(len(find_name)):

                    for j in range(len(name_check[index_check_num])):
                        # print("=================================================")
                        # print()
                        # print(name_check[index_check_num][j] + "으로 비교")
                        # print("쿠팡에 올라와있는  : " + find_name[i].text + " 입니다.")
                        if str(name_check[index_check_num][j]) not in str(find_name[i].text):
                            # print("존재하지 않습니다 . 존재하지 않습니다 . 존재하지 않습니다 . 존재하지 않습니다 . 존재하지 않습니다 . 존재하지 않습니다 . ")
                            break


                    for k in range(len(coffee_manual_keyword[index_check_num])):

                        if coffee_manual_keyword[index_check_num][k] not in str(find_name[i].text):
                            print("키워드가 들어가는 제품이 아닙니다 !")
                            break

                # print(find_name[i].text)
                # print(find_price[i].text)

                    compare_find_price = find_price[i].text.replace(",", "")
                    if min_value > int(compare_find_price) and int(compare_find_price) > Element[2] - 5000:
                        min_value = int(compare_find_price)
                        flag = i
                        temp_find_price = find_price[:]
                        temp_find_url = find_url[:]

        # 가격 젤 낮은 것 입력
        return_list.append([temp_find_price[flag].text, temp_find_url[flag]])

    return return_list