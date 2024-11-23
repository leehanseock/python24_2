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
        self.playCost = playCost
        self.inputMoney = 0

    def Operate(self):
        isContinue = True
        while isContinue:  # 금액이 투입된 경우
            isContinue = self.WouldUStart()
            if not isContinue: #WouldUStart에서 'n' 선택시
                self.inputMoney = 0
                print("게임을 종료합니다.")
                break
            self.InputMoney()
            self.ShowDolls()
            self.Game()
        print("프로그램이 종료됩니다.")

    def WouldUStart(self):
        while True:  # 올바른 입력이 들어올 때까지 반복
            print("-------------------------------------")
            self.ShowBalance()
            print(f"게임 한 판: {self.playCost}원")
            wouldU = input("게임을 플레이 하시겠습니까?(y/n): ").strip().lower()
            if wouldU == 'y':
                return True
            elif wouldU == 'n':
                return False
            else:
                print("잘못된 입력입니다. y 또는 n만 입력해주십시오.")

    def InputMoney(self):
        while True:
            try:
                if self.inputMoney > 0:
                    remaining_balance = self.inputMoney - self.playCost  # 남은 금액 계산
                    print(f"현재 남은 금액: {remaining_balance}원")
                    # 차액이 1000원 이상이면 0원을 입력해도 넘어가게 함
                    if remaining_balance >= 1000:
                        print("이전 게임에서 남은 금액으로 게임을 계속합니다.")
                        self.inputMoney -= self.playCost
                        break

                # 첫 번째 판 또는 이전 판에서 금액이 부족한 경우에는 입력받기
                money = int(input("투입할 금액을 입력하십시오:"))

                if money < 0:
                    print("음수 금액은 입력할 수 없습니다. 다시 입력해주세요.")
                    continue

                if self.inputMoney > 0 and remaining_balance < 1000:
                    money += self.inputMoney  # 이전에 투입한 금액을 더해줌

                if money >= self.playCost:
                    self.inputMoney = money
                    break
                elif money < self.playCost:
                    print(f"투입 금액이 {self.playCost}원 이상이어야만 합니다.")
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
        # 이미 뽑힌 인형선택시?
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
            del self.Dolls[selected_id]
        else:
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
