# 리스트 데이터를 파일에 쓰기
f = open("c:/pyfile/cartlist.txt", "w")

# 파일 쓰기
cartlist = ["계란", "우유", "바나나", "라면"]

for cart in cartlist:
    f.write(cart + " ")

print("쓰기 완료!")
f.close()