# 변수의 유효 범위
'''
    - 전역 변수
      메인 함수 영역에 선언(생성)하고 범위가 전체에 미침
      프로그램이 종료되면 메모리에서 소멸(해제)됨
    - 지역 변수
      함수나 제어문(조건, 반복)의 블록 안에서 생성되고
      블록을 벗어나면 소멸(해제)됨  

'''

def get_price():
    #price는 지역 변수
    price = 1000 * quantity
    print(f"{quantity}개에 {price}원 입니다.")

def one_up():
    x = 1   #지역변수
    x += 1
    return x

print(one_up()) #2   
print(one_up()) #2   


# 전역 변수
quantity = 2 # 수량
# get_price()  # 호출(사용) 

# 변수 출력
# print(quantity)
# print(price) #소멸된 변수임
