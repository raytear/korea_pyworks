# 구구단을 단보다 곱하는 수가 작거나 같은 경우까지 출력하는 프로그램

for i in range(2, 10):
    print()
    print('[', i, '단]')    
    for j in range(1, 10):
        if i < j:
            break
        print(f"{i} * {j} = {i*j}")
        # if i >= j:
            # print(f"{i} * {j} = {i*j}")

'''
i=2, j=1, 2 < 1, 2x1=2
     j=2, 2 < 2, 2x2=4
     j=3, 2 < 3(true) break 실행(빠져나옴)
'''