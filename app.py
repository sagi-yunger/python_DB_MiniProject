
from flask import Flask
from inventory_git import *
import datetime

app = Flask(__name__)
x = datetime.datetime.now() ## store todays full date and time in var x with use of datetime module 
Today = x.strftime("%m//%d//%Y") ## make var x only date in format MM/DD/YYYY with use of datetime module and store it in Today var 

@app.route('/')
def index():
    html ="""
    <html><body><ul>
    <h1>Hello Devops Class</h1> 
    <form action="/inventory" method="get" enctype="text/plain"> 
    <button>Inventory List</button>
    </form>
    <form action="/add" method="post" enctype="text/plain"> 
    <button>add to List</button>
    </form>
    <form action="/del" method="get" enctype="text/plain"> 
    <button>delete from List</button>
    </form>
    <form action="/highest" method="get" enctype="text/plain"> 
    <button>highest from List</button>
    </form>
    <form action="/lowest" method="get" enctype="text/plain"> 
    <button>lowest from List</button>
    </form>
    <form action="/sort" method="get" enctype="text/plain"> 
    <button>List sorted by price</button>
    </form>
"""
    html+="</ul></body></html>"
    return f'{html}'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/inventory')
def inventory():
    html="<html><body><ul>"  
    dct = read_from_sql()
    for line in dct:
        html+=f"<li>{line}</li>"
    html+="</ul></body></html>"
    return f'{html}'

@app.route('/add')
def add():
    result = add_item('rabbit', 'pet', '4', '40', Today )
    return f'{result}'

@app.route('/del')
def delete():
    result = delete_by_name('rabbit')
    return f'{result}'

@app.route('/highest')
def highest():
    html="<html><body><ul>"  
    high = highest_quantity()
    html+=f"<li>{high}</li>"
    html+="</ul></body></html>"
    return f'{html}'

@app.route('/lowest')
def lowest():
    html="<html><body><ul>"  
    lwst = lowest_quantity()
    html+=f"<li>{lwst}</li>"
    html+="</ul></body></html>"
    return f'{html}'

@app.route('/sort')
def sort_by_price():
    html="<html><body><ul>"  
    srt = sort_by_price_desc()
    html+=f"<li>{srt}</li>"
    html+="</ul></body></html>"
    return f'{html}'

if __name__ == '__main__':
    app.run(debug=True)

