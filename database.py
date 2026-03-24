import sqlite3

conn = sqlite3.connect("echo.db", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emotions (
        username TEXT,
        text TEXT,
        emotion TEXT
    )
    """)
    conn.commit()

def add_user(username, password):
    cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()

def validate_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return cursor.fetchone() is not None

def save_emotion(username, text, emotion):
    cursor.execute("INSERT INTO emotions VALUES (?, ?, ?)", (username, text, emotion))
    conn.commit()

def get_emotions(username):
    cursor.execute("SELECT emotion FROM emotions WHERE username=?", (username,))
    return cursor.fetchall()