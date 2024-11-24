import random

class Doll:
    def __init__(self, name, size, id):
        self.__name = name
        self.__x = random.randint(0, size-1)
        self.__y = random.randint(0, size - 1)
        self.__id = id

    def getName(self):
        return self.__name

    def getPosition(self):
        return self.__x, self.__y

    def getId(self):
        return self.__id

    # 사용자 뽑기 성공
    def prize(self):
        self.__capturedCount += 1

    # 관리자 모드
    def changeName(self, name):
        self.__name = name

    # 인형 좌표 초기화
    def resetPosition(self, board_size):
        self.__x = random.randint(0, board_size - 1)
        self.__y = random.randint(0, board_size - 1)