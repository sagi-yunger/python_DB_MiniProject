
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
    <form action="/inventory" method="post" enctype="text/plain"> 
    <button>Inventory List</button>
    </form>
    <form action="/add" method="get" enctype="text/plain"> 
    <button>add to List</button>
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
def add(Today):
    result = add_item('cow','farm animal','100','1000',Today)
    return f'{result}'


if __name__ == '__main__':
    app.run(debug=True)

