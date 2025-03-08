import sqlite3

DATABASE = 'database.db'

def create_books_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            price INTEGER,
            arrival TEXT
        )
    ''')
    conn.commit()
    conn.close()