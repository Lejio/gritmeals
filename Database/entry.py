import sqlite3

conn = sqlite3.connect('gritmeals.db')

c = conn.cursor()

try:
    cmd = """CREATE TABLE IF NOT EXISTS subscribers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(320));"""
    c.execute(cmd)
    print("Creating")
except:
    print("Skipped")
    pass

c.execute("""INSERT INTO subscribers VALUES(1,"pranavv1@umbc.edu") """)

conn.commit()

conn.close()
