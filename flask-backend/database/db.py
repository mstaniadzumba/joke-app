import sqlite3

DB_NAME = 'jokes.db'

def init_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS jokes(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
            setup TEXT NOT NULL,
            punchline TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_joke(setup, punchline):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO jokes (setup, punchline) VALUES (?, ?)", (setup, punchline))
    conn.commit()
    conn.close()