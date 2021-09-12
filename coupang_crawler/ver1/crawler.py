# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
# head_object_mannual_keyword = [["페리오","히말라야핑크솔트치약", "160*5"], ["팬틴", "어드밴스드케어샴푸", "1.13"], ["팬틴", "어드밴스드케어컨디셔너", "1.13"], ["오가니스트", "샴푸까리떼", "980"], ["오가니스트", "샴푸블랙솔트", "980"], ["오가니스트", "컨디셔너까리떼", "980"],
#                 ["오가니스트", "컨디셔너","블랙솔트", "980"], ["모노티크", "샴푸", "라벤더", "1500*2"], ["비타브리드", "샴푸", "1000"], ["알페신샴푸", "375*2"], ["닥터포헤어", "폴리젠샴푸", "750*2+100"], ["닥터포헤어", "피토테라피샴푸", "750*2+100"],
#                 ["팬틴", "오일샴푸", "1.13"], ["닥터그루트", "에딕트헤어세트", "샴푸680"], ["무코타", "헤어트리트먼트", "160*2"], ["코린드팜", "2in1", "250*3"], ["실크테라피", "헤어에센스", "180+60+15"], ["헤드스파7", "파란눈블랙헤어팩", "300*2+35"],
#                 ["실크테라피", "샤인트리트먼트", "500+100"], ["우르오스", "바디클렌저", "500"], ["커클랜드", "바디워시","800*2"], ["세타필", "바디워시", "1000"], ["모노티크", "바디워시", "1500*2"], ["온더바디스크럽", "바디워시", "블랙로즈", "600*2"],
#                 ["온더바디스크럽", "바디워시", "히말라야", "600*2"], ["뉴트로지나", "레인바스샤워젤", "1182"], ["말랑이", "버블핸드워시", "500*2+450*3"], ["아비노", "바디워시", "1000"], ["카오", "화이트솝", "12"],
#                 ["커클랜드", "바디솝", "15"], ["오스트레일리안", "보태니컬비누", "200*8"], ["글락소스미스", "센소다인", "100*5"], ["콜게이트", "그레이트레귤러", "250*5"], ["파로돈탁스", "치약", "100*6"],
#                 ["레드씰", "어린이치약", "75*4"], ["레드씰", "프로폴리스", "160*4"], ["리치", "키즈칫솔", "8"], ["리치","키즈칫솔", "유아", "8"], ["오랄비", "9000엑스퍼트", "7"], ["오랄비", "프로플렉스", "6"], ["오랄비","치간칫솔", "20*3"],
#                 ["검", "치간칫솔", "80*3"], ["플렉커스", "어린이", "치실", "75*3"], ["가그린", "제로오리지널", "1350*2+750"], ["오랄비", "글라이드", "민트향", "44*6"], ["글락소스미스", "폴리덴트", "의치세정제", "108"],
#                 ["리스테린", "그린티", "1.5*2"], ["리스테린", "헬시브라이트", "1.5*2"], ["리스테린", "쿨민트", "1.5*2"], ["피지오겔", "dmt", "200*2"], ["버츠비", "립밤", "5"], ["히말라야", "너리싱", "크림", "200*2"],
#                 ["피지오겔", "바디로션", "400*2"], ["바이오더마", "아토덤", "500*2"], ["라운드랩", "독도토너", "350*2"], ["라운드랩", "독도클렌저", "150*2+40"], ["닥터브로너스", "오가닉스킨소프트너", "475"],
#                 ["뉴트로지나", "딥클린", "클렌저", "175*2+100"], ["시세이도", "센카", "클렌저", "120*3+40"], ["참존", "징코", "클렌징티슈", "70*2+10"]]
# #
# snack_mannual_keyword = [["프리토레이", "버라이어티", "878"], ["팝코너스", "칩", "28*24"], ["마마스초이스", "닭가슴살칩", "30*7"], ["커클랜드", "핑크솔트", "감자칩","907"], ["프리토레이", "레이즈", "425"], ["신화당", "오란다", "175*12"],
#                 ["리츠", "크래커", "1.74"], ["뚜부", "크래커", "50*7"], ["프리미엄", "솔틴크래커", "1.36"], ["켄지", "파", "크래커", "15*42"], ["mars", "체다치즈", "크래커", "867"], ["커피", "누가크래커", "198*2"],
#                 ["로아커", "웨하스믹스", "800"], ["퀘이커", "그래놀라", "시리얼", "1125"], ["커클랜드", "피넛버터", "프레첼", "1.56"], ["슐츠", "프레첼", "1.56"], ["두보식품", "서리태스낵", "650"], ["오리온", "오징어땅콩콤보", "6"],
#                 ["맥스봉", "치즈플러스", "40*27"], ["청정원", "고구마츄", "90*5"], ["cj","맛밤", "42*17"], ["화과방", "영양갱", "40*40"], ["삼립", "약과", "1.5"], ["신화당", "종합전병", "918"], ["오리온", "초코파이", "39*72"],
#                 ["오리온", "카스타드", "48"], ["jaquet", "브라우니믹스", "150*5"], ["프레디", "피네스케이크", "39*80"], ["프레디", "스트로베리", "요거트","25*80"], ["켄지", "프레쉬", "버터파이", "720"], ["poult", "타르트", "900"],
#                 ["밀레폴리", "페스트리", "25*40"], ["오레오", "쿠키", "50*30"], ["마늘빵집", "갈릭", "바게뜨", "100*6"], ["네이처프렌드", "체다", "까망베르", "60*20"], ["켄지", "고프레", "바닐라", "초코", "630"],
#                 ["페퍼리지", "밀라노", "다크", "425"], ["라메르풀라", "쿠키", "틴", "750"], ["포피스", "카라멜라이즈", "쿠키", "300"], ["비첸지", "쿠키", "컬렉션", "907"], ["커클랜드", "벨기에", "쿠키", "1.4"], ["커클랜드", "허니머스타드", "스낵" ,"850"],
#                 ["오리온", "프로틴바", "미니", "594"], ["로카", "치즈", "비스킷", "580"], ["네이처밸리", "프로틴바", "1.2"], ["유기농", "현미강정", "125*4"], [""""""],





