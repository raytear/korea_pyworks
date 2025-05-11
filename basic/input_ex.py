# 입력 처리
# input() 사용
"""
print("문자 입력: ")
ch = input() #키보드로 입력한 값을 저장할 변수

print(ch)
"""

ch = input("문자 입력: ")
print(ch)


# 숫자 입력
num = input("숫자 입력: ")
num = int(num) #문자를 정수로 변환
print(type(num))

print(num + 1)


# 이름과 나이 입력받기
name = input("이름 입력: ")
print(name + "님 반가워요.")

age = input("나이 입력: ")
print(type(age)) #str
age = int(age) #문자를 숫자로 변환
#print("당신의 나이는 ", age, "세 이군요")
# 문자열끼리 더할 수 있도록 age를 str로 형변환해
print("당신의 나이는 " + str(age) + "세 이군요")
