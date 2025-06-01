# 문자열
# 리스트

'''
seasons = ["봄", "여름", "가을", "겨울"]
print(seasons)
'''

"""
# 문자열을 분리하면 리스트로 변환 가능함 - split()
str = "봄 여름 가을 겨울"
# print(str) #["봄", "여름", "가을", "겨울"]
# print(str[0]) #봄

season = str.split(' ') #공백문자로 구분
print(season)

# 영어 타자 게임
import random
import time

# 문자열을 리스트로 변환
str = "sky earth sun moon flower tree " \
    "mountain strawberry garlic potato"

word = str.split(' ')
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

# os 모듈 - 디렉터리, 파일, 환경변수 등의 os 자원을 제어할 수 있게 해주는 모듈
'''
import os

# 디렉터리 이동
os.chdir('c:/pyworks')

# dir 명령 실행 - 목록(리스트) 보기
dir = os.popen('dir')
print(dir.read())

# 파일 목록을 리스트로 얻기
files = os.listdir('c:/pyworks')
# print(files)
print(files[1]) #basic

for file in files:
    print(file)
'''

'''
import 모듈이름
from 모듈(파일) 이름 import 하위모듈, 클래스, 메서드
from 상위모듈.하위모듈 import 클래스, 메서드

'''
"""
import datetime

# 현재 날짜와 시간
now = datetime.datetime.now()
print(now)

# 오늘 날짜
today = datetime.date.today()
print(today)
"""

from datetime import datetime, date

now = datetime.now()
print(now)

today = date.today()
print(today)