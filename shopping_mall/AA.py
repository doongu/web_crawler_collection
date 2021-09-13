#requests방식의 크롤러 모듈
import requests
from bs4 import BeautifulSoup
import openpyxl #python-excel 모듈


'''크롤러 코드 '''
req = requests.get("https://search.shopping.naver.com/mall/mall.nhn") #문의하신 url에 get요청을 보내는 것, 사람이 그냥 웹사이트 들어가는 거랑 같음
html = req.content #url에 요청 -> html문서를 우리가 봄 == html문서가 req에 저장된다. 이를 편하게 다루기 위해 content로 변경
soup = BeautifulSoup(html, "html.parser") #beautifulSoup를 적용해줘야 크롤링할 함수들을 사용할 수 있음.



# find_all은 리스트로 저장해준다, 반면에 find 는 가장 먼저 찾은 것만 저장한다.
soup_div = soup.find("div", {"class": "malltv_lst"}) #얻고자 하는 데이터들의 폼을 가져오는 코드




### 쇼핑몰명 ###
mall_name = [] #mall_name을 저장할 리스트 선언
temp = soup_div.find_all("img") #temp는 잠시 값을 담기위해 넣어둔 것임

#temp를 돌면서 alt태그의 값을 가져옴
for i in range(0, len(temp)):
    mall_name.append(temp[i]["alt"])
#print(mall_name)



### URL 명 ###
mall_url = [] #mall_url을 저장할 리스트 선언
temp = soup.find_all("td", {"class": "url"})  #temp는 잠시 값을 담기위해 넣어둔 것임

#temp를 돌면서 값을 가져옴, .text는 거기에 들어있는 text를 가져옴 ex) <p>asd</p> 에 .text를 하면 asd만 추출해옴.
for i in range(0, len(temp)):
    mall_url.append(temp[i].text)
# print(mall_url)



### 쇼핑몰 소개 ###
mall_intro = [] #mall_intro을 저장할 리스트 선언
temp = soup.find_all("td", {"class": "intro"}) #temp는 임의의 변수

#p태그와 span태그를 찾아서 저장하는 코드
for i in range(0, len(temp)):
    mall_intro.append(temp[i].find("p").text.replace(",",":") + temp[i].find("span").text.replace("\t", "").replace("\n", " ")) #공백제거 및 합치기.
# print("쇼핑몰 소개 : " + mall_intro[0].text.replace(" ", ""))




### 상품개수 ###
mall_item = [] #저장할 리스트를 선언
temp = soup.find_all("td", {"class": "item"}) #모든 item들을 찾는다.

#temp를 돌며 text값을 추가하는 코드
for i in range(0, len(temp)):
    mall_item.append(temp[i].text[1:-1]) #깨끗하게 보이기 위해 양끝에 오는 값 제거
#print(mall_item)

print(mall_item)


### 몰 등급 ###
mall_grade = []
temp = soup.find_all("td", {"class": "mall_grade"})

for i in range(0, len(temp)):
    if temp[i].find("span", {"class": "grade"}): #비어있는 값이 있어서 if문으로 처리 , 만약 값이 있다면 기본적으로 추가하고
        mall_grade.append(temp[i].find('span').text)
    else:                                       #값이 없으면 공백을 추가
        mall_grade.append(" ")

# print(mall_grade)





#-------------------------------------------------------------------------
#       위 코드는 크롤링과 관련된 코드 , 아래코드는 엑셀과 관련된 코드
#-------------------------------------------------------------------------




'''엑셀 코드'''



listdata = [] #엑셀에 담을 리스트 선언]

#엑셀에 넣을 때 1행씩 담을 것이므로 아까 수집한 데이터들을 내가 원하는 형태로 바꾸어 준다.
'''
              -------------------------
 mall name => | 11번가 | G마켓 | 쿠팡 |
              -------------------------
 mall_urr =>  | url1   | url2 | url3 |
              --------------------------
이거를
          -----------------
 행 1 =>  | 11번가 | ur1  |
          -----------------
 행 2 =>  | G마켓  | url2 |
          -----------------
 행 2 =>  | 쿠팡   | url3 |
          -----------------
이렇게 바꿔줘야 나중에 엑셀에 넣을 때 편하기에 아래코드는 합치는겸 이렇게 바꿔줌
'''
#내가 수집한 데이터를 원하는 형태로 바꾸는 코드
for i in range(20):
    listdata.append([mall_name[i],mall_url[i],mall_intro[i],mall_item[i],mall_grade[i]])




#엑셀파일을 생성하고 열고,  열 너비를 지정하고, 데이터를 추가하는 코드
def write_excel_template(filename, sheetname, listdata):
    excel_file = openpyxl.Workbook() #새 엑셀파일 생성
    excel_sheet = excel_file.active #시트를 여는 코드

    #각 열에 대해서 길이를 지정해줌
    excel_sheet.column_dimensions['A'].width = 30
    excel_sheet.column_dimensions['B'].width = 30
    excel_sheet.column_dimensions['C'].width = 82
    excel_sheet.column_dimensions['D'].width = 30
    excel_sheet.column_dimensions['E'].width = 30

    #sheetname이 비어있는 값이아니면 입력받은 sheetname으로 이름 저장
    if sheetname != '':
        excel_sheet.title = sheetname #sheet이름 저장

    #입력 받은 listdata를 순회하면서 엑셀에 한 줄씩 추가하는 코드
    for item in listdata:
        excel_sheet.append(item) #엑셀 안에 한 줄씩 추가

    excel_file.save(filename) #입력받은 filename으로 엑셀파일 저장
    excel_file.close()


#아까 내가 작성한 write_excel_template 함수 호출
write_excel_template("TEST3.xlsx",'TEST' , listdata)
#write_excel_template("엑셀파일명.xlsx", '시트명', 데이터가 담긴 리스트)