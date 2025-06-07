# 영어 타자 게임
import random
import time

# 영어 단어 메모장 만들기
with open("./output/word.txt", "w") as f:
    word = ["sky", "earth", "sun", "moon", "flower", "tree",
        "mountain", "strawberry", "garlic", "potato"]
    # 단어 1개씩 쓰기
    for i in word:
        f.write(i + ' ')

# 영어 단어 읽기
with open("./output/word.txt", "r") as f:
    # word = f.read()
    # print(word)

    data = f.read().split(' ') #문자열을 공백문자로 분리
    word = random.choice(data) #단어를 무작위로 선택
    print(word)
# "sky earth sun moon flower tree mountain strawberry garlic potato"
# split() : 문자열 -> 리스트 변환
# ['sky', 'earth', 'sun', 'moon', 'flower', 'tree', 'mountain', 'strawberry', 'garlic', 'potato']