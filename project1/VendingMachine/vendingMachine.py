from project1.VendingMachine.beverage import Beverage

class VendingMachine:
    def __init__(self):
        # self.__number = number
        # self.__total = total
        self.Menu  = {1: Beverage('콜라',900, 10),
                      2: Beverage("사이다", 1000, 10)}

        self.inputMoney = 0

        #음료 초기화
        # self.list = []
        # num = input("몇개의 음료를 판매할거니?")
        # for i in range(num):
        #     name = input("제품명: ")
        #     price = int(input("가격: "))
        #     count = int(input("재고량: "))
        #     item = Beverage(name, price, count)
        #     self.list.append(item)


    # def ManageStock(self, *belist):
    #     num = input("판매할 음료 갯수")
    #     while(i<num):
    #         i = 0
    #         name = input("제품명: ")
    #         price = input("가격: ")
    #         count = input("재고량: ")
    #         beverage[i+1] = beverage()

    def printMenu(self):
        for key, value in self.Menu.items():
            str = "{0}번 : {1}\t{2}원\t{3}".format(
                key,
                value.getName(),
                value.getPrice(),
                "" if value.getCount()>=0 else "품절"
            )
            print(str + "\n")
        # for j in list:
        #     print(f"[{j+1}] 제품명:{j.getName} / 가격:{j.getPrice} / 재고량:{j.getCount}")

    def InputMoney(self, money:int):
        self.inputMoney = money

    def ReturnMoney(self):
        tmp = self.inputMoney
        self.inputMoney = 0
        return tmp

    def PrintInputMoney(self):
        print("투입된 금액: "+str(self.inputMoney)+"원")
    #
    # # 음료 제공
    # def Give(self, k):
    #     print(f"선택하신 음료 {Beverage[k]}가 나옵니다. 음료수를 받아주세요.")
    #     Beverage[k].sale
    #
    # # 상품 선택
    # def Choose(self, choice):
    #     choice = input("주문할 음료 번호를 입력해주십시오: ")
    #     self.give(choice - 1)

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