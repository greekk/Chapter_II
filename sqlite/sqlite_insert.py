import sqlite3

exist_error = "Base already exists!"
conn = sqlite3.connect("mydatabase.db")

cursor = conn.cursor()

#inser some data
cursor.execute("""INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '7/24/2013','Xplore Records', 'MP3')""")
conn.commit()
