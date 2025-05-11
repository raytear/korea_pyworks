# 반복 조건문
"""
 'y'키 입력 → "계속 반복"
 'n'키 입력 → "반복 중단"
 y/n 이외의 키 → "키를 잘못 눌렀습니다."
 
"""

while True:
    answer = input("반복을 계속 할까요(y or n 입력): ")
    if answer == 'y' or answer == 'Y':
        print("계속 반복")
    elif answer == 'n' or answer == 'N':
        print("반복 중단")
        break
    else:
        print("키를 잘못 눌렀습니다.")
        
print("프로그램 종료!")

"""
챗봇(chatbot) 프로그램
- 단어가 포함되어 있으면 출력하는 프로그램

"""
animal = "dog"

# 철자 존재 유무 확인
# in 명령어 - 있다/없다를 확인하는 명령어임
print('d' in animal) #True
print('c' in animal) #False
print('g' not in animal) #False

animals = "dog cat horse"
print('cat' in animals) #True
print('cow' in animals) #False

while True:
    user_input = input("사용자(exit 입력시 종료): ")

    if user_input == "exit":
        print("챗봇: 대화를 종료합니다. 안녕히 가세요!")
        break
    
    elif "안녕" in user_input:
        print("챗봇: 안녕하세요! 반가워요!")
        
    elif "이름" in user_input:
        print("챗봇: 저는 Python 챗봇입니다.")
        
    elif "날씨" in user_input:
        print("챗봇: 날씨앱이나 검색 기능을 이용하세요.")
        
    else:
        print("챗봇: 죄송해요. 잘 이해하지 못했어요.")






























        
