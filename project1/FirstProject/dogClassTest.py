from dog import Dog
# from {파일명} import {클래스명}

puppy = Dog()
print(f"이 강아지의 이름은 {puppy.name}입니다.")
puppy.name = "흰둥이"
print(f"이 강아지의 이름은 {puppy.name}입니다.")
puppy.Show()