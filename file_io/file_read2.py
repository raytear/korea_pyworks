# 파일 읽기
f = open("c:/pyfile/cartlist.txt", "r")

# list = f.read()
# print(list) #"계란", "우유", "바나나", "라면"

# 문자열 → 리스트 변환
# split() → 공백문자일 경우 비워둔다.
list = f.read().split() #[#"계란", "우유", "바나나", "라면"]
print(list)

print(list[0]) #계란
print(list[-1]) #라면

f.close()