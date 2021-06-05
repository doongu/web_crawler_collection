# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib3
import json

#입력 받고 , 리스트들 출력.
urllib3.disable_warnings() 

def get_url_html(input_, f_num, s_num):

    select_url = f"https://search.11st.co.kr/Search.tmall?method=getCatalogPrdSearch&catalogYN=Y&kwd={input_}#pageNum%%{f_num + 1}%%page%%{s_num*2 - 1}"
    data = {
        'methond' : 'getCatalogPrdSearch',
        'catalogYN' : 'Y',
        'kwd' : f'{input_}'
    }
    request = requests.get(login_url, data = data, verify=False)
    soup = BeautifulSoup(request.text, "html.parser")
    temp = soup.text
    # print(temp)
    index = temp.find("window.searchDataFactory.catalogPrdList = ")
    index2 = temp.find("window.searchDataFactory.popKeyword")
    len_temp = len("window.searchDataFactory.catalogPrdList = ")

    answer = str(temp[index + len_temp : index2])
    answer = str(answer.strip())
    answer = str(answer[:-1])
    jsonobject = json.loads(answer)
    return jsonobject

while True:
    #첫페이지는 그대로
    input_ = str(input())
    login_url = f"https://search.11st.co.kr/Search.tmall?method=getCatalogPrdSearch&catalogYN=Y&kwd={input_}"

    data = {
        'methond' : 'getCatalogPrdSearch',
        'catalogYN' : 'Y',
        'kwd' : f'{input_}'
    }
    request = requests.get(login_url, data = data, verify=False)
    soup = BeautifulSoup(request.text, "html.parser")
    temp = soup.text
    # print(temp)
    index = temp.find("window.searchDataFactory.catalogPrdList = ")
    index2 = temp.find("window.searchDataFactory.popKeyword")
    len_temp = len("window.searchDataFactory.catalogPrdList = ")

    answer = str(temp[index + len_temp : index2])
    answer = str(answer.strip())
    answer = str(answer[:-1])
    jsonobject = json.loads(answer)
    # for i in range(len(jsonobject["items"])):
    # print(json.dumps(jsonobject["items"][1]["modelExactSellers"][0]["nckNm"], indent = 2)) #가격비교 최저가 명
    # for j in range(len(jsonobject["items"][i])):
    #     jsonobject["items"][i]["modelExactSellers"][j]["nckNm"]
    #     print(a)
    # for i in range()
    # input_ = str(input())

    #jsonobject["items"][n번째 대표 상품]["modelExactSellers"][0]["nckNm" = 가격비교란의 최저가 명, "nckNm" = 가격비교란의 최저가 가격, "productDetailUrl" = 최저가 파는 곳 링크]
    #jsonobject["items"][1]["prdNm" = 대표 상품명, "finalPrc" = 대표 상품 가격]

    print("1 번째 페이지입니다.")
    for i in range(0, len(jsonobject["items"])):
        print("대표 상품입니다. : " + jsonobject["items"][i]["prdNm"]) #대표 상품명
        print("대표 가격입니다. : " +jsonobject["items"][i]["finalPrc"]) #대표 상품 가격
        print("가격비교 최저가 명입니다. : " + jsonobject["items"][i]["modelExactSellers"][0]["nckNm"]) #가격비교 최저가 명
        print("가격비교 최저자 가격입니다. : " + jsonobject["items"][i]["modelExactSellers"][0]["finalPrc"]) #가격비교 최저가
        print("가격비교 최저가 물품 링크입니다. : " + jsonobject["items"][i]["modelExactSellers"][0]["productDetailUrl"]) #최저가 파는곳 링크
        print("")
        print("-----------------------------------------------------------------------------------")
        print("")
    for k in range(4):
            print("-----------------------------------------------------------------------------------")


    for i in range(2, 4):  #page 수
        jsonobject = get_url_html(input_, i, 2*(i-1) - 1) #n번쨰 page 값을 넣는다.
        print(str(i) + "번째 페이지입니다.")
        for j in range(0, len(jsonobject["items"])): 
            print("대표 상품입니다. : " + jsonobject["items"][j]["prdNm"]) #대표 상품명
            print("대표 가격입니다. : " +jsonobject["items"][j]["finalPrc"]) #대표 상품 가격
            print("가격비교 최저가 명입니다. : " + jsonobject["items"][j]["modelExactSellers"][0]["nckNm"]) #가격비교 최저가 명
            print("가격비교 최저자 가격입니다. : " + jsonobject["items"][j]["modelExactSellers"][0]["finalPrc"]) #가격비교 최저가
            print("가격비교 최저가 물품 링크입니다. : " + jsonobject["items"][j]["modelExactSellers"][0]["productDetailUrl"]) #최저가 파는곳 링크
            print("")
            print("-----------------------------------------------------------------------------------")
            print("")
        for k in range(4):
            print("-----------------------------------------------------------------------------------")
        
        


# #-------------------------------------------------------------------------
# #       위 코드는 크롤링과 관련된 코드 , 아래코드는 엑셀과 관련된 코드
# #-------------------------------------------------------------------------

# '''엑셀 코드'''



# listdata = [] #엑셀에 담을 리스트 선언]

# #엑셀에 넣을 때 1행씩 담을 것이므로 아까 수집한 데이터들을 내가 원하는 형태로 바꾸어 준다.
# '''
#               -------------------------
#  mall name => | 11번가 | G마켓 | 쿠팡 |
#               -------------------------
#  mall_urr =>  | url1   | url2 | url3 |
#               --------------------------
# 이거를
#           -----------------
#  행 1 =>  | 11번가 | ur1  |
#           -----------------
#  행 2 =>  | G마켓  | url2 |
#           -----------------
#  행 2 =>  | 쿠팡   | url3 |
#           -----------------
# 이렇게 바꿔줘야 나중에 엑셀에 넣을 때 편하기에 아래코드는 합치는겸 이렇게 바꿔줌
# '''
# #내가 수집한 데이터를 원하는 형태로 바꾸는 코드
# for i in range(20):
#     listdata.append([mall_name[i],mall_url[i],mall_intro[i],mall_item[i],mall_grade[i]])


# #엑셀파일을 생성하고 열고,  열 너비를 지정하고, 데이터를 추가하는 코드
# def write_excel_template(filename, sheetname, listdata):
#     excel_file = openpyxl.Workbook() #새 엑셀파일 생성
#     excel_sheet = excel_file.active #시트를 여는 코드

#     #각 열에 대해서 길이를 지정해줌
#     excel_sheet.column_dimensions['A'].width = 30
#     excel_sheet.column_dimensions['B'].width = 30
#     excel_sheet.column_dimensions['C'].width = 82
#     excel_sheet.column_dimensions['D'].width = 30
#     excel_sheet.column_dimensions['E'].width = 30

#     #sheetname이 비어있는 값이아니면 입력받은 sheetname으로 이름 저장
#     if sheetname != '':
#         excel_sheet.title = sheetname #sheet이름 저장

#     #입력 받은 listdata를 순회하면서 엑셀에 한 줄씩 추가하는 코드
#     for item in listdata:
#         excel_sheet.append(item) #엑셀 안에 한 줄씩 추가

#     excel_file.save(filename) #입력받은 filename으로 엑셀파일 저장
#     excel_file.close()


# #아까 내가 작성한 write_excel_template 함수 호출
# write_excel_template("TEST.xlsx",'TEST' , listdata)
# #write_excel_template("엑셀파일명.xlsx", '시트명', 데이터가 담긴 리스트)
