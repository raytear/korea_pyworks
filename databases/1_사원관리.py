# 사원 관리
# sqlite3언어 사용 DB 브라우저에 접속
import sqlite3

# mydb.db에 연결
'''
sqlite3.connect("c:/pydb/mydb.db")
print("DB 연결 성공!!")
'''

# 사원 전체 검색
def select_all():
    try:
        with sqlite3.connect("c:/pydb/mydb.db") as conn:
            cur = conn.cursor() #커서(cursor) - sql 처리 객체
            sql = "SELECT * FROM employee"
            cur.execute(sql) #sql문 실행(검색)
            # 검색된 자료를 가져오기
            rs = cur.fetchall() #모든 자료
            # print(rs)
            for i in rs:
                print(i)
    except sqlite3.Error:
        print("데이터베이스 오류")

# 사원 1명 추가
def insert():
    try:
        with sqlite3.connect("c:/pydb/mydb.db") as conn:
            cur = conn.cursor()
            sql = "INSERT INTO employee VALUES ('e104', '우상혁', 3500000)"
            cur.execute(sql) #sql문 처리(삽입)
            conn.commit() #트랜잭션(커밋 완료)
            # conn.close() #with ~ as 구문은 생략함
    except sqlite3.Error:
        print("데이터베이스 오류")

# 사원 수정
def update():
    try:
        with sqlite3.connect("c:/pydb/mydb.db") as conn:
            cur = conn.cursor()
            sql = "UPDATE employee SET name = '임시현', salary = 4000000 " \
                "WHERE id = 'e103'"
            cur.execute(sql)
            conn.commit()
    except sqlite3.Error:
        print("데이터베이스 오류")

def select_one():
    try:
        with sqlite3.connect("c:/pydb/mydb.db") as conn:
            cur = conn.cursor()
            sql = "SELECT * FROM employee WHERE name LIKE '이정후'"
            cur.execute(sql)
            rs = cur.fetchone() # 1건 검색
            print(rs)
    except sqlite3.Error:
        print("데이터베이스 오류")

def delete():
    try:
        with sqlite3.connect("c:/pyd/mydb.db") as conn:
            cur = conn.cursor()
            sql = "DELETE FROM employee WHERE id = 'e103'"
            cur.execute(sql) #sql 처리(삭제)
            conn.commit()
    except sqlite3.Error:
        print("데이터베이스 오류")

# insert() #사원 추가 함수 호출
# update() #사원 수정 함수 호출
# select_one() #사원 1명 검색(상세 보기)

delete() #사원 1명 삭제 함수 호출
select_all() #사원 전체 검색 함수 호출