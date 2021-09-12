# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib3


# 되는 data 장바구니 담는걸로 함
# item 코드 찾기  # html에서 aBasketProductData[0]을 json으로 변환후 아이템 값 불러오기
url1 = "https://ohora.kr/product/detail.html?product_no=484&cate_no=160&display_group=1"
select_url = url1
headers={"User-Agent" : "Mozilla/5.0",
         "cookie" : "ohora.kr-crema_device_token=AaSW5uzRRK0CmnuN; wish_id=9379f3027e29a57a6b3e76b54b627df3; ECSESSID=9ac58035b179f385840f148d24da9566; CUK45=cuk45_ohora2019_9ac58035b179f385840f148d24da9566; CUK2Y=cuk2y_ohora2019_9ac58035b179f385840f148d24da9566; CID=CID5fb967e8cd32510380ca416a32e277b7; isviewtype=pc; org_phpsess_id_1=9ac58035b179f385840f148d24da9566; atl_epcheck=1; atl_option=1%2C1%2CH; ec_ipad_device=F; CID5fb967e8cd32510380ca416a32e277b7=9af4650863ac220f676414973feb2ab3%3A%3A%3A%3A%3A%3Ahttps%3A%2F%2Fwww.google.com%2F%3A%3A%EA%B5%AC%EA%B8%80%28%EB%AF%B8%EA%B5%AD%29%3A%3A1%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%2F%3A%3A1626795372%3A%3A%3A%3Appdp%3A%3A1626795372%3A%3A%3A%3A%3A%3A%3A%3A; recent_plist=285; return_url=/; iscache=F; ec_mem_level=1; PHPSESSVERIFY=4bf62e726b45c2db5ae160151e3ae0bc; basketcount_1=0; basketprice_1=0; couponcount_1=1; ec_async_cache_avail_mileage_1=0.00; ec_async_cache_used_mileage_1=0.00; ec_async_cache_returned_mileage_1=0; ec_async_cache_unavail_mileage_1=0; ec_async_cache_used_deposit_1=0; ec_async_cache_all_deposit_1=0; ec_async_cache_deposit_refund_wait_1=0; ec_async_cache_member_total_deposit_1=0; ohora.kr-crema_review_popup_count_v2=3; vt=1626796001; wishcount_1=1"
         }
request = requests.post(select_url,data = data,headers = headers, verify=False)
soup = BeautifulSoup(request.text, "html.parser")
soup = str(soup)
index = soup.find("var item_code")
print(soup[index + 17 :index + 29])
# printer = soup.find("td",{"class", "right"})

# print(printer)

# print(soup)

url2 = "https://www.ohora.kr/exec/front/order/Basketduplicate/" # 재입고아님
select_url = url2
data = {
'selected_item[]': '1||P00000RV000A', # 이걸 알아내는게 중요함 .. 위에서 알아낸 뒤 장바구니 요청을 보내본다.
'product_no': '463',
'command': 'add',

}


headers={"User-Agent" : "Mozilla/5.0",
         "cookie" : "ohora.kr-crema_device_token=HGF4BfQ1OTnUgUfB; CUK45=cuk45_ohora2019_3be4022487cb5f0ed61587e4aa95f21b; CUK2Y=cuk2y_ohora2019_3be4022487cb5f0ed61587e4aa95f21b; wish_id=55c356547a5f9fb0557e6b23a6116563; isviewtype=pc; return_url=/; ec_ipad_device=F; CID=CID652a8b9179a60a09824ced7e9d8f5b5e; CID652a8b9179a60a09824ced7e9d8f5b5e=893c8191810191a9b3b45189c7c5c832%3A%3A%3A%3A%3A%3Ahttps%3A%2F%2Fwww.google.com%2F%3A%3A%EA%B5%AC%EA%B8%80%28%EB%AF%B8%EA%B5%AD%29%3A%3A1%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%2F%3A%3A1627023112%3A%3A%3A%3Appdp%3A%3A1627023112%3A%3A%3A%3A%3A%3A%3A%3A; ECSESSID=02ec5352d4219f63af2a45b4e53c8581; org_phpsess_id_1=02ec5352d4219f63af2a45b4e53c8581; atl_epcheck=1; atl_option=1%2C1%2CH; recent_plist=844%7C484%7C1064%7C285; iscache=F; ec_mem_level=1; PHPSESSVERIFY=234566d53d3bb41cd862d175e52badbe; basketcount_1=5; basketprice_1=72%2C000; couponcount_1=1; ec_async_cache_avail_mileage_1=0.00; ec_async_cache_used_mileage_1=0.00; ec_async_cache_returned_mileage_1=0; ec_async_cache_unavail_mileage_1=0; ec_async_cache_used_deposit_1=0; ec_async_cache_all_deposit_1=0; ec_async_cache_deposit_refund_wait_1=0; ec_async_cache_member_total_deposit_1=0; wishcount_1=2; ohora.kr-crema_review_popup_count_v2=3; vt=1627023217"
         }

request = requests.post(select_url,data = data,headers = headers, verify=False)
soup = BeautifulSoup(request.text, "html.parser")
# print(soup)
