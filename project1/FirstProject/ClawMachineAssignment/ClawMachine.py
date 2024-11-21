from project1.FirstProject.ClawMachineAssignment.VM import VM
# 인형뽑기 기계 클래스
class ClawMachine(VM):
    # 기계 구동
    def Operate(self):
        isContinue = True
        while isContinue:  # 금액이 투입된 경우
            isContinue = self.PrintMenu()
            self.InputMoney()
            if isContinue:  # 금액이 투입된 경우
                isContinue = self.Game() #Game 메소드의 반환값을 통해 루프 여부 결정
                # 사용자가 메뉴에서 0을 입력한 경우에만 루프를 종료
                if not isContinue:
                    break
        print("프로그램이 종료됩니다.")

    # 메뉴 출력
    def PrintMenu(self):
        while True:  # 올바른 입력이 들어올 때까지 반복
            print("-------------------------------------")
            self.ShowBalance()
            print("게임 한 판: 1000원")
            wouldU = input("게임을 플레이 하시겠습니까?(y/n): ").strip().lower()  # 공백 제거 및 소문자로 변환
            if wouldU == 'y':
                return True
            elif wouldU == 'n':
                return False
            else: # y 또는 n 이외의 입력 받았을 경우
                print("잘못된 입력입니다. y 또는 n만 입력해주십시오.")

    # 게임
    def Game(self):
        print("test")