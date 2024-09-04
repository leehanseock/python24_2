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

# 현금 투입 함수
def insert_cash(money):
    print(f"현재 잔액 : {m}원", money) # 최초잔액 표시
    get_prices()

    # if money >= min(prices):
    #     print("ok")
    #     # 메뉴 고르기 함수 출력
    # else money < min(prices):
