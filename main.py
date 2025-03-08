from . import app
from flask import render_template,request,redirect,url_for
import sqlite3
DATABASE = 'database.db'

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute('SELECT * FROM books')
    db_books = cur.fetchall()
    con.close()
 
    books = []
    for book in db_books:
        books.append({
            'title': book[1],
            'author': book[2],
            'price': book[3],
            'arrival': book[4]
        })

    return render_template(
        'index.html',
        books=books
    )

    # books = [
    #     {'title': '国宝',
    #     'author': '吉田修一',
    #     'price': 2300,
    #     'arrival': '2020-10-01'},
    #     {'title': 'サピエンス全史',
    #     'author': 'ユヴァル・ノア・ハラリ',
    #     'price': 990,
    #     'arrival': '2022-01-01'},
    #     {'title': '日本人への遺言',
    #     'author': '司馬遼太郎',
    #     'price': 650,
    #     'arrival': '1999-02-01'}
    # ]
    # books = []


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    author = request.form['author']
    price = request.form['price']
    arrival = request.form['arrival']

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute(
        'INSERT INTO books (title, author, price, arrival) VALUES(?, ?, ?, ?)',
        (title, author, price, arrival))
    con.commit()
    con.close()
    return redirect(url_for('index'))
