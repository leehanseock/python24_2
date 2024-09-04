# 과제 : 딕셔너리를 이용한 자동판매기
#if __name__ == "__main__":

# 딕셔너리를 사용한 메뉴 생성
menu = {1:{'콜라':500}, 2:{'사이다':500}, 3:{'물':800}, 4:{'파워에이드':1000}}
# menu_name = list(menu.keys())

# 메뉴 출력 함수
def print_menu():
    print("🥤한석벤딩🥤")
    for inner_dict in menu.values():
        for item, price in inner_dict.items():
            print(f'|{item}: {price}원|', end=' ')
print_menu()

# 현금 투입 함수
def insert_cash(money):
    print(f"현재 잔액 : {m}원", money) # 최초잔액 표시

# 메뉴 선택 함수
def make_a_choice(number):
    number =input("구매하고 싶은 음료 번호를 선택하여 주십시오:")
    try :
        print('ok')
    except KeyError as e:
        print("메뉴에 있는 번호를 선택해 주십시오.")