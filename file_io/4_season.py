# 리스트의 요소를 쓰기

seasons = ["봄", "여름", "가을", "겨울"]
# 텍스트 파일 저장 시에 한글이 깨지지 않도록 함 - encoding="utf-8"
with open("./output/season.txt", "w", encoding="utf-8") as f:
    for season in seasons:
        f.write(season)
        f.write('\n')

# 텍스트 파일 읽기
with open("./output/season.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(text)
    