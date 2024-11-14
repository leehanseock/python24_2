from project1.VendingMachine.vendingMachine import VendingMachine

if __name__ == '__main__':
    a = VendingMachine()
    isCountinue = True

    while isCountinue:
        a.printMenu()
        isCountinue = a.InputMoney()  # InputMoney의 반환값으로 루프 지속 여부 결정
        a.PrintInputMoney()
        a.ReturnMoney()