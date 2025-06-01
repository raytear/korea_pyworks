# 클래스 변수와 인스턴스 변수
# 카운터(Counter) 만들기
# 카운터1
"""
class Counter:
    # 생성자
    def __init__(self):
        self.x = 0  # 인스턴스 변수
        self.x += 1 #self.x = self.x + 1

    def get_count(self):
        return self.x
    
class Counter2:
    x = 0   # 클래스 변수

    def __init__(self):
        Counter2.x += 1  # 클래스 이름으로 직접 접근

    def get_count(self):
        return self.x

'''
# 인스턴스 생성
c1 = Counter()
print(c1.get_count())  #1

c2 = Counter()
print(c2.get_count())  #1
'''

# 방법 2
c1 = Counter2()
print(c1.get_count()) #1

c2 = Counter2()
print(c2.get_count()) #2

c3 = Counter2()
print(c3.get_count()) #3
"""

class Cls:
    x, y = 10, 20  # 클래스 변수

    # 교환 1
    def change(self):
        temp = self.x
        self.x = self.y
        self.y = temp

    # 교환 2
    def change2(self):
        # 구조 분할 방식
        self.x, self.y = self.y, self.x
    
# 인스턴스(객체) 생성
a = Cls()
# 교환전
print(a.x, a.y) # 10, 20

# 교환후
a.change()  #교환 매서드 호출
print(a.x, a.y) # 20, 10

# b 인스턴스 생성
b = Cls()
# 교환전
print(b.x, b.y) # 10, 20

# 교환후
b.change2()
print(b.x, b.y) # 20, 10