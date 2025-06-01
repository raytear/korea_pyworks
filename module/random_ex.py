# random 모듈
import random

"""
# 0.0 <= random.random() < 1
# print(random.random())

# random.randint(a, b) : a부터 b까지 정수 범위
# print(random.randint(1, 10))  # 1 ~ 10중 무작위수(난수) 발생

# 주사위 눈
dice = random.randint(1, 6) # 1 ~ 6
# print(dice)

# 주사위 10번 던지기
for i in range(10): #range(0, 10)
    dice = random.randint(1, 6)
    print(dice)

# 동전 던지기
coin = random.randint(1, 2)
print(coin)
if(coin == 1):
    print("앞면")
else:
    print("뒷면")
"""

'''
# 숫자 추측 게임
com = random.randint(1, 30)
# print(com)

while True:
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

print("게임을 종료합니다.")
'''

# 로또 복권 추첨 - 45개의 숫자중에 6개 추출
lotto = []  # 당첨 번호를 저장할 리스트 생성

"""
for i in range(6):
    num = random.randint(1, 45) #당첨 번호
    if num not in lotto:  # 리스트에 추첨되지 않은 번호
        lotto.append(num) # 번호 추가
# for문은 중복이 발생해도 카운트가 되므로 4, 5개가 될 수 있음
# [10, 30, 22, 12, 42] 만약 2번 인덱스에서 10이 중복되면 삭제됨


# 반드시 6개 저장하고 반복 종료
while len(lotto) < 6:
    num = random.randint(1, 45) #당첨 번호
    if num not in lotto:  # 리스트에 추첨되지 않은 번호
        lotto.append(num)
# len(lotto) - 리스트의 개수 0 ~ 5번까지(6개까지) true
# [10, 30, 3, 22, 12, 42] 만약 2번 인덱스에서 10이 중복되면 삭제되고 또 추첨

print(lotto)
"""

'''
# 리스트에서 요소를 무작위로 추출
# random.choice

carts = ["라면", "계란", "우유", "콩나물"]

print(random.choice(carts))
'''

# 영어 타자 게임
import random
import time

# 단어 리스트 생성
word = ["sky", "earth", "sun", "moon", "flower", "tree",
        "mountain", "strawberry", "garlic", "potato"]
n = 1  #문제 번호

print("[타자 게임] 준비되면 엔터")
input()   #엔터(공백 입력)

start = time.time()  #시작 시각
while n < 11:
    print("\n문제", n)
    question = random.choice(word)  #출제된 단어
    print(question)

    you = input()  #사용자 입력(대기 상태)
    #입력후 문제와 단어가 일치하는지 여부 작성
    if you == question:
        print("통과!")
        n += 1 #n = n + 1 #다음 문제 증가
    else:
        print("오타! 다시 도전!")
'''
    n=1, 1번 출제
    n=10, 10번 문제 출제되고
    n=11, 반복 종료
'''
end = time.time()  #종료 시각
et = end - start   #게임 소요 시각
print(f"게임 소요 시간: {et:.2f}초")

"""
# 인덱싱과 슬라이싱
print(word[0]) #sky
print(word[4]) #flower
print(word[-1]) #potato
print(word[-2]) #garlic
print(word[0:4]) #['sky', 'earth', 'sun', 'moon']
print(word[:4]) #['sky', 'earth', 'sun', 'moon']
print(word[4:]) #['flower', 'tree', 'mountain', 'strawberry', 'garlic', 'potato']

# 무작위로(랜덤하게) 단어 추출
str = random.choice(word)
print(str)
"""