# 자리배정 생성기 만들기 과제
# 1. 30개의 자리에 28명이 랜덤하게 배치가 되는 자리배정 생성기 만들기
# 2. 각 자리에 누가 되었는지 보여주도록 시각화

# 30개의 좌석번호 생성
seatNums = [ nums for nums in range(30)]
print(seatNums)

# 좌석 배치 전의 학생이름(28명) 리스트 생성('before')
names = ['도라에몽', '퉁퉁이', '진구', '비실이', '이슬이',
            '짱구', '훈이', '맹구', '철수', '유리',
            '한지우', '웅', '로사', '로이', '나옹',
            '신태일', '매튜', '한소라', '장한솔', '이미나',
            '정석', '리키', '신나리', '샐리', '셜록스',
            '세인트', '이누야샤', '유가영']
print('학생 리스트 : ', names)
print('총 학생 수 : ',len(names))
print('빈 자리 수 : ', 30 - len(names))

# 학생이름 수가 30개 미만일 때 null 값 처리
if len(names) <= 30 :
    emptyNum = 30 - len(names)
    for e in range(emptyNum) :
        names.append("빈 좌석")

# 좌석번호와 학생이름 리스트 값을 각각 key 값과 value 값으로 갖는 딕셔너리 생성
dict = {s:n for s,n in zip(seatNums, names)}
# print(dict)

# 랜덤 라이브러리의 shuffle 메소드를 이용해 좌석번호 리스트를 섞고, 섞인 좌석번호를 key 값으로 할당하는 딕셔너리를 다시 생성해서 랜덤 좌석배정
# 랜덤 라이브러리 가져오기
import random as r
r.shuffle(seatNums)
shuffled_dict = {ss:n for ss, n in zip(seatNums, names)}
print(shuffled_dict)

# 최종 좌석배치표 생성
endList =["\t", " \t", "  \t", "   \t"]
print('▶️ 좌석배치 결과 ◀️')
print("-------------------------------------------------🟩교단🟩-----------------------------------------------------------")
for n in range(0, 30, 10):
    for i in range(n, n + 10):
        if len(shuffled_dict[i]) == 1:
            print(i+1, shuffled_dict[i], end=endList[3])
        elif len(shuffled_dict[i]) == 2:
            print(i+1, shuffled_dict[i], end=endList[2])
        elif len(shuffled_dict[i]) == 3:
            print(i+1, shuffled_dict[i], end=endList[1])
        else:
            print(i+1, shuffled_dict[i], end=endList[0])
    print()
    print("--------------------------------------------------------------------------------------------------------------------")