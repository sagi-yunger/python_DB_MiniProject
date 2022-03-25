
import re
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
    html+='<br/> <a href="/">Back home</a> <br/> </ul></body></html>'
    return f'{html}'

@app.route('/add', methods=['GET','POST']) ##page to add new item
def add():
    if request.method == 'POST':
        data = request.form['name']
        data2 = request.form['catagory']
        data3 = request.form['quantity']
        data4 = request.form['price']
        print(data,data2,data3,data4)
        item = add_item(data,data2,data3,data4,Today)
        return f'{item}  <br/> <a href="/add">Back to add</a> <br/> <a href="/">Back home</a>'
             # return render_template('add.html', data=data)
    return render_template('add.html')



@app.route('/price_change', methods=['GET','POST']) ##page to change price of an item
def price_change():
    if request.method == 'POST':
        data = request.form['name']
        data2 = request.form['price']
        print(data,data2)
        item = price_change_by_name(data,data2)
        return f'{item}  <br/> <a href="/price_change">Back to price change</a> <br/> <a href="/">Back home</a>'
    return render_template('price_change.html')

@app.route('/quantity_change', methods=['GET','POST']) ##page to change quantity of an item
def quantity_change():
    if request.method == 'POST':
        data = request.form['name']
        data2 = request.form['quantity']
        print(data,data2)
        item = quantity_change_by_name(data,data2)
        return f'{item}  <br/> <a href="/quantity_change">Back to quantity change</a> <br/> <a href="/">Back home</a>'
    return render_template('quantity_change.html')

@app.route('/category_change', methods=['GET','POST']) ##page to change quantity of an item
def category_change():
    if request.method == 'POST':
        data = request.form['name']
        data2 = request.form['category']
        print(data,data2)
        item = category_change_by_name(data,data2)
        return f'{item}  <br/> <a href="/category_change">Back to category change</a> <br/> <a href="/">Back home</a>'
    return render_template('category_change.html')

@app.route('/name_change', methods=['GET','POST']) ##page to change quantity of an item
def name_change():
    if request.method == 'POST':
        data = request.form['name']
        data2 = request.form['new_name']
        print(data,data2)
        item = change_item_name(data,data2)
        return f'{item}  <br/> <a href="/name_change">Back to name change</a> <br/> <a href="/">Back home</a>'
    return render_template('name_change.html')

@app.route('/del', methods=['GET','POST']) ##page to change quantity of an item
def delete_item():
    if request.method == 'POST':
        data = request.form['name']
        print(data)
        item = delete_by_name(data)
        return f'{item}  <br/> <a href="/del">Back to delete item</a> <br/> <a href="/">Back home</a>'
    return render_template('delete_item.html')

@app.route('/highest') ##page to show one or a list of items with the highest quantity from the DB

def highest():
    html="<html><body><ul>"  
    high = highest_quantity()
    for line in high:
        html+=f"<li>{line}</li>"
    html+='<br/> <a href="/">Back home</a> <br/> </ul></body></html>'
    return f'{html}'

@app.route('/lowest') ##page to show one or a list of items with the lowest quantity from the DB
def lowest():
    html="<html><body><ul>"  
    lwst = lowest_quantity()
    for line in lwst:
        html+=f"<li>{line}</li>"
    html+='<br/> <a href="/">Back home</a> <br/> </ul></body></html>'
    return f'{html}'

@app.route('/sort') ##page to show list from the DB sorted by price in a descending order
def sort_by_price():
    html="<html><body><ul>" 
    srt = sort_by_price_desc() 
    for line in srt:
        html+=f"<li>{line}</li>"
    html+='<br/> <a href="/">Back home</a> <br/> </ul></body></html>'
    return f'{html}'

if __name__ == '__main__':
    app.run(debug=True)

