# 클래스의 정의와 사용
# 클래스 - 객체(사물)에 대한 속성(변수)과 기능(메서드)을 코드로 구현한 것
"""
class Student:
    name = "김하나" #속성-property, 멤버 변수
    grade = 3

    #클래스 내부의 모든 함수(메서드)의 매개변수는 self를 넣어야 함
    def learn(self):
        print("수업을 들어요.")

# 사용 - 클래스의 객체 생성
st = Student()   #생성자

# st로 속성과 기능에 접근
print("이름:", st.name)
print("학년:", st.grade)
st.learn()

"""

# 클래스 주요 3요소 - 속성(변수), 생성자, 함수(메서드)
# self는 멤버 변수와 메서드에 모두 사용함(필수)
# def __init__(self): → init 양 옆 __(언더바 2개) 작성 주의
'''
class Student:
    #생성자(초기자) - Constructor
    def __init__(self):
        self.name = "콩쥐"
        self.grade = 1

    def learn(self):
        print("수업을 들어요.")

st = Student()
print(f'{st.name}학생은 {st.grade}학년입니다.')
st.learn()

'''

# 클래스는 여러 개의 인스턴스를 생성할 수 있다
# 매개변수가 있는 생성자
class Student:
    #생성자
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def learn(self):
        print("수업을 들어요")
    '''
    # 학생 정보 출력 메서드
    def show_info(self):
        return f'{self.name} 학생은 {self.grade}학년입니다.'
    '''
    def __str__(self): #파이썬 제공 - 문자열 정보
        return f'{self.name} 학생은 {self.grade}학년입니다.'

'''
# 인스턴스 생성
st1 = Student("콩쥐", 2)
print(st1) #객체 출력
st1.learn()

st2 = Student("팥쥐", 1)
#print(st2.show_info())
print(st2)
st2.learn()

'''


# 객체 리스트 생성
students = [
    Student("김하나", 1),
    Student("박열", 3),
    Student("이넷", 4)
]

# 첫번째 인스턴스 출력
print(students[0])
print()

print("----- 학생 명단 -----")
for st in students:
    print(st)