class Dog :
    def __init__(self): # 생성자 (아무것도 전달받지 않은 상태)
        self.name = "바둑이"
    # 멤버 메소드 정의
    def Show(self):
        print(self.name)