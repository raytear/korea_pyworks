# 파일 읽기
# 읽기 모드 - "r"

# 파일 열기
f = open("c:/pyfile/file1.txt", "r")

# 파일 읽기
data = f.read()
print(data)

# 파일 닫기
f.close()