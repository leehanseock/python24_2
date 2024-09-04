# 과제 : 딕셔너리를 이용한 자동판매기

# 중첩 딕셔너리를 사용한 메뉴 생성
menu = {1: {'콜라': 500}, 2: {'사이다': 500}, 3: {'물': 800}, 4: {'파워에이드': 1000}}
# menu_name = list(menu.keys())

# 메뉴 가격만 추출하기
def get_prices():
    prices = []
    for values2 in menu.values():
        for price in values2.values():
            prices.append(price)
    return prices
# get_prices() 함수 호출 및 결과 저장
prices = get_prices()

# 메뉴 이름만 추출하기
def get_menu_names():
    menu_names = []
    for item in menu.values():
        menu_names.extend(item.keys())  # item.keys()는 dict_keys 객체를 반환합니다.
    return menu_names
# get_names() 함수 호출 및 결과 저장
menu_names = get_menu_names()

# prices 출력
# print(prices)
# print('최솟값',min(prices))

# 메뉴 출력 함수
def print_menu():
    print("🥤한석벤딩🥤")
    for i in range(len(menu_names)):
        print("|",f"{i+1}번 {menu_names[i]} : {prices[i]}원 ", end = "|")
    print()

# 현금 투입 함수
# balance = 0 #이 부분 어떻게 java의 private 변수처럼 외부 접근 방지할지 고민
def insert_cash(money):
    print("(🚨정수만 입력하세요. 0을 입력시 구매가 종료됩니다.)")
    print(f"투입금액: {money}원")
    try :
        cash = int(input("현금을 투입해주십시오:"))
        money += cash
        if cash == 0: #거래 종료
            print(f"거래가 종료되었습니다. 잔액 {money}원을 받아주십시오.")
            return 0
        elif money > 0:
            money = choose(money)
            return money
    except Exception :
        print("현금만 투입해 주십시오.") # 입력값이 정수가 아닌 경우 예외 처리
        return money

# 메뉴 선택 함수
def choose(inserted) :
    try :
        menu_num = int(input("구매하실 음료 번호를 메뉴에서 선택해 주십시오:"))
        if inserted >= prices[menu_num-1]:
            print(f"{menu_num}번 {menu_names[menu_num-1]}을 선택하셨습니다. ")
            # 거스름돈 계산 & 음료 제공 함수 호출
            inserted = process_order(menu_num-1, inserted)
            return inserted
        else :
            print("투입 금액이 부족합니다.")
            return inserted
    except Exception:
        print("메뉴에 있는 번호를 선택해주셔야 합니다.")
        return inserted

# 음료 제공 & 거스름돈 반환 함수
def process_order(num, inserted2):
    inserted2 -= prices[num]
    print(f"{menu_names[num]}가/이 나옵니다. 음료를 받아주세요.")
    print(f"거스름 돈은 {inserted2}원 입니다.")
    return inserted2

# 구조
def vendingmachine():
    balance = 0
    while True:
        print_menu()
        balance = insert_cash(balance)
        print("=====================================================")
        if balance == 0 :
            break

# 메인 문
if __name__ == "__main__":
    vendingmachine()