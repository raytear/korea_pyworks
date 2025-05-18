# tuple 자료구조
# 튜플 자료구조는 소괄호() 사용
t = (1, 2, 3)
print(t)
print(type(t))

# 인덱싱(조회)
print(t[0])
print(t[1])
print(t[2])

# 슬라이싱
print(t[1:3]) #(2, 3)
print(t[:])

# 수정 불가
# t[1] = 4

# 삭제 불가
# del t[1]

# 요소를 1개 저장하기
# t1 = (1) - 튜플이 아닌 정수임
t1 = (10,)
print(t1)
print(type(t1))

# tuple 합치기
t2 = t + t1
print(t2)

'''
a= [1, 2, 3]
print(a)
print(type(a))

# 리스트 - 중복 허용, 순서가 정해짐
a = [1, 2, 3, 1, 2]
print(a)
print(type(a))

# 인덱싱
print(a[0])     #1
print(a[-1])    #3

# 수정
a[1] = 4
print(a)

d = {1: 'a', 2: 'b', 3: 'c'}
print(d)
print(type(d))
print(d[1])
print(d[3])
print(d.keys())
print(d.values())

# 수정
d[2] = 'd'
print(d)
'''