#크롤러 함수 crawler_data_for_coupang(크롤링 할 요소, 인덱스, 페이지):
def crawler_data_for_coupang(Element, index, page):

    t_find_delivery_return = []
    t_find_name = []
    t_find_price = []

    select_title = ""
    select_price = ""
    find_delivery = ""
    select_url = f"https://www.coupang.com/np/search?q={Element[index]}&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=salePriceAsc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={page}&rocketAll=false&searchIndexingToken=&backgroundColor="
    data = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    try:
        request = requests.get(select_url, headers=data, timeout = 10, verify=False)
        soup = BeautifulSoup(request.text, "html.parser")
    except:
        time.sleep(5)
        request = requests.get(select_url, headers=data, timeout=10, verify=False)
    soup = BeautifulSoup(request.text, "html.parser")
    # except requests.exceptions.Timeout as errd:
    #     print("Timeout Error : ", errd)
    #
    # except requests.exceptions.ConnectionError as errc:
    #     print("Error Connecting : ", errc)
    #
    # except requests.exceptions.HTTPError as errb:
    #     print("Http Error : ", errb)
    #
    # # Any Error except upper exception
    # except requests.exceptions.RequestException as erra:
    #     print("AnyException : ", erra)

    # 이렇게 찾으면 깔끔하게 다 찾아줌
    select_rocket = soup.find_all("li", {"class": "search-product"})

    #물품의 링크를 다 찾는다.
    find_url_temp = soup.find_all("a", {"class": "search-product-link"})

    # 배송 처리
    # print(select_rocket[11].find("span", {"class" : "badge rocket"}))
    t_find_url = []

    for i in range(len(select_rocket)):
        try:
            check_rocket = None
            check_global = None
            check_rocket = select_rocket[i].find("span", {"class": "badge rocket"})

            check_global = select_rocket[i].find("span", {"class": "badge global"})
            check_sold_out = select_rocket[i].find("div", {"class":"out-of-stock"})
            # print(check_sold_out)
            parse_url = select_rocket[i].find("a", {"class": "search-product-link"})["href"]

            if check_rocket == None and check_global == None and check_sold_out == None :

                t_find_url.append("https://www.coupang.com" + parse_url)
            else:
                t_find_url.append("None")

            # .find("span", {"class" : "badge rocket"})
        except:
            pass

    #찾은 페이지의 로켓, 직구를 제외한 상품들의 안에 들어가서 가격, 배송비를 뽑아온다.
    for url in t_find_url:
        if url != "None":
            select_url = url
            data = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
            try:
                request = requests.get(select_url, headers=data, timeout = 10, verify=False)
                soup = BeautifulSoup(request.text, "html.parser")
            except:
                time.sleep(5)
                request = requests.get(select_url, headers=data, timeout=10, verify=False)
            soup = BeautifulSoup(request.text, "html.parser")
            # except requests.exceptions.Timeout as errd:
            #     print("Timeout Error : ", errd)
            #
            # except requests.exceptions.ConnectionError as errc:
            #     print("Error Connecting : ", errc)
            #
            # except requests.exceptions.HTTPError as errb:
            #     print("Http Error : ", errb)
            #
            # # Any Error except upper exception
            # except requests.exceptions.RequestException as erra:
            #     print("AnyException : ", erra)

            select_title = soup.find("h2", {"class": "prod-buy-header__title"})
            select_price = soup.find("span", {"class": "total-price"})
            find_delivery = soup.find("div", {"class": "prod-shipping-fee-message"})
            # len 이 에러나면 링크는 있지만품절 상품이다. 품절 상품은 젤 뒤에 있으니 for문을 끝낸다
            try:
                a,b,c = len(select_title), len(select_price), len(find_delivery)
            except:
                print("품절 상품입니다.")
                break
            #배송비 문자열 슬라이싱


            temp = find_delivery.text.replace("\n", "")
            if temp == "무료배송":
                temp_delivery = "무료배송"
                t_find_delivery_return.append(temp_delivery)

            else:

                temp_delivery = ""
                for i in range(len(temp) - 1, -1, -1):
                    temp_delivery += temp[i]
                    if temp[i] == " ":
                        break
                temp_delivery = temp_delivery[::-1]
                # temp_delivery.replace(",", "")[:-1]
                if temp_delivery.replace(",", "").replace("원", "").strip() == "알아보기":
                    t_find_delivery_return.append("무료배송")

                else:
                    t_find_delivery_return.append(temp_delivery.replace(",", "").replace("원", "").strip())

            t_find_name.append(select_title.text.replace("\n", ""))
            t_find_price.append(select_price.text.replace("\n", "").replace("원", "").replace(",", ""))

    def remove_values_from_list(the_list, val):
        return [value for value in the_list if value != val]


    t_find_url = remove_values_from_list(t_find_url, 'None')


    return t_find_name, t_find_price, t_find_url, t_find_delivery_return


