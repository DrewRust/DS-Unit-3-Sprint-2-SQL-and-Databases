import sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_cursor = sl_conn.cursor()

#### Will print the total count from charactercreator_character
# count = sl_cursor.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchall()
# print(count)
# print("\n")

#### Will print a list of tuples from character_creator
# characters = sl_cursor.execute('SELECT * FROM charactercreator_character LIMIT 10;').fetchall()
# print(characters)
# print("\n")

#### Trying out what I'll be running below
# armory_items = sl_cursor.execute('SELECT * FROM armory_item LIMIT 10;').fetchall()
# print(armory_items)
# print("\n")

#### Will print how many entries from armory_item
# count2 = sl_cursor.execute('SELECT COUNT(*) FROM armory_item;').fetchall()
# print(count2)
# print("\n")


#### https://stackoverflow.com/questions/28755505/how-to-convert-sql-query-results-into-a-python-dictionary
#### https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-description.html
#### syntax: tuples = cursor.description
#### desc = armory_it.description

#### query
qu= 'SELECT * FROM armory_item'

def put_sqltable_in_dict(insert_query):
    armory_it = sl_cursor.execute(insert_query)
    desc = armory_it.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in armory_it.fetchall()]
    return data

#### Calling the function above 
# dictionary = put_sqltable_in_dict()
# print(dictionary)


#### Will print the mage's table (id, has_pet (true or false), mana_count)
query_mage = '''
SELECT * FROM charactercreator_mage;
'''
sl_cursor.execute(query_mage)
result_mage = sl_cursor.execute(query_mage).fetchall()
print(result_mage)




