import sqlite3

con = sqlite3.connect('movies.db')

cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Movies
            """)