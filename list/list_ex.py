# 리스트 자료 구조

# cart = "라면" #변수
# print(cart)

"""
리스트(list) 
- 여러 개의 자료를 저장하는 자료 구조이다.
- 대괄호([])를 사용
- 요소에 접근할 때 위치(인덱스)를 사용(맨 앞: 0번, 맨 뒤: -1)
"""

'''
carts = ["라면", "우유", "토마토", "콩나물"]

# 리스트 객체 출력
print(carts)

# 특정 요소(element) 검색
print(carts[0])
print(carts[1])
print(carts[2])
print(carts[-1])
print(carts[-2])

# 요소 수정
carts[1] = "생수"
print(carts)
'''

# 정수형 자료를 저장할 리스트 생성
numbers = [10, 40, 30, 10, 30]

# 리스트 출력
print(numbers)
print(type(numbers)) # type() 자료형을 확인하는 함수

# 요소의 개수 - len
print("리스트의 크기:", len(numbers))

# 요소 검색(접근)
print(numbers[0]) # 10
print(numbers[1]) # 40
print(numbers[2]) # 30
print(numbers[4]) # 30
print(numbers[-1]) # 30

# 요소 수정
numbers[2] = 50

# 요소 삭제
del numbers[3]

print(numbers) # [10, 40, 50, 30]

# for 반복문 : for 반복변수 ~ in 리스트 구문
print(40 in numbers) # True
print(20 in numbers) # False
print(20 not in numbers) # True

# 전체 요소 출력
for num in numbers:
    print(num, end = ' ') # 요소를 옆으로 출력할 때
    # print(num) - 요소를 아래로 출력할 때

print() #줄바꿈

# 40보다 작은 요소(값) 출력
for num in numbers:
    if num < 40:
        print(num)

'''
num = 10, 10 < 40(True), 10 출력
num = 40, 40 < 40(False), 미출력
num = 50, 50 < 40(False), 미출력
num = 30, 30 < 40(True), 30 출력
'''

# 음식 분류하기 - 한식, 일식, 중식
foods = ["비빔밥", "짜장면", "초밥", "김치찌개"]
print(foods)

for food in foods:
    # 중식 리스트
    if food in ["짜장면", "짬뽕"]:
        print(f'{food}는(은) 중식입니다.')
    # 일식 리스트
    elif food in ["초밥", "우동"]:
        print(f'{food}는(은) 일식입니다.')
    # 한식 리스트
    else:
        print(f'{food}는(은) 한식입니다.')