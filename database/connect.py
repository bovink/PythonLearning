import pymysql

# 服务器、用户名、密码、数据库名
db = pymysql.connect("localhost", "root", "A1UH6kDp0Fxc", "happybook")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("database version : %s" % data)

db.close()