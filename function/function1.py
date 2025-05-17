# 함수 - 특정 기능(작업)을 수행하는 코드 블럭(작은 프로그램)
'''
    - def 키워드 사용
    - def 함수이름():
    - return이 있는 함수와 없는 함수
'''
# 함수 정의
def say_hello():
    print("안녕하세요~")

def say_hello2(name): #매개변수로 name을 전달
    print(name + "님 안녕하세요!")

"""
# 함수 호출
say_hello()

say_hello2("민준")
say_hello2("유빈")

# main() 함수 영역
# print("안녕하세요~")
"""

# return이 있는 함수
# 어떤 수를 제곱해주는 함수 정의
def square(x):
    return x * x

# 절대값을 계산하는 함수
# 양수를 입력하면 양수로 반환되고
# 음수를 입력하면 양수로 반환됨
def my_abs(n):
    if n < 0:
        return -n
    else:
        return n

def get_gugu(dan):
    for i in range(1, 10):
        # print(dan, 'x', i, '=', (dan * i))
        print(f"{dan} x {i} = {dan*i}")
# 함수 호출 시 매개변수로 숫자를 입력
val1 = square(8)

val2 = my_abs(-5)

# 구구단 호출
get_gugu(3)

print("val1 =", val1)
print("val2 =", val2)