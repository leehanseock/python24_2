# 과제 : 딕셔너리를 이용한 자동판매기
#if __name__ == "__main__":

# 딕셔너리를 사용한 메뉴 생성
menu = {'콜라':500, '사이다':500, '물':800, '파워에이드':1000}
# menu_name = list(menu.keys())

# 메뉴 출력 함수
def print_menu():
    print("🥤한석벤딩🥤")
    for k, v in menu.items():
        print(f'{k}: {v}원', end=' / ')
# print_menu()