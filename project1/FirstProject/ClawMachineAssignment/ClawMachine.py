from matplotlib import pyplot as plt
from project1.FirstProject.ClawMachineAssignment.Doll import Doll
from project1.FirstProject.ClawMachineAssignment.VM import VM

class ClawMachine(VM):
    def __init__(self, playCost, size):
        # 뽑기판 크기 지정
        self.size = size
        # 인형 객체 생성
        self.Dolls = {1: Doll("doraemon", size,1),
                      2: Doll("pikachu", size, 2),
                      3: Doll("kirby", size, 3),
                      4: Doll("dora", size, 4)
                      }
        self.playCount = 0
        self.playCost = playCost
        self.inputMoney = 0

    def Operate(self):
        isContinue = True
        while isContinue:  # 금액이 투입된 경우
            isContinue = self.WouldUStart()
            if not isContinue:  # WouldUStart에서 'n' 선택시
                print("게임을 종료합니다.")
                self.ReturnMoney()
                break
            self.InputMoney()  # 금액 입력
            if self.inputMoney < self.playCost:
                print(f"잔액이 부족합니다. {self.playCost}원 이상을 투입해야 합니다.")
                continue  # 금액이 부족하면 다시 시작

            self.ShowDolls()
            self.Game()

            # 게임이 끝난 후 게임 요금 차감
            self.inputMoney -= self.playCost
            print(f"남은 잔액: {self.inputMoney}원")

    def WouldUStart(self):
        while True:
            print("-------------------------------------")
            self.ShowBalance()
            print(f"게임 한 판: {self.playCost}원")
            wouldU = input("게임을 플레이 하시겠습니까?(y/n): ").strip().lower()
            if wouldU == 'y':
                return True
            elif wouldU == 'n':
                return False
            elif wouldU == '999':
                self.AdminMode()
                return True
            else:
                print("잘못된 입력입니다. y 또는 n만 입력해주십시오.")

    def InputMoney(self):
        while True:
            try:
                money = int(input("투입할 금액을 입력하십시오:"))
                if money >= 0:
                    self.inputMoney += money
                    break
                else:
                    print("0원 이상을 투입해주세요.")
            except ValueError:
                print("유효한 숫자를 입력해주십시오.")

    def ShowDolls(self):
        print("뽑을 수 있는 인형:")
        plt.figure(figsize=(6, 6))
        colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta']

        for idx, doll in self.Dolls.items():
            x, y = doll.getPosition()
            color = colors[idx % len(colors)]
            plt.scatter(x, y, label=f"{doll.getName()} position", color=color, s=100, marker='o')
        plt.xlim(0, 30)
        plt.ylim(0, 30)
        plt.grid(False)
        plt.title("Claw Machine")
        plt.legend()
        plt.show()
        for id, doll in self.Dolls.items():
            print(f"{id}: {doll.getName()}")

    def SelectDoll(self):
        try:
            selected_id = int(input("뽑을 인형의 번호를 입력하세요: "))
            if selected_id in self.Dolls:
                return self.Dolls[selected_id]
            else:
                print("존재하지 않는 번호입니다. 다시 입력해주세요.")
        except ValueError:
            print("유효한 번호를 입력해주세요.")
        return None  # invalid case returns None

    def Game(self):
        # 뽑을 인형 선택
        selected_doll = self.SelectDoll()

        if selected_doll is None:
            print("잘못된 선택입니다. 게임을 다시 시도해주세요.")
            return True  # 다시 게임을 진행하도록 False 대신 True를 반환

        selected_id = selected_doll.getId()
        doll_x, doll_y = selected_doll.getPosition()

        print("31x31 크기에서 인형 좌표를 맞춰보세요! (0~30)")
        while True:
            try:
                user_x = int(input("X 좌표 입력: "))
                user_y = int(input("Y 좌표 입력: "))
                if 0 <= user_x <= 30 and 0 <= user_y <= 30:
                    break
                else:
                    print("좌표는 0에서 30 사이여야 합니다.")
            except ValueError:
                print("유효한 숫자를 입력해주세요.")

        # 뽑기 성공 여부 판단
        success = (user_x == doll_x and user_y == doll_y)
        if success:
            print(f"축하합니다! {selected_doll.getName()} 뽑기 성공!")
            selected_doll.prize()
            self.playCount += 1
            del self.Dolls[selected_id]
        else:
            self.playCount += 1
            print(f"아쉽습니다. {selected_doll.getName()} 뽑기 실패!")

        # 결과 그래프
        plt.figure(figsize=(6, 6))
        for doll in self.Dolls.values():
            x, y = doll.getPosition()
            plt.scatter(x, y, label=f"{doll.getName()} position", color='blue', s=100, marker='o')
        plt.scatter(user_x, user_y, label="user input", color='red', s=100, marker='x')
        plt.xlim(0, 30)
        plt.ylim(0, 30)
        plt.grid(False)
        plt.title("Claw Machine")
        plt.legend()
        plt.show()

######################################################################################################
    # 관리자 모드 오버라이딩
    def AdminMode(self):
        admin_menu = {
            1: self.ShowSalesRecord,
            2: self.Reset
        }
        while True:
            # 관리자 메뉴를 출력합니다.
            print("\n=== 인형 뽑기 관리자 메뉴 ===")
            print("1: 판매 실적 확인")
            print("2: 시스템 초기화")
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

    # 총 판매수익
    def ShowSalesRecord(self):
        total_sales = self.playCount * self.playCost
        print(f"총 판매액: {total_sales}원")

    # 시스템 초기화 (인형 뽑기용)
    def Reset(self):
        self.playCount = 0
        # 인형 이름 변경
        for doll in self.Dolls.values():
            while True:
                name = input("적용할 인형 이름을 입력해주십시오: ").strip()
                # 빈 문자열인지 확인
                if name:
                    doll.changeName(name)
                    break
                else:
                    print("유효한 이름을 입력해주십시오.")

        #인형 위치 초기화
        for doll in self.Dolls.values():
            while True:
                try:
                    size = int(input("초기화시 적용할 뽑기판 사이즈를 입력해주십시오:"))
                    if size > 0:
                        doll.resetPosition(size)
                        break
                    else:
                        print("0을 초과하는 정수를 입력해주십시오.")
                except ValueError:
                    print("유효한 숫자를 입력해주십시오.")
        print("시스템이 초기화되었습니다.")
