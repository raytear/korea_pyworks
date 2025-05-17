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

"""
i=70, 70 > 70, max_val = 70, 변화 없음
i=80, 80 > 70, max_val = 80, 변경
i=50, 50 > 80, max_val = 80, 변화 없음
i=60, 60 > 80, max_val = 80, 변화 없음
i=90, 90 > 80, max_val = 90, 변경
i=40, 40 > 90, max_val = 90, 변화 없음
"""

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

# 리스트의 내포 - 결과가 리스트로 반환
# [표현식 for 요소 in 리스트]
arr1 = [1, 2, 3, 4, 5]
arr2 = [] # 3의 배수 저장
arr3 = [] # 3의 배수 저장(리스트 내포)
arr4 = [] # 홀수만 저장

# arr1의 요소를 3의 배수로 저장
# append() 함수를 사용해야 함
# arr2.append(1)
# print(arr2[0])
# 일반 for문 사용

for i in arr1:
    arr2.append(3 * i)
print("arr2 =", arr2)

# 리스트 내포
arr3 = [3 * i for i in arr1]
print("arr3 =", arr3)

arr4 = [i for i in arr1 if i % 2 == 1]
print("arr4 =", arr4)

# 리스트의 정렬 - 오름차순
# 정렬 알고리즘
# 버블 정렬 - 인접한 두 요소를 비교하여 큰 값을 오른쪽으로 이동
n_list = [60, 40, 90, 50, 80]
n = len(n_list)
print("리스트의 크기:", n)

# 콜론(블럭 기능) → 다음줄(들여쓰기, 4칸)
for i in range(0, n):
    for j in range(0, n - 1):
        if n_list[j] > n_list[j + 1]:
            # 교환 방법 1
            # temp = n_list[j]
            # n_list[j] = n_list[j + 1]
            # n_list[j + 1] = temp

            # 교환 방법 2
            n_list[j], n_list[j+1] = n_list[j+1], n_list[j]

'''
    i=0(1행), j=0, 60 > 40 교환 발생 40, 60, 90, 50, 80
              j=1, 60 > 90 유지     40, 60, 90, 50, 80
              j=2, 90 > 50 교환     40, 60, 50, 90, 80
              j=3, 90 > 80 교환     40, 60, 50, 80, 90
    i=1(2행), j=0, 40 > 60 유지     40, 60, 50, 80, 90
              j=1, 60 > 50 교환     40, 50, 60, 80, 90
              j=2, 60 > 80 유지     40, 60, 50, 80, 90
              j=3, 80 > 90 유지     40, 60, 50, 80, 90 [저장]
    i=2(3행)  교환 없음
    i=3(4행)  교환 없음
    i=4(5행)  교환 없음
'''
print("*** 오름차순 정렬 ***")
for i in n_list:
    print(i, end=' ')

print()

# n_list.sort() #라이브러리 함수
# print(n_list)

# 별찍기 - 직각삼각형 모양(5행 5열)
for i in range(1, 6): #range() 종료는 '종료-1'
    for j in range(1, i + 1):
        print("*", end='')
    print()
'''
*
**
***
****
*****

i=행, j=열

i=1, j=1, *
i=2, j=1, *
     j=2, **
i=3, j=1, *
     j=2, **
     j=3, ***
'''

"""
- 두 수를 비교 후 교환(자리바꿈) 발생
- 중첩 for
"""

x = 1
y = 2
print('x =', x, ", y =", y)

# 방법 1

'''
교환을 위한 임시 변수 - temp

temp = x
x = y
y = temp
'''

# 방법 2
x, y = y, x
print('x =', x, ", y =", y)
