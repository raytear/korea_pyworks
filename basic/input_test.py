# 입력 처리 실습 문제
# 나이를 계산하는 프로그램
birth_year = input("태어난 연도를 입력하세요: ")
print(type(birth_year))

# 나이 = 현재년도 - 태어난연도
age = 2025 - int(birth_year) #문자를 정수로 변환
print(birth_year, "년에 태어난 사람의 나이는", age, "세 입니다.")

# 출력할 때는 숫자를 문자로 변환함
print(str(birth_year) + "년에 태어난 사람의 나이는 " + str(age) + "세 입니다.")

# f포맷 방식 - f다음에 쌍따옴표로 감싸고, 변수는 중괄호({})로 감싼다.
print(f"{birth_year}년에 태어난 사람의 나이는 {age}세 입니다.")
