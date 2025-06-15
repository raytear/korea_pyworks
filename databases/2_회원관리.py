# 회원 DB 관리
# 별칭 사용 - sql
import sqlite3 as sql

# db 생성 및 연결
'''
with sql.connect("./mydb/member.db") as conn:
    print("DB 생성 및 연결 성공!!")
'''

# DB 연결 함수 정의
def getconn():
    try:
        with sql.connect ("./mydb/member.db") as conn:
            return conn
    except sql.Error as e:
        print(f"DB 오류 발생: {e}")
        return None
    
def create_table():
    '''테이블 생성'''
    conn = getconn()
    cur = conn.cursor()
    sql = """
    CREATE TABLE member(
        m_id TEXT PRIMARY KEY,
        m_passwd TEXT NOT NULL,
        m_name TEXT NOT NULL,
        m_gender TEXT,
        m_age INTEGER
    )
    """
    cur.execute(sql) #sql(실행)
    conn.commit() #커밋(트랜잭션)
    print("테이블 생성")

def insert_member():
    '''회원 등록'''
    conn = getconn()
    cur = conn.cursor()
    # 동적 바인딩 방식(? - 칼럼값 입력), 튜플 형태로 입력
    sql = "INSERT INTO member VALUES(?, ?, ?, ?, ?)"
    # cur.execute(sql, ('m1001', 'm1357@!', '우영우', '여자', 28))
    cur.execute(sql, ('m1002', 'm2468@!', '장그래', '남자', 25))
    conn.commit()
    print("회원 등록 완료!")

def select_all():
    '''회원 전체 검색'''
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql) 
    rs = cur.fetchall() # 모두 검색
    print(rs)
    for i in rs:
        print(i)

def select_one():
    '''회원 1명 검색'''
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member WHERE m_name LIKE ?"
    cur.execute(sql, ('장그래', )) 
    rs = cur.fetchone() # 1건 검색
    print(rs)

def update_member():
    '''회원 수정'''
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE member SET m_passwd = ?, m_name = ?, m_gender = ?, \
            m_age = ? WHERE m_id = ?"
    cur.execute(sql, ('m2468@!', '오상식', '남자', 45, 'm1002'))
    conn.commit()
    print("회원 수정 완료!")

def delete_member():
    '''회원 삭제'''
    conn = getconn()
    cur = conn.cursor()
    # 기본키로 삭제할 것!
    sql = "DELETE FROM member WHERE m_id = ?"
    cur.execute(sql, ('m1001',)) #튜플이므로 콤마 사용할 것!
    conn.commit()
    print("회원 삭제 완료!")  


# create_table()
# insert_member()
# select_one()
# update_member()
# delete_member()
select_all()