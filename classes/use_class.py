# 모듈 사용하기
from 은행업무.bank_account import BankAccount

# BankAccount의 인스턴스(객체)
account = BankAccount()

# 입금하기
account.deposit(10000)

# 출금하기
# account.withdraw(20000) #오류발생
account.withdraw(5000)

# 잔고조회
account.get_balance()

# 거래내역 조회
# print(account.get_transaction_history())
print("\n[거래내역]")
for trans in account.transaction_history:
    print(f"- {trans[0]}: {trans[1]}원")