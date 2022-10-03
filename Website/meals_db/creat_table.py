import sqlite3

conn = sqlite3.connect('data.db')

c = conn.cursor()

try:
    c.execute(""" CREATE TABLE subs(
        id INTEGER,
        email TEXT(40))""")
except:
    pass

conn.commit()

conn.close()
