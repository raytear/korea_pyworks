# 딕셔너리를 이용한 성적 관리
# 여러개의 값을 저장할 수 있고, 키와 값으로 대응된 구조
# 학생의 성적 통계
student_list = [
    {"name": "이대한", "kor": 80, "eng": 80, "mth": 75},
    {"name": "박민국", "kor": 90, "eng": 75, "mth": 60},
    {"name": "최지능", "kor": 95, "eng": 98, "mth": 90}
]

# 첫번째 요소 검색
print(student_list[0]) #0번 인덱스로 검색
print(student_list[1])

print("========= 성적표 =========")
print(" 이름   국어 영어 수학 ")
for st in student_list:
    print(f"{st["name"]}   {st["kor"]}   {st["eng"]}   {st["mth"]}")

# 개인별 총점과 평균
# 소수점 자리 처리 - 점(.) 찍고 자리수와 f(float) 사용 
print("=== 개인별 총점과 평균 ===")
print(" 이름   총점 평균 ")
for st in student_list:
    total = st["kor"] + st["eng"] + st["mth"] #총점
    avg = total / 3 #평균
    print(f"{st["name"]}  {total}  {avg:.1f}")

# 과목별 총점과 평균
sum_subj = [0, 0, 0] #국어 총점, 영어 총점을 저장
avg_subj = [0.0, 0.0, 0.0] #국어 평균, 영어 평균

# 총점 계산
for st in student_list:
    sum_subj[0] = sum_subj[0] + st["kor"]
    sum_subj[1] = sum_subj[1] + st["eng"]
    sum_subj[2] = sum_subj[2] + st["mth"]

# 평균 계산
for st in student_list:
    avg_subj[0] = sum_subj[0] / len(student_list)
    avg_subj[1] = sum_subj[1] / len(student_list)
    avg_subj[2] = sum_subj[2] / len(student_list)

print("====== 과목별 총점 ======")
print(f"국어 총점:  {sum_subj[0]}")
print(f"영어 총점:  {sum_subj[1]}")
print(f"수학 총점:  {sum_subj[2]}")

print("====== 과목별 평균 ======")
print(f"국어 평균:  {avg_subj[0]:.2f}")
print(f"영어 평균:  {avg_subj[1]:.2f}")
print(f"수학 평균:  {avg_subj[2]:.2f}")

"""
cart = {'fruit': '딸기', 'dring': '맥주'}
print(cart) #딕셔너리 객체 형태로 출력
print(type(cart)) #dict
print(cart.keys())
print(cart.values())

# 요소 검색 - '키'로 검색
print(cart['fruit'])

# 전체 출력
for key in cart:
    print(key, ':', cart[key])

# fruit : 딸기
# dring : 맥주
"""