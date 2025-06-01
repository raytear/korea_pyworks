# 문자열은 특별한 1차원 리스트이다.

alpha = ['a', 'b', 'c', 'd']

"""
# 인덱싱
print(alpha[2])

# 슬라이싱(범위로 검색 - ':' 사용)
print(alpha[0:3])  # 종료값 = 종료인덱스-1
print(alpha[0:-1])
print(alpha[0:])   # 마지막 값까지 추출
print(alpha[:])    # 마지막 값까지 추출

# 문자열은 특별한 1차원 리스트이다.
f = "apple"
print(f[0])
print(f[2])
print(f[-1])
print(f[:])

s = "20250510Rainy"
# 연도 추출
year = s[:4] #끝 → 끝 인덱스-1
print(year)

# 월일 추출
day = s[4:8]
print(day)

# 날씨 추출
weather = s[8:]
print(weather)

print(year + '.' + day + '.' + weather)
"""

'''
# 문자열 함수(메서드)
fruit = "banana,grape,kiwi"
print(fruit)
print(type(fruit)) #<class 'str'>

# split(구분기호) - 문자열을 리스트로 변환해줌
fruit = fruit.split(',')
print(fruit) #['banana', 'grape', 'kiwi']
print(type(fruit)) #<class 'list'>

# 인덱싱과 슬라이싱
print(fruit[0])
print(fruit[2])
print(fruit[-1])

print(fruit[0:2]) #['banana', 'grape']
print(fruit[0:3]) #['banana', 'grape', 'kiwi']
print(fruit[:])   #['banana', 'grape', 'kiwi']

# replace("변경 전 문자", "변경 후 문자")
s = "Hello, World"
s = s.replace("World", "Korea") #replace된 값을 s에 다시 저장하지 않으면 출력 안됨
print(s)

# find(문자) - 문자의 인덱스(위치) 번호 반환
s1 = "smile"
print(s1.find('m')) #1번 인덱스
print(s1.find('k')) #-1 반환

# 실습(부산 → 서울로 변경)
s2 = "대한민국의 수도는 부산이다."
s2 = s2.replace("부산", "서울") 
print(s2)
'''

# 백신 접종자 분류하기
# 접종 대상 - 20세 ~ 65세, 비대상 - "하반기 일정 확인"
'''
백신 접종 대상인 경우 - 출생연도 끝자리
1 or 6 - 월요일
2 or 7 - 화요일
3 or 8 - 수요일
4 or 9 - 목요일
5 or 0 - 금요일

'''

"""
birth_year = input("출생연도 입력: ") #출생연도 → 문자열
age = 2022 - int(birth_year) + 1

if age >= 20 and age <= 65:
    print("백신 접종 대상")
    if birth_year[-1] == '1' or birth_year[-1] == '6':
        print("월요일 접종")
    elif birth_year[-1] == '2' or birth_year[-1] == '7':
        print("화요일 접종")
    elif birth_year[-1] == '3' or birth_year[-1] == '8':
        print("수요일 접종")
    elif birth_year[-1] == '4' or birth_year[-1] == '9':
        print("목요일 접종")
    elif birth_year[-1] == '5' or birth_year[-1] == '0':
        print("금요일 접종")
else:
    print("하반기 일정")
"""
'''
# 실습 - 문자열 처리
x = input("Happy Birthday!!를 입력하세요: ")
x = x.capitalize() #문자열의 맨 앞 글자를 대문자로 변경해줌
print(x) #Happy birthday!!
y = x.split() #공백문자로 구분 - (' ') or () 사용
print(y) #['Happy', 'birthday!!']
'''

# 리스트
# 문자열 → 1차원 리스트

car = "나는 전기차를 구매했어요"

# 인덱싱과 슬라이싱
print(car[0]) #나
print(car[3]) #전
print(car[3:6]) #전기차

# 전기차를 수소차로 변경
car = car.replace("전기차", "수소차")
print(car)

# 찾기 함수
print(car.find("구매했어요")) #8
print(car.find("판매했어요")) #-1

# 공백 문자 제거 - strip()
str = " Hi~ han."
print(str.strip()) #양쪽 공백 제거
print(str.lstrip()) #왼쪽 공백 제거

str2 = "Hi~ han. "
print(str2.strip())
print(str2.rstrip()) #오른쪽 공백 제거

# 실습 문제
# python-programming
arr_str = input("Input string: ").split('-')
arr_len = int(input("Input number: "))
arr_val = list(range(0, arr_len, 2))
arr_val.remove(4)

print(arr_str) # ['python', 'programming']
# print(arr_val) # range(0, 10, 2) → [0, 2, 4, 6, 8]
print(arr_val) # [0, 2, 6, 8]

print(arr_str[1].find('e')) # -1
print(arr_val[2]) # 6
print(arr_str[1].find('e') + arr_val[2]) # 5