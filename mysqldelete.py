import pymysql

conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',charset='utf8',db='pythondb')

with conn.cursor() as cursor:
    sql="delete from scores where ID =4"
    cursor.execute(sql)
    conn.commit()
    sql="select * from scores"   
    cursor.execute(sql)
    data=cursor.fetchall()
    print(data)

    conn.commit()    
conn.close()