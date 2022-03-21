import sqlite3
import datetime



PATH = "C:\\sagi\\jupyter-adi\\sql\\GIT\\"
FILENAME = "Inventory.db"
FILE = PATH + FILENAME

def set_sql_connect():
    """
    this function connect to a DB with sqlite3 module and then return a connection object.
    """
    con = sqlite3.connect(FILE)
    print(f"connected")
    return con

def set_sql_curser(con):
    """
    this function create a curser object after a connection has been made with set_sql_connect.
    IN: con
    TYPE: sqlite3.connect
    OUT: cur
    TYPE: sqlite3.connect.curser
    """
    cur = sqlite3.Cursor(con)
    print(f"curser up")
    return cur

def sql_close(con):
    """
    this function commit the changes that been made to the DB via open connection and then close the connection to the DB.
    IN: con
    TYPE: sqlite3.connect
    """
    con.commit()
    print(f"commited change in DB")
    con.close()
    print(f"closed DB")

def read_from_sql(cur):
    """
    this function read and retrive all the informtion from the DB
    OUT: Values from DB as LIST
    TYPE: LIST
    """
    query = "SELECT * FROM Inventory"
    data = cur.execute(query).fetchall()
    print(f"{data}")
    return data






con = set_sql_connect()
cur = set_sql_curser(con)
read_from_sql(cur)
sql_close(con)