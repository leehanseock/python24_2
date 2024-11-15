from project1.VendingMachine.vendingMachine import VendingMachine

if __name__ == '__main__':
    a = VendingMachine()
    isContinue = True

    while isContinue:
        a.printMenu()
        a.InputMoney()
        if isContinue:  # 금액이 투입된 경우
            isContinue = a.ChooseMenu() # ChooseMenu의 반환값을 통해 루프 여부 결정
            # 사용자가 메뉴에서 0을 입력한 경우에만 루프를 종료
            if not isContinue:
                break