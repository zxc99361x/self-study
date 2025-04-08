import pymysql

conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',charset='utf8',db='pythondb')

with conn.cursor() as cursor:
    sql="select * from scores"
    cursor.execute(sql)
    datas=cursor.fetchall()
    print(datas)
    print('-'*30)
    sql="select * from scores"
    cursor.execute(sql)
    datas=cursor.fetchone()
    print(datas)

    conn.commit()    
conn.close()