# 인자로 input 리스트를 받는다
def select_data(category_n, name_check, check_mannual_key_n):
    return_list = []
    check_flag = True

    index_check_num = -1
    print(category_n)
    #n번째 카테고리의 Elemnet
    flag_break = 0
    for Element, mannual_Element in zip(category_n, check_mannual_key_n):
        flag_break = 0
        # #품목보다 많이 비싸면 멈춰버림
        # if flag_break == 2:
        #     break
        #     flag_break = 0

        print(mannual_Element)
        index_check_num += 1
        min_value = 9999999999
        flag = -1

        #index는 Element의 0번째, 1번째 요소를 보기 위함 ['프렌치카페카페믹스', '프렌치카페카페믹스 190*2', 32990] 여기서 '프렌치, 프렌치카페믹스로 된 결과값
        for index in range(0,len(Element)-2):
            print("==============", Element[index],"를 검색합니다.================")
            print("==============", Element[-1], "원을 원합니다. 검색합니다.================")
            print("\n")
            # 원하는 페이지 수 1page부터 ~까지  page수를 동적으로 해야할 것 같은데 or try, except
            for page in range(1, 10):
                print("flag break 값 : " , flag_break)
                if flag_break == 2:
                    flag_break = 0
                    break
                # 크롤러 작동
                find_name, find_price, find_url, find_delivery = crawler_data_for_coupang(Element, index, page)
                print(find_name)
                print(find_price)
                print(find_url)
                print(len(find_name))
                print(len(find_price))
                print(len(find_url))
                if len(find_url) == 0:
                    break
                #찾은 제품을 순회한다. #여기서 인덱스 해결해야함

                for i in range(len(find_name)):
                    if flag_break == 1:
                        flag_break = 2
                        break
                    for k in range(len(check_mannual_key_n[index_check_num])):
                        check_or_cnt = 0
                        for m in range(len(check_mannual_key_n[index_check_num][k])):
                            if check_mannual_key_n[index_check_num][k][m] in str(find_name[i]):
                                check_or_cnt += 1
                                break

                        print("제품명 출력 : ", find_name[i])
                        print("배송비 출력 : ", find_delivery[i])
                        print("가격 출력 : ", find_price[i])
                        print("url 출력 : ", find_url[i])

                        if check_or_cnt == 0:
                            print("'" ,check_mannual_key_n[index_check_num][k], "'", "키워드가 들어가는 제품이 아닙니다 !")
                            print("\n\n")

                            check_flag = False
                            break


                    if check_flag == False:
                        check_flag = True
                        continue
                    
                    #임시로 배송비와 가격을 더하는 부분
                    try:
                        price_plus_delivery = int(find_price[i])
                        print("제품명 출력 : ", find_name[i])
                        print("배송비 출력 : ",find_delivery[i])
                        print("가격 출력 : ",find_price[i])
                        print("url 출력 : ",find_url[i])
                        if find_delivery[i] != "무료배송":
                            price_plus_delivery += int(find_delivery[i])
                        print("배송비 + 가격 출력: ", price_plus_delivery)
                        print("비교할 가격은 : ", Element[-1])



                        #연속 두번 같은값이 들어가는게 여기를 만족하는 제품이 없어서 , !!!
                        if min_value > price_plus_delivery and price_plus_delivery >= Element[-1] - int(Element[-1] * 0.3):
                            min_value = price_plus_delivery
                            flag = i
                            temp_find_price = find_price[:]
                            temp_find_url = find_url[:]
                            temp_find_delivery = find_delivery[:]
                            print("가격대가 맞습니다. 저장합니다.")
                            print("\n\n")
                        elif price_plus_delivery > int(Element[-1] * 2.0):
                            print("가격이 너무 차이나므로 다음 품복으로 넘어갑니다.")
                            print("\n\n")
                            flag_break = 1
                            break
                        else:
                            print("가격대가 맞지 않습니다.")
                            print("\n\n")
                    except:
                        continue
        # 가격 젤 낮은 것 입력
        if flag == -1:
            print("제품이 존재하지 않습니다.", "제품이 존재하지 않습니다.", "제품이 존재하지 않습니다.")
            return_list.append(["제품이 존재하지 않습니다.", "제품이 존재하지 않습니다.", "제품이 존재하지 않습니다."])

        else:
            print(temp_find_price[flag], temp_find_delivery[flag], temp_find_url[flag], "를 추가합니다. !!!!!!!!!!!!!!!!!!!!!!!!" )
            return_list.append([temp_find_price[flag], temp_find_delivery[flag], temp_find_url[flag] ])

    return return_list