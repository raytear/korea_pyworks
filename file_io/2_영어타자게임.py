# 영어 타자 게임
import random
import time

# 단어장 파일 읽어오기
with open("./output/word.txt", "r") as f:
    word = f.read().split() #읽은 문자열을 공백문자로 분리

'''
# 단어 리스트 생성
word = ["sky", "earth", "sun", "moon", "flower", "tree",
        "mountain", "strawberry", "garlic", "potato"]
'''
n = 1  #문제 번호

print("[타자 게임] 준비되면 엔터")
input()   #엔터(공백 입력)

start = time.time()  #시작 시각
while n < 11:
    print("\n문제", n)
    question = random.choice(word)  #출제된 단어(랜덤)
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