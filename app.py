from flask import Flask
from inventory_git import *

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Devops Class</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/inventory/')
def inventory():
    return f'{read_from_sql()}'

if __name__ == '__main__':
    app.run(debug=True)

