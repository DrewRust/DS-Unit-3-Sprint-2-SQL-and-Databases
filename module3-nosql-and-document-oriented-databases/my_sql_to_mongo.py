import sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_cursor = sl_conn.cursor()
count = sl_cursor.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchall()
# print(count)
# print("\n")

# # Will print a list of tuples
# characters = sl_cursor.execute('SELECT * FROM charactercreator_character LIMIT 10;').fetchall()
# print(characters)
# print("\n")

# count2 = sl_cursor.execute('SELECT COUNT(*) FROM armory_item;').fetchall()
# print(count2)
# print("\n")

# # Will print a list of tuples
# armory_items = sl_cursor.execute('SELECT * FROM armory_item LIMIT 10;').fetchall()
# print(armory_items)
# print("\n")

# https://stackoverflow.com/questions/28755505/how-to-convert-sql-query-results-into-a-python-dictionary

def put_sqltable_in_dict():
    qu= 'SELECT * FROM armory_item'
    armory_it = sl_cursor.execute(qu)
    desc = armory_it.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in armory_it.fetchall()]
    return data

dictionary = put_sqltable_in_dict()
print(dictionary)







