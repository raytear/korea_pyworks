# 파일에 쓰기 추가 - "a" 모드 사용
f = open("c:/pyfile/file1.txt", "a")

f.write("Have a good time")

print("쓰기 추가 완료!")
f.close()