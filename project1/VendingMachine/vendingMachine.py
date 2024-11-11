from project1.VendingMachine import beverage

class vendingMachine:
    def __init__(self, number, input, total):
        self.__number = number
        self.__input = 0
        self.__total = total

        # 음료 초기화
        list = []
        num = input("몇개의 음료를 판매할거니?")
        for i in range(num):
            name = input("제품명: ")
            price = input("가격: ")
            count = input("재고량: ")
            beverage[i] = beverage(name, price, count)
            list.append(beverage[i])

    def printMenu(self):
        for j in list:
            print(f"[{j+1}] 제품명:{j.getName} / 가격:{j.getPrice} / 재고량:{j.getCount}")

    def getMoney(self, input):
        self.__input += input

    # 음료 제공
    def give(self, k):
        print(f"선택하신 음료 {beverage[k]}가 나옵니다. 음료수를 받아주세요.")
        beverage[k].sale

    # 상품 선택
    def choose(self, choice):
        choice = input("주문할 음료 번호를 입력해주십시오: ")
        self.give(passedNum - 1)