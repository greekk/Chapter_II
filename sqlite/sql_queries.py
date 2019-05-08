import sqlite3

select_all_artist = "SELECT * FROM albums WHERE artist=?"
select_all = "SELECT * FROM albums"
select_all_rows = "SELECT rowid,* FROM albums ORDER BY artist"
select_with_like = "SELECT * FROM albums WHERE title LIKE 'The%'"

with sqlite3.connect("mydatabase.db") as conn:
    #conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(select_all_artist, [('Red')])
    print(cursor.fetchone())#fetchall()

    print("\nHere's a listing of all records without order:\n")
    cursor.execute(select_all)
    result = cursor.fetchall()
    for item in result:
        print(item)

    print("\nHere's a listing of all the records in the table:\n")
    for row in cursor.execute(select_all_rows):
        print(row)

    print("\nResults from a LIKE query:\n")
    cursor.execute(select_with_like)
    result = cursor.fetchall()
    for item in result:
        print(item)




