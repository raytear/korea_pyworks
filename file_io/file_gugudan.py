# 파일에 구구단 쓰기
# 5단
f = open("c:/pyfile/gugudan.txt", "w")

"""
dan = 5
for i in range(1, 10):
    f.write(f"{dan} x {i} = {dan * i}\n")
"""

# 구구단 전체
for i in range(2, 10):
    for j in range(1, 10):
        gugudan = f"{i} x {j} = {i * j}\n"
        f.write(gugudan)
    f.write("\n") #단별 줄바꿈
f.close()

# 구구단 파일 읽기
f = open("c:/pyfil/gugudan.txt", "r")

gugudan  = f.read()
print(gugudan)

f.close()