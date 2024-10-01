# 자리배정 생성기 만들기 과제
# 1. 30개의 자리에 28명이 랜덤하게 배치가 되는 자리배정 생성기 만들기
# 2. 각 자리에 누가 되었는지 보여주도록 시각화

# 넘파이 라이브러리 임포트
import numpy as np

# 좌석 배치 전의 학생이름 리스트 생성('before')
before = ['도라에몽', '퉁퉁이', '진구', '비실이', '이슬이',
            '짱구', '훈이', '맹구', '철수', '유리',
            '한지우', '웅', '로사', '로이', '나옹',
            '신태일', '매튜', '한소라', '장한솔', '이미나',
            '정석', '리키', '신나리', '샐리', '셜록스',
            '세인트', '이누야샤', '유가영', '금강', '싯포']

# 파이썬 리스트를 넘파이 배열로 변환하기
before_arr = np.array(before)
print(before_arr)

# 30개의 좌석번호 생성 후 랜덤하게 섞기
seatNums = np.arange(30)
np.random.shuffle(seatNums)
print(seatNums)

# 랜덤하게 섞인 좌석번호를 인덱스 번호로 해서 좌석배치 순으로 학생이름 출력('after')
after = before_arr[seatNums[:30]]
print(after)

# 최종 좌석배치표 생성
endList =["\t", " \t", "  \t", "   \t"]
#
# for i in range(10):
#     if len(after[i]) == 1:
#         print(after[i], end = endList[3])
#     elif len(after[i])==2 :
#         print(after[i], end = endList[2])
#     elif len(after[i])==3:
#         print(after[i], end=endList[1])
#     else :
#         print(after[i], end = endList[0])
# print()
# for j in range(10, 20):
#     if len(after[j]) == 1:
#         print(after[j], end=endList[3])
#     elif len(after[j]) == 2:
#         print(after[j], end=endList[2])
#     elif len(after[j]) == 3:
#         print(after[j], end=endList[1])
#     else:
#         print(after[j], end=endList[0])
# print()
# for k in range(20, 30):
#     if len(after[k]) == 1:
#         print(after[k], end=endList[3])
#     elif len(after[k]) == 2:
#         print(after[k], end=endList[2])
#     elif len(after[k]) == 3:
#         print(after[k], end=endList[1])
#     else:
#         print(after[k], end=endList[0])
# print()
#
for start in range(0, 30, 10):  # 0부터 30까지 10단위로 끊음 (0~9, 10~19, 20~29)
    for i in range(start, start + 10):
        if len(after[i]) == 1:
            print(after[i], end=endList[3])
        elif len(after[i]) == 2:
            print(after[i], end=endList[2])
        elif len(after[i]) == 3:
            print(after[i], end=endList[1])
        else:
            print(after[i], end=endList[0])
    print()  # 각 구간의 10개 출력 후 줄바꿈
