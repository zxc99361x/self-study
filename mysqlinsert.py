import pymysql

conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',charset='utf8',db='pythondb')

with conn.cursor() as cursor:
    sql="""
    insert into scores(Nmae,Chinese,English,Math) values
        ('李大毛',95,92,80),
        ('林小明',82,83,61),
        ('黃小英',74,53,71),
        ('柳大樹',86,87,89),
        ('和美麗',89,73,95)
    """
    cursor.execute(sql)
    conn.commit()    
conn.close()