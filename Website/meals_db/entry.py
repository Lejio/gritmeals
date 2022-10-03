import sqlite3

def create_connection():
    conn = sqlite3.connect('Database/gritmeals.db')

    c = conn.cursor()

    return c, conn


def create_table(c):
    try:
        cmd = """CREATE TABLE IF NOT EXISTS subscribers(
            email TEXT);"""
        c.execute(cmd)
        print("Creating")
    except:
        print("Skipped")
        pass

def insert_data(c, email):
    print(email)
    c.execute(f"""INSERT INTO subscribers VALUES("{email}") """)

def get_all_subs(c):

    return c.execute("""SELECT * FROM 'subscribers'""")


def save_session(conn):
    conn.commit()

    conn.close()
