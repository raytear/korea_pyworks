# 상속
class Animal:
    def breath(self):
        print("동물은 숨을 쉽니다.")
    
    # raise - 예외 처리를 미루면 사용하는 곳에서 try ~ except함
    def cry(self):
        raise NotImplementedError("반드시 메서드를 구현해야 합니다.")

# Animal을 상속받은 Dog 클래스
class Dog(Animal):
    def cry(self):
        print("왈~ 왈~")

class Cat(Animal):
    pass

# 부모클래스의 인스턴스 생성
animal = Animal()
animal.breath()

try:
    # 자식클래스의 인스턴스 생성
    dog = Dog()
    dog.breath() #부모 클래스의 메서드 호출
    dog.cry()

    cat = Cat()
    cat.cry()
except NotImplementedError as e:
    print(f'오류: {e}')