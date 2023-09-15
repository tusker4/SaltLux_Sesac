from tkinter import *
import pymysql

# 0. 전역변수 선언부
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

#  1. 데이터 베이스 연결 (pymysql)
conn = pymysql.connect(host='127.0.0.1', user='root', password='0000',
                       db='hanbitDB', charset='utf8')

#  2. 커서생성
cur = conn.cursor()

while (True):
    data1 = input("사용자 ID ==> ")
    if data1 == "":
        break;
    data2 = input("사용자 이름 ==> ")
    data3 = input("사용자 이메일 ==> ")
    data4 = input("사용자 출생년도 ==> ")
    sql = "INSERT INTO usertable VALUES('" + data1 + \
        "','" + data2 + "','" + data3 + "'," + data4 + ")"
    cur.execute(sql)


# 3. 테이블 생성
# cur.execute(
#     "CREATE TABLE IF NOT EXISTS userTable (id char(4), userName char(15), email char(20), birthYear int)")

# 4. 데이터 입력
# cur.execute(
#     "INSERT INTO userTable VALUES('john', 'John Bann', 'john@naver.com', 1990)")
# cur.execute(
#     "INSERT INTO userTable VALUES('kim', 'kim chi', 'kim@daum.net', 1992)")
# cur.execute(
#     "INSERT INTO userTable VALUES('sam', 'strong sam', 'sam@naver.com', 1933)")

# 5. 입력데이터 저장
conn.commit()
# 6. 닫기
conn.close()
