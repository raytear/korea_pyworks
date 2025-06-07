# 객체의 형태를 그대로 유지하면서 파일 쓰고 읽기
# 객체 - 리스트, 딕셔너리, 튜플
#pickle.dump() - 쓰기, pickle.load() - 읽기
import pickle

try:
    with open("./output2/object.dat", "wb") as f:
        lis = ['강아지', '고양이', '닭']
        dic = {1: '강아지', 2: '고양이', 3: '닭'}
        
        pickle.dump(lis,f) #파일에 저장
        pickle.dump(dic,f) #파일에 저장
except:
    print("파일을 찾을 수 없습니다.")

# 파일 읽기
try:
    with open("./output2/object.dat", "rb") as f:
        list = pickle.load(f)
        dict = pickle.load(f)
        print(list)
        print(dict)
except:
    print("파일을 찾을 수 없습니다.")