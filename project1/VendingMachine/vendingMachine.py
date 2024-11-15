from project1.VendingMachine.beverage import Beverage

class VendingMachine:
    def __init__(self):
        self.Menu  = {1: Beverage('콜라',900, 2),
                      2: Beverage("사이다", 1000, 2),
                      3: Beverage("아이스티", 1000, 2),
                      4: Beverage("물", 750, 1)}
        self.inputMoney = 0

    def printMenu(self):
        for key, value in self.Menu.items():
            str = "{0}번 : {1}\t{2}원\t{3}".format(
                key,
                value.getName(),
                value.getPrice(),
                "" if value.getCount()>=0 else "품절"
            )
            print(str)
        print("(구매를 종료하시려면 0을 입력해주세요.)")

    def InputMoney(self):
        try:
            money = int(input("투입할 금액을 입력하십시오:"))
            self.inputMoney = money
        except ValueError:
            print("유효한 숫자를 입력해주십시오.")
            return True
        if (money==0):
            return False
        else :
            self.ChooseMenu()
            return True

    def ReturnMoney(self):
        tmp = self.inputMoney
        self.inputMoney = 0
        print(f"잔액 {tmp}원을 받아주십시오.")
        print("=====================================")
        return tmp

    def PrintInputMoney(self):
        print("투입된 금액: "+str(self.inputMoney)+"원")

    # 메뉴 선택
    def ChooseMenu(self):
        selectedMenu = int(input("메뉴 선택하시오:"))
        result = selectedMenu in self.Menu.keys()
        if selectedMenu == 999:
            self.AdminMode()
        elif result == True:
            if self.inputMoney< self.Menu[selectedMenu].getPrice():
                result=False
                print("금액이 부족합니다")
            elif self.Menu[selectedMenu].getCount()>0:
                self.OutProduct(selectedMenu)
            else :
                print("재고가 부족합니다.")

    # 음료 제공
    def OutProduct(self, menu):
        self.Menu[menu].sale()
        print(f"{self.Menu[menu].getName()}가(이) 나왔습니다.")
        self.inputMoney -= self.Menu[menu].getPrice()
        isContinue = False

        for key, value in self.Menu.items():
            if self.inputMoney >= value.getPrice():
                isContinue = True
                break
        return isContinue

    ########################################################
    # 관리자 모드
    def AdminMode(self):
        admin_menu = {
            1: self.SettingBeverage,
            2: self.showSalesRecord,
            3: self.reset
        }

        while True:
            # 관리자 메뉴를 출력합니다.
            print("\n=== 관리자 메뉴 ===")
            for key, value in self.Menu.items():
                str = "{0}번 : {1}\t{2}원\t판매량:{3}개\t재고량:{4}개".format(
                    key,
                    value.getName(),
                    value.getPrice(),
                    value.getSalesCount(),
                    value.getCount()
                )
                print(str)
            print("1: 음료 설정 변경")
            print("2: 판매 실적 확인")
            print("3: 시스템 초기화")
            print("0: 종료")
            try:
                choice = int(input("원하는 번호를 입력하십시오: "))
            except ValueError:
                print("유효한 숫자를 입력해주십시오.")
                continue
            if choice == 0:
                print("관리자 모드를 종료합니다.")
                print("=====================================")
                break
            elif choice in admin_menu:
                admin_menu[choice]()  # 해당 번호의 함수 호출
            else:
                print("잘못된 입력입니다. 다시 시도하십시오.")

    def SettingBeverage(self):
        for key, value in self.Menu.items():
            str = "{0}번 : {1}\t{2}원\t재고량:{3}개".format(
                key,
                value.getName(),
                value.getPrice(),
                value.getCount()
            )
            print(str)
        toChange = int(input("변경하려는 음료 번호를 입력하십시오:"))
        result2 = toChange in self.Menu.keys()
        if result2 == True:
            print("음료 세팅 : 1. 음료 변경 2. 음료 가격 변경 3. 음료 재고 변경")
            settingMenu = int(input("메뉴 번호: "))
            if settingMenu == 1 :
                changedName = input("변경하려는 음료명을 입력하십시오:")
                self.Menu[toChange].changeName(changedName)
            elif settingMenu == 2 :
                changedPrice = int(input("변경하려는 음료가격을 입력하십시오:"))
                self.Menu[toChange].changePrice(changedPrice)
            elif settingMenu == 3 :
                changedStockNum = int(input("변경하려는 재고량을 입력하십시오:"))
                self.Menu[toChange].changeCount(changedStockNum)
            else :
                print("관리자 메뉴에 있는 번호를 입력해주십시오.")

    # 판매실적확인
    def showSalesRecord(self):
        sum = 0
        for key, value in self.Menu.items():
            str = "{0}번 : {1} {2}개×{3}원 = {4}원".format(
                key,
                value.getName(),
                value.getSalesCount(),
                value.getPrice(),
                value.getSalesCount()*value.getPrice()
            )
            sum += value.getSalesCount() * value.getPrice()
            print(str)
        print("-------------------------------------")
        print(f"총 판매액: {sum}원")

    # 초기화
    def reset(self):
        for key, value in self.Menu.items():
            value.changeCount(0)
    print("시스템이 초기화되었습니다.")
