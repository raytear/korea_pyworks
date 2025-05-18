# set(집합) 자료 구조
# 중괄호({}) 사용
# 중복 허용되지 않고, 순서가 없다.

s1 = {1, 2, 3, 1, 2}
print(s1)
print(type(s1))

s2 = {'s', 'k', 'y'}
print(s2)

# 빈 집합 생성
s2 = set()
print(s2)

# 요소 추가 - add() 함수 사용
s2.add('a')
s2.add('p')
s2.add('p')
s2.add('l')
s2.add('e')
print(s2)

# 요소 삭제
s2.remove('a')
print(s2) #{'e', 'l', 'p'}

# 요소 수정 불가
# s2[1] = 'm'

# 문자열
# str = "apple"
# print(str)