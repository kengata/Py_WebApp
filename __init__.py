from flask import Flask
app = Flask(__name__)
from . import main

from . import db
db.create_books_table()