# 변수의 유효 범위
# 지역변수에 global을 붙이면 전역변수화(정적 변수) 함
# 전역변수와 생명 주기가 같음(프로그램이 종료되면 소멸)

def one_up2():
    global x #x는 전역변수화 됨
    x += 1
    return x

x = 1 #전역변수
print(one_up2()) #2
print(one_up2()) #3
print(one_up2()) #4

# 배송비 계산하기
'''
    상품 가격이 40000원 이상이면 배송비 3000원을 포함하고, 
    40000원 이상이면 배송비를 포함하지 않는 프로그램 만들기
'''
def get_price(unit_price, quantity):
    # 배송비
    delivery_fee = 3000
    # 가격 = 단위당 가격 * 수량
    price = unit_price * quantity
    if price < 40000:
        price = price + delivery_fee
    else:
        price
    return price

# main() 영역
# 상품1 가격 - 25000원, 수량 2개 - 배송비 미포함(50000)
# 상품2 가격 - 30000원, 수량 1개 - 배송비 포함(33000)

price1 = get_price(25000, 2)
price2 = get_price(30000, 1)

print("상품1 가격:" + str(price1) + "원")
print("상품2 가격:" + str(price2) + "원")
