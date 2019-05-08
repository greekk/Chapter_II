import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = """UPDATE albums SET artist = 'Chuck Shuldiner' WHERE title = 'Until We Have Faces'"""

cursor.execute(sql)

conn.commit()
