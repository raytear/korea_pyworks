# 다중 예외 처리

try:
    data = [50, 40, 80, 60]
    x = int(input("정수 입력(0~3): "))

    print(data[x])

    # print(data[4]) # IndexError
except IndexError:
    print("범위를 초과했어요. 0~3까지 입력하세요.")
except ValueError as e:
    print(e)
    print("유효하지 않은 숫자입니다. 숫자를 입력하세요.")