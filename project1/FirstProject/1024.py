print("점수 정렬 프로그램")
list = []
for i in range(10):
    list.append(input(f"{i+1}번 학생의 점수를 입력해 주세요 : "))
# 버블 정렬
# length = len(list) - 1
# for j in range (length) :
#     for k in range(length-j):
#         if list[k] > list[k+1]:
#             list[k], list[k+1] = list[k+1], list[k]
# print(list)