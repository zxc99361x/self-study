import sqlite3
conn=sqlite3.connect('test.sqlite')
cursor=conn.cursor()

sqlstr='''Create TABLE IF NOT EXISTS contact \
("id" INTEGER PRIMARY KEY NOT NULL,
"name" TEXT NOT NULL,
"tel" TEXT NOT NULL)
'''
cursor.execute(sqlstr)

conn.commit()
conn.close()