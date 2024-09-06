# 과제 : 딕셔너리를 활용한 자판기 프로그램

# 중첩 딕셔너리를 사용한 메뉴 생성
menu = {'콜라': 500, '사이다': 500, '물': 800, '파워에이드': 1000, '밀키스': 750}

# 메뉴 이름(key값)만 추출
keys = menu.keys()
key_list = list(keys) # 키 값을 리스트로 변환

# 메뉴 가격(value값)만 추출하기
values = menu.values()
value_list = list(values)

# 메뉴 출력 함수
def print_menu():
    print("🥤한석벤딩🥤")
    for i in range(len(key_list)):
        print("|",f"{i+1}번 {key_list[i]} : {value_list[i]}원 ", end = "|")
    print()

# 현금 투입 함수
def insert_cash(money):
    print("🚨현금만 받습니다 (정수만 입력하세요.)")
    print(f"투입금액: {money}원")
    try :
        cash = int(input("현금을 투입해주십시오:"))
        money += cash
        if money >= 0: # 다음 단계로
            money = choose(money)
            return money
        elif money < 0 :
            print("현금이 0원 미만이 될 수는 없습니다.")
            return money
    except Exception :
        print("현금만 투입해 주십시오.") # 입력값이 정수가 아닌 경우 예외 처리
        return money

# 메뉴 선택 함수
def choose(inserted) :
    try :
        print("=====================================================")
        print(f"투입금액: {inserted}원")
        menu_num = int(input("구매하실 음료 번호를 메뉴에서 선택해 주십시오:"))
        if menu_num > 0 and menu_num <= len(key_list) : #입력한 값이 딕셔너리 키값 범위내에 있는지 필터링
            if inserted >= value_list[menu_num - 1]:
                print(f"{menu_num}번 {key_list[menu_num - 1]}을 선택하셨습니다. ")
                # 거스름돈 계산 & 음료 제공 함수 호출
                inserted = process_order(menu_num - 1, inserted)
                return inserted
            else:
                print("투입 금액이 부족합니다.")
                return inserted
        else :
            print("메뉴에 있는 번호를 선택해주셔야 합니다.")
            return inserted
    except Exception:
        print("메뉴에 있는 번호를 선택해주셔야 합니다.")
        return inserted

# 음료 제공 & 거스름돈 반환 함수
def process_order(num, inserted2):
    inserted2 -= value_list[num]
    print(f"{key_list[num]}(가/이) 나옵니다. 음료를 받아주세요.")
    print(f"잔액은 {inserted2}원 입니다.")
    return inserted2

# 자판기 함수
def vendingmachine():
    balance = 0
    while True:
        print_menu()
        balance = insert_cash(balance)
        print("=====================================================")
        try:
            answer = input("거래를 계속 하시겠습니까? y/n으로 답해주십시오: ").lower()
            if answer == 'y':
                continue
            elif answer == 'n':
                print(f"자판기를 종료합니다. 잔액 {balance}원을 받아 주십시오.") #잔액 반환
                break
            else:
                print("'y'나 'n'만 입력해 주십시오.")
                print("=====================================================")
        except Exception:
            print("'y'나 'n'만 입력해 주십시오.")
            print("=====================================================")
            continue

# 메인 문
if __name__ == "__main__":
    vendingmachine()