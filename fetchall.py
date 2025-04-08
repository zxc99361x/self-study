import sqlite3
conn=sqlite3.connect('test.sqlite')
cursor=conn.execute('select *from contact')
rows=cursor.fetchall()
print(rows)
for row in rows:
    print(row[0])