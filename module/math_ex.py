# 수학 관련 함수(메서드)
# 내림, 올림, 제곱근 함수
import math

# 올림
print(math.ceil(2.54))      #3

# 내림(버림)
print(math.floor(10.42))    #10

# 제곱근 - 실수로 반환
print(math.sqrt(25))
print(math.sqrt(2))

# 원주율(파이) - math.pi(함수가 아닌 속성)
print(math.pi)

# 원의 넓이 = math.pi * 반지름 * 반지름
# 실수 - float
radius = 4 #반지름
area = math.pi * radius * radius
print(f'원의 넓이: {area:.3f}')