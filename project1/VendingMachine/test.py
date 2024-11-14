from project1.VendingMachine.vendingMachine import VendingMachine

if __name__ == '__main__':
    a = VendingMachine()

    a.printMenu()
    a.InputMoney(900)
    a.PrintInputMoney()

    isCountinue= False
    while(isCountinue==False):
        isCountinue, menu = a.ChooseMenu()
    print("{0} / {1}".format(isCountinue, menu))

    a.OutProduct(menu)
    a.ReturnMoney()