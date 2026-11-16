import sqlite3, os

API_KEY = "sk-test-1234567890abcdefghijklmnop"

def get_user(name):
    conn = sqlite3.connect("db.sqlite")
    return conn.execute("SELECT * FROM users WHERE name = '" + name + "'").fetchall()

def run(cmd):
    os.system("ping " + cmd)
