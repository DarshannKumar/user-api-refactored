import sqlite3
import os

db_path = os.path.abspath("users.db")
print(f"📦 Creating database at: {db_path}")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

cursor.execute("INSERT INTO users (name, email, password) VALUES ('John Doe', 'john@example.com', 'password123')")
cursor.execute("INSERT INTO users (name, email, password) VALUES ('Jane Smith', 'jane@example.com', 'secret456')")
cursor.execute("INSERT INTO users (name, email, password) VALUES ('Bob Johnson', 'bob@example.com', 'qwerty789')")

conn.commit()
conn.close()

print("✅ Table 'users' created with 3 sample users.")
