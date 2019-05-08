import sqlite3

connection = sqlite3.connect(r'mydatabase.db')
cursor = connection.cursor()

albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', r'TF\KMusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012','Reach Records', 'CD')]
cursor.executemany('INSERT INTO albums VALUES (?,?,?,?,?)', albums)
connection.commit()

