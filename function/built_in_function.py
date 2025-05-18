# 내장 함수
a = [1, 2, 3, 4]

# 합계
print(sum(a))           #10

# 최대값, 최소값
print(max(a))           #4
print(min(a))           #1

# 반올림
print(round(2.74))      #3
print(round(2.14))      #2

# 소수 자리수
x = 702.351
print(round(x, 2))      #702.35
print(round(x, 1))      #702.4
print(round(x))         #정수 702

# 내림(floor()), 올림(ceil()) → import math 사용 필요
import math #수학 모듈을 가져옴
print(math.ceil(2.15))  #3
print(math.floor(2.74)) #2

# 문자열 표현식을 숫자로 변환
print('1 + 2')          #1 + 2
print(eval('1 + 2'))    #3

# 문자열을 리스트로 변환
print(list('korea'))    #['k', 'o', 'r', 'e', 'a']

# 절대값 함수 정의
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x
    
# 거듭 제곱 함수 정의
def my_pow(x, y):
    gob = 1
    for i in range(0, y):
        gob = gob * x
    return gob

'''
    x=2(밑), y=3(지수)
    i=0, gob = 1 * 2
    i=1, gob = 2 * 2
    i=2, gob = 4 * 2
    i=3, 반복 종료
'''

# 절대값
print(abs(-3))          #3
print(my_abs(-3))       #3

# 거듭제곱 - 2의 3승
print(pow(2, 3))        #8 - pow(밑, 지수)
print(pow(3, 3))        #27
print(my_pow(2, 3))     #8

'''
# 1 ~ 4까지 곱하기
# 1 x 2 x 3 x 4 = 24 → 4!
gob = 1
for i in range(1, 5):
    gob = gob * i
    print('i =', i, ', gob =', gob)

print("곱한 값:", gob)
'''