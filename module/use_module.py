"""
# food.py 모듈 사용
from my_lib.food import cook, eat, name
from my_lib.calculator import add, sub, mul, div

# calculator.py 사용
#덧셈
addition = add(10, 4)
print(addition) #14

#뺄셈
subtraction = sub(10, 4)
print(subtraction) #6

#곱셈
multiple = mul(10, 4)
print(multiple) #40

#나눗셈
#division = div(10, 4)
#ZeroDivisionError: division by zero
division = div(10, 0)
print(division) #2.5

# food.py 사용
cook()
eat()
print(name)
"""
# from 패키지(디렉터리) 이름 import 모듈이름
from my_lib import food
from my_lib import calculator

# calculator
print(calculator.add(10, 4))
print(calculator.sub(10, 4))
print(calculator.mul(10, 4))
print(calculator.div(10, 4))

# food
print(food.name)
food.cook()
food.eat()