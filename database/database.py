import sqlite3

conn = sqlite3.connect(
    "database/finmate.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(

id INTEGER PRIMARY KEY AUTOINCREMENT,

category TEXT,

amount REAL

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS budget(

id INTEGER PRIMARY KEY AUTOINCREMENT,

income REAL,

budget REAL

)
""")

conn.commit()