print("여러 개의 반환값")
"""
def add_and_mul(x, y):
    return x+y, x*y

value1 = add_and_mul(10, 20)
print(value1) #(30, 200)
print(type(value1)) #tuple

# 구조 할당
add, mul = value1
print(f'{add} {type(add)}') #30, int
print(f'{mul} {type(mul)}') #200, int

"""

# 변수의 유효범위 - 전역변수, 지역변수, 정적변수(global)
'''
print("변수의 유효 범위")
g1 = 1
def funcA():
    g1 = 100 #지역 변수(global g1이면 전역변수가 됨)
    global g2 #전역변수화 함
    l_value = 10 #지역변수
    print("g1:", g1) #100
    print(g2) #python
    print(l_value) #10
    g1 =  200
    print(g1) #200

g2 = "python" #전역 변수
funcA() #호출
print("g2:", g2)
# print(l_value) #값이 할당되지 않은 변수

# 중복검사
# 리스트(list), 셋(set)
a1 = [1, 2, 3, 2, 2]
s1 = {1, 2, 3, 2, 2}

print(a1) # [1, 2, 3, 2, 2] 
print(a1[3]) #2

print(s1) #{1, 2, 3} #중복 불허
print(s1[3]) #인덱싱 안됨
'''

# 동명이인 찾기
# 1. 리스트로 구현하기
def find_same_name(a):
    same_name = []
    n = len(a) #리스트의 크기
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                same_name.append(a[i])

    return same_name

# 2. set으로 구현하기
def find_same_name2(a):
    same_name = set() #빈 집합 생성
    n = len(a) #리스트의 크기
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                same_name.add(a[i])

    return same_name

'''
['콩쥐', '흥부', '팥쥐', '흥부']
i=0(1행),
        j=1, a[0] == a[1], False
        j=2, a[0] == a[2], False
        j=3, a[0] == a[3], False
i=1(2행),
        j=2, a[1] == a[2], False
        j=3, a[1] == a[3], True [흥부]
i=2(3행),
        j=3, a[2] == a[3], False
i=3(4행),
        for문 종료       
'''

v = ['콩쥐', '흥부', '팥쥐', '흥부']
result1 = find_same_name(v)
print(result1)

result2 = find_same_name2(v)
print(result2)