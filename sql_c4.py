import sqlite3
conn=sqlite3.connect('test.sqlite')

conn.execute(f"DELETE FROM contact WHERE id ={1}")

conn.commit()
conn.close()