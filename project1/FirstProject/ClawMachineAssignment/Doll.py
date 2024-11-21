class Doll:
    def __init__(self, name, count):
        self.__name = name
        self.__count = count
        self.__capturedCount = 0

    def getName(self):
        return self.__name

    def getCount(self):
        return self.__count

    # 사용자 뽑기 성공
    def prize(self):
        self.__count -= 1
        self.__capturedCount += 1

    # 관리자 모드
    def changeCount(self, count):
        self.__count = count

    def changeName(self, name):
        self.__name = name

    def getCapturedCount(self):
        return self.__capturedCount

    # 뽑힌 인형 개수 초기화
    def resetCapturedCount(self):
        self.__capturedCount = 0