import pymysql
db = pymysql.connect('localhost', 'root', 'A1UH6kDp0Fxc', 'happybook',charset='utf8')

cursor = db.cursor()

sql = "SELECT * FROM happybook.books"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        title = row[0]
        author = row[1]
        clicktotal = row[2]
        print("title:%s,author:%s" % (author, clicktotal))
except:
    print('hello')

db.close()