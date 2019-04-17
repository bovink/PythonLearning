import pymysql

db = pymysql.connect(host='localhost', user='root', passwd='A1UH6kDp0Fxc', db='happybook', charset='utf8')

cursor = db.cursor()

sql = """INSERT INTO happybook.books(title, author) values ('go','sssss')"""

try:
    # 执行sql语句
    cursor.execute(sql)
    db.commit()
except:
    print('hello')

db.close()