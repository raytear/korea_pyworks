'''
재귀 호출 - 재귀 함수
 - 어떤 함수 안에서 자기 자신을 부르는 것을 말한다.
 - 재귀 호출은 무한반복하므로 종료 조건이 필요함
 - if문 사용
'''
# 재귀 함수 이용
def sos(n):
    print("Help me!")
    n = n - 1
    if n > 0:  #종료 조건
        sos(n)

'''
방법 1
def sos(n):
    for i in range(0, n):
        print("Help me!")
'''

'''
  n=4, sos(4), "Help me!"  
       sos(3), "Help me!" 
       sos(2), "Help me!" 
       sos(1), "Help me!" 반복 종료
'''
# sos()를 호출
sos(4)

# 1부터 5까지 곱하기
# 1x2x3x4x5  -> 5!
# 일반 함수로 정의
def get_gob(n):
    gob = 1  #초기값
    for i in range(1, n + 1):
        gob *= i #gob = gob * i
    return gob

# 재귀 함수로 정의
def facto(n):
    if n <= 1: #종료조건
        return 1  
    else:  #루프 조건
        return n * facto(n - 1)

'''
    n=5, facto(5), 5*facto(4)
         facto(4), 5*4*facto(3)
         facto(3), 5*4*3*facto(2)
         facto(2), 5*4*3*2*facto(1)
         facto(1), 5*4*3*2*1*facto(0) 반복종료
'''
print(get_gob(5)) #120

print(facto(5))  #120
print(facto(0))  #1
print(facto(1))  #1