# # 함수
# def CtoF(C):
#     return [c*1.8 + 32 for c in C]
# C = []
#
# F = CtoF(C)
# print(f'섭씨 : {C} [C]')
# print(f'화씨 : {F} [F]\n')

# def fun():
#     global a
#     a = 5
#     print(a)
# a = 100
#
# print(a)
# fun()
# print(a)

# def printVal(a, b, c):
#     s = f' a is {a}, b is {b} and c is {c}'
#     print(s)
# printVal(1, b =33, 10)

# def printVal(*a):
#     print(type(a))
#     for v in a :
#         print(v)
# printVal(1)
# printVal(1, 'abcd')
# printVal()
# print((1,2,3))

def isObesity(**kwd):
    h = kwd['h']  # 키를 cm에서 m로 변환
    w = kwd['w']
    print(f"키 : {kwd['h']}, 몸무게 : {kwd['w']}")
    BMI = w/h**2
    if BMI < 18.5 :
        result = f'BMI 지수는 {BMI :.2f}입니다. 당신은 마른 체형입니다.'
    elif BMI < 25.0:
        result = f'BMI 지수는 {BMI :.2f}입니다. 당신은 표준 체형입니다.'
    elif BMI < 30.0:
        result = f'BMI 지수는 {BMI :.2f}입니다. 당신은 비만 체형입니다.'
    else :
        result = f'BMI 지수는 {BMI :.2f}입니다. 당신은 고도 비만 체형입니다.'
    print(result)
isObesity(h = 1.73, w = 61)