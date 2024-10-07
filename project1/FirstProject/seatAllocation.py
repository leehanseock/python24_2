# 자리배정 생성기 만들기 과제
# 1. 30개의 자리에 28명이 랜덤하게 배치가 되는 자리배정 생성기 만들기
# 2. 각 자리에 누가 되었는지 보여주도록 시각화

# 넘파이 라이브러리 임포트
import numpy as np

# 좌석 배치 전의 학생이름(28명) 리스트 생성('before')
before = ['도라에몽', '퉁퉁이', '진구', '비실이', '이슬이',
            '짱구', '훈이', '맹구', '철수', '유리',
            '한지우', '웅', '로사', '로이', '나옹',
            '신태일', '매튜', '한소라', '장한솔', '이미나',
            '정석', '리키', '신나리', '샐리', '셜록스',
            '세인트', '이누야샤', '유가영']
print('학생 리스트 : ', before)
print('총 학생 수 : ',len(before))
print('빈 자리 수 : ', 30 - len(before))

# 학생이름 수가 30개 미만일 때 null 값 처리
if len(before) <= 30 :
    emptyNum = 30 - len(before)
    for e in range(emptyNum) :
        before.append("빈 좌석")

# 파이썬 리스트를 넘파이 배열로 변환하기
before_arr = np.array(before)
# print(before_arr)

# 30개의 좌석번호 생성 후 랜덤하게 섞기
seatNums = np.arange(30)
np.random.shuffle(seatNums)
# print(seatNums)

# 랜덤하게 섞인 좌석번호를 인덱스 번호로 해서 좌석배치 순으로 학생이름 출력('after')
after = before_arr[seatNums[:30]]
# print(after)

# 최종 좌석배치표 생성
endList =["\t", " \t", "  \t", "   \t"]
print('▶️ 좌석배치 결과 ◀️')
print("-------------------------------------------------🟩교단🟩-----------------------------------------------------------")
for n in range(0, 30, 10):
    for i in range(n, n + 10):
        if len(after[i]) == 1:
            print(i+1, after[i], end=endList[3])
        elif len(after[i]) == 2:
            print(i+1, after[i], end=endList[2])
        elif len(after[i]) == 3:
            print(i+1, after[i], end=endList[1])
        else:
            print(i+1, after[i], end=endList[0])
    print()
    print("--------------------------------------------------------------------------------------------------------------------")