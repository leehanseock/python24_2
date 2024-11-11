from project1.VendingMachine.beverage import Beverage

class VendingMachine:
    def __init__(self):
        self.Menu  = {1: Beverage('콜라',900, 10),
                      2: Beverage("사이다", 1000, 10)}
        self.inputMoney = 0

    def printMenu(self):
        for key, value in self.Menu.items():
            str = "{0}번 : {1}\t{2}원\t{3}".format(
                key,
                value.getName(),
                value.getPrice(),
                "" if value.getCount()>=0 else "품절"
            )
            print(str + "\n")

    def InputMoney(self, money:int):
        self.inputMoney = money

    def ReturnMoney(self):
        tmp = self.inputMoney
        self.inputMoney = 0
        return tmp

    def PrintInputMoney(self):
        print("투입된 금액: "+str(self.inputMoney)+"원")

    # 메뉴 선택
    def ChooseMenu(self):
        selectedMenu = int(input("메뉴 선택하시오:"))
        result = selectedMenu in self.Menu.keys()
        if result == True:
            if self.inputMoney< self.Menu[selectedMenu].getPrice():
                result=False
                print("금액이 부족합니다")
        return result, selectedMenu

    # 음료 제공
    def OutProduct(self, menu):
        self.Menu[menu].sale()
        print(f"{self.Menu[menu].getName()}가 나왔습니다.")
        self.inputMoney -= self.Menu[menu].getPrice()
        isCountinue = False

        for key, value in self.Menu.items():
            if self.inputMoney >= value.getPrice():
                isContinue = True
                break
        return isContinue