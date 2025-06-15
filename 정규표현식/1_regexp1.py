# 정규 표현식 - 특정한 메타문자를 사용해서 문자열을 검색 또는 변경하는 표현식
# 예) 아이디나 비밀번호 또는 전화번호가 입력 형식에 맞는지 유효성 검사
# 예) 주민번호 뒷자리 등을 마스킹 처리(*문자로 변경)
import re

"""
# 'korea'란 문자열을 정규표현식으로 조사
pattern = re.compile("^[a-z]+") #정규표현식
# match() - 문자의 처음부터 일치하는지 검색
match = pattern.match("korea")
print(match) #<re.Match object; span=(0, 5), match='korea'>
# print(match.group()) #k
# print(match.start()) #0
# print(match.end()) #5
if match:
    print("일치하는 문자열 있음: ", match.group())
else:
    print("일치하는 문자열 없음")

# 전화번호 검증 - "010-1234-5678"
phone_pat = re.compile("010-[0-9]{3,4}-[0-9]{4}")
mat = phone_pat.match("010-12-5678")
# bool() - True / False로 결과 반환
print(bool(mat)) #False

# 한글이름 검증
name_pat = "제갈수연동우"
pat = re.compile("[가-힣]{2,5}")
mat = pat.fullmatch(name_pat)
print(bool(mat)) #False
"""

# 전화번호 패턴의 유효성(validation) 검사
def validate_phone_number(phone):
    # phone_pat = re.compile("010-[0-9]{3,4}-[0-9]{4}")
    phone_pat = re.compile("010-\d{3,4}-\d{4}") #\d → [0-9]와 같음
    return bool(phone_pat.fullmatch(phone))

phone_list = [
    "010-1234-5678", #유효
    "010-123-4567",  #유효 
    "010-12-5678",   #무효 
    "01012345678",   #무효 
    "010-1234-567"   #무효 
]

print("== 전화번호 검증 결과 ==")
for phone in phone_list:
    print(f'{validate_phone_number(phone)}')