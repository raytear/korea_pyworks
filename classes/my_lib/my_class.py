# 클래스 만들기
class Car:
    # 모델명, 연식 - 속성
    # 생성자(필수 요소)
    def __init__(self, model, year):
        self.model = model
        self.year = year

    # 인스턴스의 문자열 정보
    def __str__(self):
        return f"모델명: {self.model}, 연식: {self.year}"

if __name__ == "__main__":
    # Car의 인스턴스(객체) 생성
    c1 = Car("Ionic6", 2024)
    print(c1)


# 쇼핑몰 장바구니 구현
class Cart:
    #생성자
    def __init__(self, user):
        self.user = user
        self.items = []   #장바구니 리스트

    # '*'(가변 매개변수) - 리스트
    # 리스트 추가 - extend() 사용
    def add(self, *goods):
        self.items.extend(goods)

    # 품목 삭제
    def remove(self, item):
        # 리스트의 주요 함수(삭제) - remove()
        if item in self.items:  #장바구니에 리스트에 존재하는 품목
            self.items.remove(item)  #품목 삭제

    # 인스턴스 정보를 문자열로 출력
    def __str__(self):
        return f"{self.user}의 장바구니: {self.items}"

if __name__ == "__main__":
    # Cart의 인스턴스 생성
    my_cart = Cart("박이슬")

    # 품목 추가
    my_cart.add("계란", "우유", "쌀")

    # 품목 삭제
    my_cart.remove("우유")
    my_cart.remove("콩나물")

    print(my_cart)
