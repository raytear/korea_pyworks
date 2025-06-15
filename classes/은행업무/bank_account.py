# 은행 계좌 클래스 활용
class BankAccount:
    # 생성자 함수
    def __init__(self):
        self.balance = 0 #잔고
        self.transaction_history = [] #거래 내역
    
    # 입금
    def deposit(self, amount):
        self.balance += amount #잔고 = 잔고 + 입금액
        self.transaction_history.append(('입금', amount))
        print(f"{amount}원 입금되었습니다. 현재 잔액: {self.balance}")

    # 출금
    def withdraw(self, amount):
        if(amount > self.balance):
            print(f"잔액이 부족합니다. 현재 잔액: {self.balance}")
        else:
            self.balance -= amount #잔고 = 잔고 - 출금액
            self.transaction_history.append(('출금', amount))
            print(f"{amount}원 출금되었습니다. 현재 잔액: {self.balance}")
    
    # 잔액 조회
    def get_balance(self):
        return self.balance

    # 거래내역 조회
    def get_transaction_history(self):
        return self.transaction_history
    
# 메인 함수
def main():
    # BankAccount 객체(인스턴스) 생성
    account = BankAccount()

    while True:
        print("============================================================")
        print("1. 예금 | 2. 출금 | 3. 잔액조회 | 4. 거래내역 조회 | 5. 종료")
        print("============================================================")

        try:
            choice = input("선택> ") #사용자 입력
            if choice == '1':
                amount = int(input("입금액> "))
                account.deposit(amount) #입금 함수 호출
            elif choice == '2':
                amount = int(input("출금액> "))
                account.withdraw(amount) #출금 함수 호출
            elif choice == '3':
                print(f"현재 잔액> {account.get_balance()}")
            elif choice == '4':
                print("\n[거래 내역]")
                for type, amount in account.transaction_history:
                    print(f"- {type}: {amount}원")                
            elif choice == '5':
                print("프로그램 종료")
                break
            else:
                print("메뉴를 잘못 선택했습니다. 다시 입력해주세요")
        except ValueError:
            print("숫자를 입력해주세요.")

if __name__ == "__main__":
    main() #실행 함수 호출
