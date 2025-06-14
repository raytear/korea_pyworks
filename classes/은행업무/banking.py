# 은행 업무 - 입금, 출금, 잔액 조회

balance = 0 #전역 변수(값을 공유)
while True:
    print("=========================================")
    print("1. 예금 | 2. 출금 | 3. 잔액조회 | 4. 종료")
    print("=========================================")

    try:
        choice = input("선택> ") #사용자 입력
        if choice == '1':
            amount = int(input("입금액> ")) #금액(정수로 형변환)
            balance += amount #잔고 = 잔고 + 입금액
            print(f"{amount}원 입금되었습니다. 현재 잔액: {balance}")

        elif choice == '2':
            amount = int(input("출금액> "))
            if(amount > balance):
                print(f"잔액이 부족합니다. 현재 잔액: {balance}")
            else:
                balance -= amount #잔고 = 잔고 - 출금액
                print(f"{amount}원 출금되었습니다. 현재 잔액: {balance}")
        elif choice == '3':
            print(f"잔액> {balance}")
        elif choice == '4':
            print("프로그램 종료")
            break
        else:
            print("메뉴를 잘못 선택했습니다. 다시 입력해주세요")
    except ValueError:
        print("숫자를 입력해주세요.")