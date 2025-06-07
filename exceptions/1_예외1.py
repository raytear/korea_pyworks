# 예외(Exception) 처리
# 여러가지 예외 발생 코드
# print('10' + '2') #Type Error(자료형 예외)

# calc1 = 4 + num * 3 #NameError(변수명 예외)

# calc2 =  4 * (10 / 0) #ZeroDivisionError(산술 예외)

import random

"""
while True:
    try:
        x = input("숫자를 입력하세요(q 종료): ")
        
        if x == 'q':
            print("프로그램 종료")
            break
        
        x = int(x) #문자를 정수로 변환
        print(x + 1)
    except ValueError:
        # 예외가 발생할 경우 실행될 코드(메시지 출력)
        print("유효한 숫자가 아닙니다. 다시 입력해주세요")
"""

# 숫자 추측 게임
com = random.randint(1, 30)
# print(com)

while True:
    try:
        x = input("맞혀보세요(입력: 1 ~ 30)")
        guess = int(x)  #입력받은 문자를 숫자형으로 변환
        #print(guess + 10)

        if guess < 0 or guess > 30:
            print("범위를 초과했어요. 다시 입력하세요")
        elif guess == com:
            print("정답!")
            break
        elif guess > com:
            print("너무 커요!")
        else:
            print("너무 작아요")
    except ValueError as e:
        # print(e)
        print("유효한 숫자가 아닙니다. 다시 입력하세요.")


print("게임을 종료합니다.")