# 다중 조건문(if ~ elif ~ else)
"""
나이         구분       입장료
3 ~ 7       미취학      1000
8 ~ 13      초등        2000
14 ~ 19     중,고등     2500
20 ~ 100    일반인      3000
"""

print("♣ 놀이공원 입장료 계산 ♣")
age = int(input("나이를 입력하세요: ")) #나이

if age >= 3 and age < 8:
    print("미취학 아동입니다.")
    admission_fee = 1000 #입장료    
elif age >=8 and age < 14:
    print("초등학생입니다.")
    admission_fee = 2000
elif age >=14 and age < 20:
    print("중,고등학생입니다.")
    admission_fee = 2500
else:
    print("일반인입니다.")
    admission_fee = 3000

print("입장료는 " + str(admission_fee) + "원 입니다.")
