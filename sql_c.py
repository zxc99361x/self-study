import sqlite3
conn=sqlite3.connect('test.sqlite')
cursor=conn.cursor()

sqlstr='''Create TABLE IF NOT EXISTS table01 \
("id" INTEGER PRIMARY KEY NOT NULL,
"name" TEXT NOT NULL,
"tel" TEXT NOT NULL)
'''
cursor.execute(sqlstr)

sqlstr='insert into table01 values(1,"Divid","02-1234567")'
cursor.execute(sqlstr)
conn.commit()
conn.close()