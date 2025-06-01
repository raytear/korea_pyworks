# 모듈 만들기 - calculator.py
# 사칙연산 계산기
def add(x, y): #더하기
    return x + y

def sub(x, y): #빼기
    return x - y

def mul(x, y): #곱하기
    return x * y

def div(x, y): #나누기
    #분모가 0이 아니면 결과값 리턴
    if y !=0:
        return x / y
    else: #y == 0
        print("0으로 나눌 수 없습니다.")