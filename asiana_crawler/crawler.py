from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import os, shutil

# javascript 형태이기 때문에 python의 selenium으로 처리해준다.
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory' : r'C:\Users\Han\Desktop\answer'})


def crawler_damage(damage_txt):
    url = "https://www.asianacargo.com/tracking/viewOalDamage.do" # url 입력
    driver = webdriver.Chrome(executable_path='chromedriver', options=chrome_options) # chromedriver를 통해 chrome을 제어해야한다. (크롱 공식 사이트에서 다운로드 하시면 됩니다.)
    driver.set_window_position(0, 0)    # 크롬창의 위치 설정 부분
    driver.set_window_size(1600, 1000)  # 크롬창의 크기 설정 부분 

    # txt파일을 받아서 한줄씩 list에 추가해준다.
    f = open(damage_txt, "r")
    list_code = []
    while True:
        line = f.readline()
        if not line: break
        list_code.append(line)
    f.close()


    for i in range(len(list_code)):

        driver.get(url) # url을 크롬드라이브를 이용해 엽니다.
        driver.implicitly_wait(5) # 화면이 로딩하는 시간이 있기에 wait시간을 걸어주었습니다. (time으로 걸어도 됩니다.)
        search_val = driver.find_element_by_id("search_val")  # 현재 크롬창에서 search_val을 id값으로 가지는 요소를 변수에 저장
        driver.implicitly_wait(1) # 대기
        search_val.send_keys(list_code[i]) # text 값을 전달합니다.(입력합니다.)

        driver.implicitly_wait(1) # 대기
        search = driver.find_element_by_id("btn_searchOalDamage") # 조회 버튼의 id값을 찾아 입력했습니다.
        search.click() # 클릭 메소드, (조회 버튼을 클릭합니다.)
        time.sleep(5) # 대기
        driver.implicitly_wait(2) # 대기

        confirm_paper = driver.find_element_by_xpath('//*[@id="damageTable"]/tbody/tr/td[12]/button') # xpath 형식으로 크롤링 ( 이 방법이 더쉽습니다. )
        confirm_paper.click() # 확인서를 클릭합니다. 
        driver.implicitly_wait(2) # 대기
        driver.execute_script("window.scrollTo(0, 1000);") # 사실 안넣어도 되는데, 그래도 프로그램이 활기차게 동작하는 것처럼 보이게 하기 위해 넣었습니다. 스크롤을 내려주는 기능입니다.
        time.sleep(5) # 대기
        
        down_pdf = driver.find_element_by_id("btn_print") # pdf 버튼의 id값을 찾아서 넣었습니다.
        down_pdf.click() # pdf 다운 버튼 클릭
        time.sleep(5) # 대기

        filepath = r'C:\Users\Han\Desktop\answer'
        filename = max([filepath + "\\" + f for f in os.listdir(filepath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(filepath, list_code[i].replace("\n", "") + ".pdf"))