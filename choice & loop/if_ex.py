"""
순차구조(sequential structure) - 위에서 아래로, 한 줄씩 실행
선택구조(choice structure) - 분기문(if)
반복구조(repetition structure) - 반복문(while, for)
"""

# 조건문
# 나이가 15세 이상이면 "관람가" 출력

age = input("나이를 입력하세요: ")
age = int(age) #int("문자")문자를 정수로 변환함

"""
if age >= 15: #조건식 True이면 실행됨
    print("관람가") #들여쓰기(indent)
print("나이는 " + str(age) + "세입니다.")
"""

# 나이가 15세 이상이면 "관람가" 아니면 "관람불가" 출력

if age >= 15:
    print("관람가")
else:
    print("관람불가")

"""
elif age < 15:
    print("관람불가")
"""

print("나이는 " + str(age) + "세입니다.")


# 어떤 수를 입력받아서 짝수인지 홀수인지 판별하는 프로그램
# 4 % 2 == 0, 5 % 2 == 1

print(4 + 5)
print(4 - 5)
print(4 * 5)
print(4 / 5)
print(4 // 5) #몫
print(4 % 5)  #나머지


# 비교 연산 (결과값: True/False)
print(4 > 5) #False
print(4 == 5) #False
print(4 != 5) #True
print(4 % 2 == 0) #True
print(5 % 2 == 0) #False


#num=12 → num이라는 변수에 12를 저장(기억)
num = input("숫자를 입력하세요: ")
num = int(num) #입력된 문자를 숫자로 변환

if num % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

"""
 - 입장객 수와 좌석열 수를 입력받아 줄 수 계산하기
 - 좌석열(column), 줄(행) 수(row)
 - 입장객 수가 좌석열에 나누어 떨어지는 경우,
   나누어 떨어지지 않는 경우
   예) 20 / 5 => 4줄, 21 / 5 => 5줄
"""

customer = int(input("입장객 수 입력: ")) #입력된 문자를 정수로 변환
column = int(input("좌석열 수 입력: "))

if customer % column == 0:
    row = int(customer / column) #실수를 정수로 변환
else: #customer % column != 0:
    row = int(customer / column) + 1
    
print(str(row) + "개의 줄이 필요합니다.")
