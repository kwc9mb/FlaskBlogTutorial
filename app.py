import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    return "<h1>Create a Post<\h1>"

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    return "<h1>Edit a Post<\h1>"

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    return

app.run(host="0.0.0.0", port=5001)