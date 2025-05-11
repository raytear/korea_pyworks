# 중첩 for문
for i in range(1, 6):
    for j in range(1, 6):
        print('가', end='')
    print() #행 바꿈 

"""
i=1(1행) j=1, 가
         j=2, 가가
         j=3, 가가가
         j=4, 가가가가
         j=5, 가가가가가
i=2(2행) j=1, 가
         j=2, 가가
         j=3, 가가가
         j=4, 가가가가
         j=5, 가가가가가
         
"""
print()
for i in range(5): #초기값에 0이 생략됨
    for j in range(5):
        print('가', end='')
    print() #행 바꿈

# 전체 구구단(2 ~ 9) 출력
# 9행 1열 출력
for i in range(2, 10):
    print('[', i, '단 ]')
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()    

# 1행 9열 출력
for i in range(1, 10):
    for j in range(2, 10): #단
        print(f"{j} x {i} = {j * i}", end=' | ')
    print()
