import sqlite3

CONN = sqlite3.connect('recipe_book.db')
CURSOR = CONN.cursor()
