# random 모듈
import random

"""
# 0.0 <= random.random() < 1
print(random.random())

# random.randint(a, b) : a부터 b까지 정수 범위
print(random.randint(1, 10)) # 1 ~ 10 중 무작위수(난수) 발생

# 주사위 눈
dice = random.randint(1, 6) #1 ~ 6
print(dice)

# 주사위 10번 던지기
for i in range(10): #range(0, 10)
    dice = random.randint(1, 6)
    print(dice)

# 동전 던지기
coin = random.randint(1, 2)
if(coin == 1):
    print("앞면")
else:
    print("뒷면")
"""

'''
# 숫자 추측 게임
com = random.randint(1, 30)
print(com)

while True:
    x = input("맞혀보세요(입력: 1 ~ 30)")
    guess = int(x) #입력받은 문자를 숫자형으로 변환
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

print("게임을 종료합니다.")
'''

# 로또 복권 추첨 - 45개의 숫자 중에 6개 추출
lotto = [] #당첨 번호를 저장할 리스트 생성

"""
for i in range(6):
    num = random.randint(1, 45) #당첨 번호
    if num not in lotto: #리스트에 추첨되지 않은 번호
        lotto.append(num) #번호 추가
"""
        
while len(lotto) < 6:
    num = random.randint(1, 45) #당첨 번호
    if num not in lotto: #리스트에 추첨되지 않은 번호
        lotto.append(num)

print(lotto)

# 리스트에서 요소를 무작위로 추출
# random.choice

carts = ["라면", "계란", "우유", "콩나물"]

print(random.choice(carts))

# 영어 타자 게임
