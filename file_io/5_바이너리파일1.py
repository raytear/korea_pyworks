# 바이너리 파일 쓰고 읽기
# 쓰기 모드 - "wb", 읽기 모드 - "rb"
"""
with open("./output/data.bin", "wb") as f:
    text = "비가 내린다."
    f.write(text.encode()) # encode() - 코드화 함(0, 1로 바꾸는 함수)

with open("./output/data.bin", "rb") as f:
    data = f.read()
    print(data.decode()) # decode() - 코드를 문자로 바꿈(복호화)
"""

# 이미지 파일 복사 - 읽고 쓰기
try:
    with open("./output/bird.jpg", "rb") as f1:
        image = f1.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")


# 쓰기
try:
    with open("./output2/bird.jpg", "wb") as f2:
        f2.write(image)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")