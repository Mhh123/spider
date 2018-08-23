import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='weisuo', charset='utf8')

cursor = conn.cursor()

item = {
    'name': '王宝强', 
    'age': 36,
    'love': 'GreenHat'
}

sql = 'insert into user(name, age, love) values("%s","%s","%s")' % (item['name'], item['age'], item['love'])

try:
    cursor.execute(sql)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()
finally:
    conn.close()