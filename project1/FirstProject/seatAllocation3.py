import random
import matplotlib.pyplot as plt

# 1. 총 30개의 자리
total_seats = list(range(1, 31))  # 1부터 30까지의 자리를 리스트로 만듭니다.

# 2. 28명의 사람 (임의의 이름을 할당할 수 있습니다.)
people = [f"Person {i}" for i in range(1, 29)]  # Person 1부터 Person 28까지

# 3. 랜덤하게 자리를 배정하기 위해 자리를 셔플합니다.
random.shuffle(total_seats)

# 4. 빈 자리를 표시하기 위해 30개의 자리를 'Empty'로 초기화
seating_arrangement = ['Empty'] * 30

# 5. 28명의 사람을 첫 28개의 자리에 배치
for i, person in enumerate(people):
    seating_arrangement[total_seats[i] - 1] = person

# 6. 배정된 자리를 시각화 (3행 10열)
def visualize_seating(seating_arrangement):
    fig, ax = plt.subplots(figsize=(10, 6))

    # 3행 10열 형태로 시각화
    ax.set_xlim(0, 10)  # 가로 10열
    ax.set_ylim(0, 3)  # 세로 3행
    ax.set_xticks([])
    ax.set_yticks([])

    for i, seat in enumerate(seating_arrangement):
        row = i // 10  # 10열을 기준으로 행 계산
        col = i % 10  # 10열을 기준으로 열 계산
        ax.text(col + 0.5, 2.5 - row, seat, ha='center', va='center', fontsize=10,
                bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.3'))

    ax.set_title("Seating Arrangement (3 Rows x 10 Columns)")
    plt.show()

# 7. 자리 배치 시각화 실행
visualize_seating(seating_arrangement)