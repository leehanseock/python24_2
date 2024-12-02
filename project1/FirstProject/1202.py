class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.__speed = 0  # private 속성

    def speedUp(self):
        self.__speed += 10
        print(f"현재 속도는 {self.__speed}입니다.")

    def speedDown(self):
        self.__speed -= 10
        print(f"현재 속도는 {self.__speed}입니다.")

    def stop(self):
        self.__speed = 0
        print(f"현재 속도는 {self.__speed}입니다.")

class SportsCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.top = False

    def TopOpen(self):
        self.top = True

    def TopClose(self):
        self.top = False

# 메인문 작성
if __name__ == '__main__':
    CarList = [
        SportsCar("마제라티", "파랑"),
        Car("프리우스", "베이지"),
        SportsCar("람보르기니", "노랑")
    ]

    i = 0
    while i < len(CarList):
        print(f"차 이름: {CarList[i].name}, 색상: {CarList[i].color}")
        i+=1
