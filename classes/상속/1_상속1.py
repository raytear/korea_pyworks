# 클래스의 상속

class Person:
    # 생성자 (함수)
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"안녕하세요. 성명: {self.name}", end='')

    # 객체의 문자열 정보 출력 메서드    
    def __str__(self):
        return f"이름: {self.name}"
    
# Person을 상속받은 Employee 클래스 정의
class Employee(Person): #()안에 부모 클래스 사용
    def __init__(self, name, id):
        super().__init__(name) #부모 생성자 호출
        self.id = id

    def greet(self):
        super().greet()
        print(f", 사번은 {self.id}입니다.")

    def __str__(self): #메서드 재정의(Overriding)
        return super().__str__() + f", 사번: {self.id}"
        

'''
# p1 인스턴스(객체) 생성
p1 = Person("우영우")
print(p1) #객체 출력
p1.greet() #인사하기 메서드 출력

'''

# e1 인스턴스 생성
e1 = Employee("장그래", 'e1004')
print(e1)
e1.greet()

e2 = Employee("김대리", 'e1005')
print(e2)
e2.greet()

employees = [
    Employee("장그래",'e1004'),
    Employee("김대리",'e1005'),
    Employee("오과장",'e1006'),
    Employee("박차장",'e1007')
]

print("=== 사원 리스트 ===")
for e in employees:
    print(e)