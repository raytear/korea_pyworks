# 그룹핑(Grouping) - 소괄호로 그룹을 구분
# 이름과 전화번호 구분하기
import re

phone = "jang  010-1234-5678"
pat = re.compile("(\w+)\s{1,2}(010-\d{3,4}-\d{4})") #\w - 영어 대소문자, 숫자 포함, \s - 공백
mat = pat.match(phone)
print(mat.group())
print(mat.group(1)) #jang
print(mat.group(2)) #010-1234-5678

# sub() - 그룹을 표시
# sub(\g<1>) - 그룹1
# 폰번호 뒷 4자리 마스킹 처리
pattern = re.compile("(\w+)\s{1,2}(010-\d{3,4})-\d{4}")

print(pattern.sub("\g<1>", phone)) #jang
print(pattern.sub("\g<2>-****", phone))