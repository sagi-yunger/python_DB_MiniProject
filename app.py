
from flask import Flask
from inventory_git import *

app = Flask(__name__)


@app.route('/')
def index():
    html ="""
    <html><body><ul>
    <h1>Hello Devops Class</h1> 
    <form action="/inventory" method="post" enctype="text/plain"> 
    <button>Inventory List</button>
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



if __name__ == '__main__':
    app.run(debug=True)

