import sqlite3

from app.config import DATABASE_PATH

def connect() -> sqlite3.Connection:
    con = sqlite3.connect(DATABASE_PATH)
    con.execute("PRAGMA foreign_keys = ON")

    return con