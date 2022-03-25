
from flask import Flask, render_template, request
from inventory_git import *
import datetime

app = Flask(__name__)

x = datetime.datetime.now() ## store todays full date and time in var x with use of datetime module 
Today = x.strftime("%m//%d//%Y") ## make var x only date in format MM/DD/YYYY with use of datetime module and store it in Today var 

@app.route('/') ##home page
def index():
    html ="""
    <html><body><ul>
    <h1>Hello Devops Class</h1> 
    <form action="/inventory" method="get" enctype="text/plain"> 
    <button>Inventory List</button>
    </form>
    <form action="/add" method="get" enctype="text/plain"> 
    <button>add to List</button>
    </form>
    <form action="/price_change" method="get" enctype="text/plain"> 
    <button>change item price</button>
    </form>
    <form action="/quantity_change" method="get" enctype="text/plain"> 
    <button>change item quantity</button>
    </form>
    <form action="/category_change" method="get" enctype="text/plain"> 
    <button>change item category</button>
    </form>
    <form action="/name_change" method="get" enctype="text/plain"> 
    <button>change item name</button>
    </form>
    <form action="/del" method="get" enctype="text/plain"> 
    <button>delete from List</button>
    </form>
    <form action="/highest" method="get" enctype="text/plain"> 
    <button>highest quantity from List</button>
    </form>
    <form action="/lowest" method="get" enctype="text/plain"> 
    <button>lowest quantity from List</button>
    </form>
    <form action="/sort" method="get" enctype="text/plain"> 
    <button>List sorted by price</button>
    </form>
"""
    html+="</ul></body></html>"
    return f'{html}'

@app.route('/user/<name>') ## page to say hello
def user(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/inventory') ##page to show list from the DB
def inventory():
    html="<html><body><ul>"  
    dct = read_from_sql()
    for line in dct:
        html+=f"<li>{line}</li>"
    html+="</ul></body></html>"
    return f'{html}'

@app.route('/add') ##page to add new item
def loadform():
    return render_template('add.html')

    # result = add_item('rabbit', 'pet', '4', '40', Today )
    # return f'{result}'
@app.route('/add', methods=['POST']) ##page to add new item
def add():
    data = request.form['insert-new-item']
    return data
    
    # result = add_item('rabbit', 'pet', '4', '40', Today )
    # return f'{result}'

@app.route('/price_change') ##page to change price of an item
def price_change():
    result = price_change_by_name('cat', '32')
    return f'{result}'

@app.route('/quantity_change') ##page to change quantity of an item
def quantity_change():
    result = quantity_change_by_name('Xbox', '2000')
    return f'{result}'

@app.route('/category_change') ##page to change category of an item
def category_change():
    result = category_change_by_name('Xbox', 'gaming consoles')
    return f'{result}'

@app.route('/name_change') ##page to change name of an existing item (the new name most be non existing)
def name_change():
    result = change_item_name('rabbit', 'duck')
    return f'{result}'
    
@app.route('/del') ##page to remove an item by name
def delete():
    result = delete_by_name('rabbit')
    return f'{result}'

@app.route('/highest') ##page to show one or a list of items with the highest quantity from the DB

def highest():
    html="<html><body><ul>"  
    high = highest_quantity()
    for line in high:
        html+=f"<li>{line}</li>"
    html+="</ul></body></html>"
    return f'{html}'

@app.route('/lowest') ##page to show one or a list of items with the lowest quantity from the DB
def lowest():
    html="<html><body><ul>"  
    lwst = lowest_quantity()
    for line in lwst:
        html+=f"<li>{line}</li>"
    html+="</ul></body></html>"
    return f'{html}'

@app.route('/sort') ##page to show list from the DB sorted by price in a descending order
def sort_by_price():
    html="<html><body><ul>" 
    srt = sort_by_price_desc() 
    for line in srt:
        html+=f"<li>{line}</li>"
    html+="</ul></body></html>"
    return f'{html}'

if __name__ == '__main__':
    app.run(debug=True)

