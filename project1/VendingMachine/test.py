from project1.VendingMachine.vendingMachine import VendingMachine

if __name__ == '__main__':
    a = VendingMachine()
    a.printMenu()
    a.InputMoney(900)
    a.PrintInputMoney()

    isOk= False
    while(isOk==False):
        isOk, menu = a.ChooseMenu()
    print("{0} / {1}".format(isOk, menu))

    a.OutProduct(menu)
    a.ReturnMoney()