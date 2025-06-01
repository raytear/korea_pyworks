# 함수의 매개변수
# 기본 매개변수(디폴트 매개변수)
# 함수 호출시 매개변수를 생략하면 기본값으로 실행(count=1)
def print_string(text, count=1):
    for i in range(count):
        print(text)

# print_string() 호출
print_string("apple", 4)
print_string("banana")

# 가변 매개변수
# 매개변수의 입력값이 정해지지 않고 변경해야 할 때 사용하는 함수
# 변수 앞에 '*'을 넣음
# 평균을 계산하는 함수 정의
def calc_avg(*number):
    total = 0 #합계
    for i in number: #number(iterable - 리스트, 튜플)
        total += i
    avg = total / len(number) #평균 = 합계 / 개수
    return avg

print(calc_avg(1, 2))  #1.5
print(calc_avg(1, 2, 3, 4))  #2.5

# 두 수를 더하는 함수 정의
'''
def add(x, y): #x=10, y=20
    return x + y #더한 값을 반환

# 제곱수 계산 함수
def square(n):
    return n * n

# add(매개변수) 호출
val=add(10, 20)
print("더하기:", val)

# square() 호출
val2 = square(4)
print(f"제곱수: {val2}")
'''

# 실습 문제
def my_func(x, y):
    if x == y:
        return x + y
    else: # x != y
        return x - y

result1 = my_func(8, 8)
print("result1 = ", result1) #16

result2 = my_func(8, 9)
print("result2 = ", result2) #-1