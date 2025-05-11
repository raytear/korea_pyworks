# 연산자 - 대입, 산술, 비교(논리)
# 변수 만들기
# '='은 대입 연산자
user_id = "smile"
password = "k1234"

print("user_id =", user_id)
print("password =", password)

# 변수값 교환하기
x = 1
y = 2

print("===== 교환전 =====")
print("x =", x, ", y =", y)

# 교환
temp = x
x = y
y = temp

print("===== 교환후 =====")
print("x =", x, ", y =", y)

# 산술 연산
n1 = 10
n2 = 4

print("n1 + n2 =", n1 + n2)
print("n1 - n2 =", n1 - n2)
print("n1 * n2 =", n1 * n2)
print("n1 / n2 =", n1 / n2) #나누기
print("n1 // n2 =", n1 // n2) #몫
print("n1 % n2 =", n1 % n2) #나머지
print("n1 ** n2 =", n1 ** n2) #거듭제곱

# 비교 연산
x = 10
y = -10

print(x > 0) #True
print(y > 0) #False
print()

print(x > y) #True
print(x < y) #False
print()

print(x == 10) #True
print(x == y) #False
print(x != y) #True
print(x is y) #False
print(x is not y) #True
print()

# 논리 연산 - and, or, not
# and - 2개의 조건이 모두 참일 때 참이다.
# or - 2개의 조건 중 1개만 참이어도 참이다.
print(x > 0 and y > 0) #False
print(x > 0 or y > 0) #True
print(not (y > 0)) #True

# 비트 연산
# 문자열 연산('+', '*')
head = "Good"
tail = " Job!"

print(head + tail) #문자 연결

print('=' * 10)
print(head + tail)
print('=' * 10)
