from pyasn1_modules.rfc2985 import counterSignature

class Beverage:
    def __init__(self, name, price, count):
        self.__name = name
        self.__price = price
        self.__count = count
        self.__salesCount = 0

    # 판매
    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getCount(self):
        return self.__count

    def sale(self):
        self.__count -= 1
        self.__salesCount += 1

    # 관리자
    def changePrice(self, price):
        self.__price = price

    def changeCount(self, count):
        self.__count = count

    def changeName(self, name):
        self.__name = name

    def getSalesCount(self):
        return self.__salesCount

    def resetSalesCount(self):
        self.__salesCount = 0