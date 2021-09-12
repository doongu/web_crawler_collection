import excel_controller as ec

if __name__ == '__main__':
    #ec.read_excel("데이터가 담겨있는 엑셀 경로")
    check_excel_input_value, check_name_list = ec.read_excel('C:/Users/Hellllo/Desktop/크몽/쿠팡 크롤링/test2.xlsx')

    print(check_name_list)
    # #엑셀에 쓰는 함수 실행
    ec.write_excel(check_excel_input_value, check_name_list)

    # for i in range(len(check_excel_input_value)):
    #     print(check_excel_input_value[i])
    # for i in range(20):
    #     print(check_name_list[i])