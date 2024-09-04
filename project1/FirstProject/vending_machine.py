# 과제 : 딕셔너리를 이용한 자동판매기
#if __name__ == "__main__":

# 중첩 딕셔너리를 사용한 메뉴 생성
menu = {1: {'콜라': 500}, 2: {'사이다': 500}, 3: {'물': 800}, 4: {'파워에이드': 1000}}
# menu_name = list(menu.keys())

# 메뉴 출력 함수
def print_menu():
    print("🥤한석벤딩🥤")
    for k, v in menu.items():
        print(f'|{k}: {v}원', end='|')
    print()
print_menu()

# 메뉴 가격만 추출하기
def get_prices():
    prices = []
    for values2 in menu.values():
        for price in values2.values():
            prices.append(price)
    return prices

# get_prices() 함수 호출 및 결과 저장
prices = get_prices()

# prices 출력
print(prices)
print('최솟값',min(prices))

# 현금 투입 함수
balance = 0 #이 부분 어떻게 java의 private 변수처럼 외부 접근 방지할지 고민
def insert_cash():
    try :
        money = int(input("현금을 투입해주십시오(🚨정수만 입력하시오):"))
        balance = money
        print(f"투입하신 금액은 {balance}원 입니다.")  # 현재 잔액 표시
        if balance >= min(prices):
            print('메뉴고르기 함수 출력')  # 메뉴 선택 기능 호출
        else:
            print("투입 금액이 부족합니다.")
    except ValueError:
        print("현금만 투입해 주십시오(정수만 입력해 주십시오).")  # 입력 값이 정수가 아닌 경우 처리
insert_cash()