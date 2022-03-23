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
    query = f"SELECT * FROM Inventory"
    data = cur.execute(query).fetchall()
    print(f"{data}")
    return data


def is_exist(item):
    """
    this function chack if an object exist in the DB and return True or False.
    IN: an object to check if exist in DB
    TYPE:
    OUT: True or False
    TYPE: bool
    """
    con = set_sql_connect()
    cur = set_sql_curser(con)
    query = f"SELECT * FROM Inventory"
    data = cur.execute(query).fetchall()
    sql_close(con)
    for row in data:
        if item in row:
            print(f"{item} already exist")
            return True
    print(f"no {item} in db")
    return False

def add_item(Item, catagory , quantity , price , date):
    """
    This function inserts a new user into an existing database, once validating that the user or email doesnt exist
    """
    print("in add")
    con = set_sql_connect() ## CREATE CONNECTION
    cur = set_sql_curser(con) ## CREATE CURSER
    if not is_exist(Item): ## is exist validation
        query = "INSERT INTO Inventory ('Item', 'Category', 'Quantity', 'Price', 'Date') VALUES (?,?,?,?,?)" ## PREPARED STATEMENT
        cur.execute(query, (Item, catagory , quantity , price , date)) ## PREPARED STATEMENT
        print(f"New item has been added with values of: {Item, catagory , quantity , price , date}")
    else:
        print("item already exists")
    sql_close(con)

def sql_del(item):
    	## delete values from a specific ID (deletes a row)
    con = set_sql_connect() ## CREATE CONNECTION
    cur = set_sql_curser(con) ## CREATE CURSER
    print(type(item))
    query = "DELETE FROM Inventory WHERE Item=?"
    try:
        cur.execute(query, (item,))
        print(f"item {item} had been deleted")
    except IOError as e:
        raise str(e)
    sql_close(con)

x = datetime.datetime.now()

Today = x.strftime("%m/%d/%Y")

def price_change_by_name(Item, price):
    	##check if item exist and update the price of a specific Item by name.
    con = set_sql_connect() ## CREATE CONNECTION
    cur = set_sql_curser(con) ## CREATE CURSER
    if is_exist(Item): ## is exist validation
        query = "UPDATE Inventory SET Price=? WHERE Item=?"
        cur.execute(query, (price, Item))
        print(f"item {Item} price had been updated with value of: {price}")
    else:
        print(f"{Item} does not exist")    
    sql_close(con)

def quantity_change_by_name(Item, Quantity):
    	##check if item exist and update the Quantity of a specific Item by name.
    con = set_sql_connect() ## CREATE CONNECTION
    cur = set_sql_curser(con) ## CREATE CURSER
    if is_exist(Item): ## is exist validation
        query = "UPDATE Inventory SET Quantity=? WHERE Item=?"
        cur.execute(query, (Quantity, Item))
        print(f"item {Item} Quantity had been updated with value of: {Quantity}")
    else:
        print(f"{Item} does not exist")   
    sql_close(con)

def category_change_by_name(Item, Category):
    	##check if item exist and update the Category of a specific Item by name.
    con = set_sql_connect() ## CREATE CONNECTION
    cur = set_sql_curser(con) ## CREATE CURSER
    if is_exist(Item): ## is exist validation
        query = "UPDATE Inventory SET Category=? WHERE Item=?"
        cur.execute(query, (Category, Item))
        print(f"item {Item} Category had been updated with value of: {Category}")
    else:
        print(f"{Item} does not exist")   
    sql_close(con)

def change_name(Item, name):
    	##check if item exist and change item name.
    con = set_sql_connect() ## CREATE CONNECTION
    cur = set_sql_curser(con) ## CREATE CURSER
    if is_exist(Item): ## is exist validation
        query = "UPDATE Inventory SET Item=? WHERE Item=?"
        cur.execute(query, (name, Item))
        print(f"item {Item} name had been changed to: {name}")
    else:
        print(f"{Item} does not exist")   
    sql_close(con)

def highest_quantity():
    con = set_sql_connect() ## CREATE CONNECTION
    cur = set_sql_curser(con) ## CREATE CURSER
    query = "SELECT * FROM Inventory WHERE Quantity = (SELECT Max(Quantity) FROM Inventory)"
    high = cur.execute(query).fetchall()
    print(f"{high}")
    sql_close(con)
    return high


def lowest_quantity():
    con = set_sql_connect() ## CREATE CONNECTION
    cur = set_sql_curser(con) ## CREATE CURSER
    query = "SELECT * FROM Inventory WHERE Quantity = (SELECT Min(Quantity) FROM Inventory)"
    low = cur.execute(query).fetchall()
    print(f"{low}")
    sql_close(con)
    return low



def sort_by_price_desc():
    con = set_sql_connect() ## CREATE CONNECTION
    cur = set_sql_curser(con) ## CREATE CURSER
    query = f"SELECT * FROM Inventory ORDER BY Price DESC"
    data = cur.execute(query).fetchall()
    print(f"{data}")
    return data


def go():
    # con = set_sql_connect()
    # cur = set_sql_curser(con)
    # read_from_sql(cur)
    # sql_close(con)
    # exist = is_exist('Tent')
    # print(exist)
    # sql_del('cag')
    # add_item( 'bag' , 'Outdoors', '500', '45' , Today)
    # price_change_by_name('bag','30')
    # quantity_change_by_name('dag', '300')
    # category_change_by_name('bag', 'common tool')
    # change_name('dag', 'bag')
    # highest_quantity()
    # lowest_quantity()
    sort_by_price_desc()



go()