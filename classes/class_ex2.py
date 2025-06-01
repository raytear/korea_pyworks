# 계산기 클래스 - 사칙연산 기능 수행
'''
class Calculator:
    # 생성자에 멤버 변수가 포함됨
    def __init__(self):
        self.x = 0  # x변수에 0이 저장

    def add(self, y): #덧셈
        self.x += y  #self.x = self.x + y
        return self.x

    def sub(self, y): #뺄셈
        self.x -= y
        return self.x
    
    def mul(self, y):
        self.x *= y
        return self.x
    
    def div(self, y):
        if y != 0:
            self.x /= y
        else:
            print("Error: 0으로 나눌수 없습니다.")
        return self.x

# 인스턴스 생성
cal = Calculator() 
print(cal.add(10)) #10
print(cal.sub(4))  #6
print(cal.mul(2))  #12
# print(cal.div(10)) #1.2
print(cal.div(0)) #1.2
'''

# 캡슐화(정보 은닉)
# private - 같은 클래스 내부만 접근 가능, 외부에서 접근 불허
# public - 외부 클래스 어디에서나 접근 가능함

# 멤버변수에 언더스코어 2개를 붙이면 private 멤버가 됨
"""
class BankAccount:
    def __init__(self):
        self.__ano = ""    # 계좌번호
        self.owner = ""  # 계좌주
        self.balance = 0 # 잔고

# 은행 계좌 인스턴스 생성
# 캡슐화 위배
account = BankAccount()
# account.ano = "12-1234"  
# account.__ano = "12-1234" #ano에 접근 못함
print(account.__ano)
"""

# private 멤버는 메서드를 만들어 설정과 접근함
# set + 멤버변수(설정자), get + 멤버변수(접근자)
class BankAccount:
    def __init__(self):
        self.__ano = ""    #private (멤버변수)
        self.__owner = ""
        self.__balance = 0

    #계좌 번호 설정(저장)
    def set_ano(self, ano):  #public (메서드)
        self.__ano = ano

    # 계좌 번호 가져오기
    def get_ano(self):
        return self.__ano
    
    # 계좌주 설정
    def set_owner(self, owner):
        self.__owner = owner

    # 계좌주 가져오기
    def get_owner(self):
        return self.__owner

    # 잔고 설정
    def set_balance(self, balance):
        self.__balance = balance

    # 잔고 가져오기
    def get_balance(self):
        return self.__balance
    
# 계좌 생성
account1 = BankAccount()

# 계좌정보 입력(저장)
account1.set_ano("12-1234")
account1.set_owner("신유빈")
account1.set_balance(20000)

# 계좌정보 출력
print("계좌번호:", account1.get_ano())
print("계좌주:", account1.get_owner())
print("잔고:", account1.get_balance())