# 리스트의 연산 - 개수, 총점, 평균, 최대값, 최소값
score = [70, 80, 50, 60, 90, 40] # 정수형 리스트
count = len(score)  # 개수를 저장할 변수
total = 0           # 총점을 저장할 변수
avg = 0.0           # 평균을 저장할 변수
max_val = 0         # 최대값
min_val = 0         # 최소값

# 총점 계산
# total = score[0] + score[1] + ... + score[5]
for i in score:
    total += i # total = total + i
    print(f'i={i}, total={total}')
'''
i=70, total = 0+70
i=80, total = 70+80
i=50, total = 150+50
'''

# 평균 계산 (평균 = 총점 / 개수)
avg = total / count

# 최대값 계산 - [70, 80, 50, 60, 90, 40]
max_val = score[0] # 최대값으로 설정함
for i in score:
    if i > max_val:
        max_val = i

'''
i=70, 70 > 70, max_val = 70, 변화 없음
i=80, 80 > 70, max_val = 80, 변경
i=50, 50 > 80, max_val = 80, 변화 없음
i=60, 60 > 80, max_val = 80, 변화 없음
i=90, 90 > 80, max_val = 90, 변경
i=40, 40 > 90, max_val = 90, 변화 없음
'''

# 최소값 계산
min_val = score[0] # 최소값으로 설정함
for i in score:
    if i < min_val:
        min_val = i

# 출력
print("개수:", count)
print("총점:", total)
print("평균:", avg)
print("최대값:", max_val)
print("최소값:", min_val)