# with ~ as 구문 사용 - f.close() 사용하지 않음
# 파일의 위치 - 상대경로(내 위치를 기준으로 설정)
# './output/gugu.txt' -> 점(.) 1개는 내 위치와 같은 계층
with open('./output/gugu.txt', 'w') as f:
    for i in range(2, 10):
        for j in range(1, 10):
            gugudan = f"{i} x {j} = {i*j}\n"
            f.write(gugudan)
        f.write('\n')