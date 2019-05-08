import sqlite3

connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()

sql = """DELETE FROM albums WHERE artist = 'John Doe'"""

cursor.execute(sql)
connection.commit()
