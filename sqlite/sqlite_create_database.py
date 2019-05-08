import sqlite3

exist_error = "Base already exists!"
conn = sqlite3.connect("mydatabase.db")

cursor = conn.cursor()
try:
    cursor.execute("""CREATE TABLE albums(title text, artist text, release_date text, publisher text, media_type text)""")
except Exception:
    print(exist_error)
