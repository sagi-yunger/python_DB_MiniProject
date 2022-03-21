import sqlite3
import datetime



PATH = "C:\\sagi\\jupyter-adi\\sql\\GIT\\"
FILENAME = "Inventory.db"
FILE = PATH + FILENAME

def set_sql_connect():
    con = sqlite3.connect(FILE)
    print(f"connected")
    return con

def set_sql_curser(con):
    cur = sqlite3.Cursor(con)
    print(f"curser up")
    return cur

def sql_close(con):
    con.commit()
    print(f"commited change in DB")
    con.close()
    print(f"closed DB")

def read_from_sql(cur):
    query = "SELECT * FROM Inventory"
    data = cur.execute(query).fetchall()
    print(f"{data}")






con = set_sql_connect()
cur = set_sql_curser(con)
read_from_sql(cur)
sql_close(con)