# 리스트의 주요 메서드(함수)
'''
a = [1,2,3]

# 요소 추가
a.append(4) # 맨 뒤에서 추가

# 특정 위치에 추가
a.insert(1, 5)

# 요소 삭제
a.pop() # 맨 뒤의 요소 삭제

# 특정 위치에서 삭제 - [1, 5, 2, 3]
a.pop(1) # 1번 인덱스 값 삭제
# a.remove(5) # 요소 중 5를 삭제

print(a)
'''

car = ["Sonata", "BMW", "EV4", "Ionic6"]

# 요소 추가 - "모닝"을 추가
car.append("모닝")

# 요소 삭제 - "BMW" 삭제
# car.remove("BMW")
car.pop(1)

print(car)

# 리스트의 정렬 - sort()
n = [1, 4, 3, 2]
n.sort() #오름차순 정렬(작은 수 → 큰 수) #내림차순은 없음
print(n)

# 리스트 뒤집기(거꾸로) - 오름차순 후 뒤집기(=내림차순)
n.reverse()
print(n)

# 리스트의 복사
a1 = [1, 2, 3, 4, 5]
a2 = [] #a1을 복사할 빈 리스트 생성
a3 = [] #a1의 요소에 3의 배수로 저장

print("a1 =", a1)

# a1[0]를 a2[0]에 저장 - 1개 요소 저장
#a2.append(1)

# a1을 a2에 복사하기
for i in a1:
    a2.append(i)
print("a2 =", a2)

# a1의 요소에 3의 배수로 저장(복사)
# 조건 - 요소 중 10보다 작은 수 저장
for i in a1:
    if 3 * i < 10:
        a3.append(3 * i)
print("a3 =", a3)