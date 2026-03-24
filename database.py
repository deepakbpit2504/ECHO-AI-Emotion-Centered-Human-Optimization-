import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cur = conn.cursor()

def init_db():
    cur.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS emotions(username TEXT, text TEXT, emotion TEXT)")
    conn.commit()

init_db()

def add_user(username, password):
    cur.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()

def validate_user(username, password):
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return cur.fetchone() is not None

def save_emotion(username, text, emotion):
    cur.execute("INSERT INTO emotions VALUES (?, ?, ?)", (username, text, emotion))
    conn.commit()

def get_emotions(username):
    cur.execute("SELECT emotion FROM emotions WHERE username=?", (username,))
    return cur.fetchall()