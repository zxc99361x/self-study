import sqlite3
conn=sqlite3.connect('test.sqlite')

conn.execute(f"UPDATE contact SET name='{'Ken'}' WHERE id ={1}")
conn.commit()
conn.close()
