# from the past video
# 1. establish connection
# 2. create cursor
# 3. execute query
# 4. get results.

import os
import sqlite3
import psycopg2
from dotenv import load_dotenv

# Load .env file and save credentials
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")

conn = psycopg2.connect(dbname=DB_NAME, 
                        user=DB_USER,
                        password=DB_PASS, 
                        host=DB_HOST)
postGres_cursor = conn.cursor()

# print(postGres_cursor)
# print(conn)
postGres_cursor.execute('SELECT * FROM playground;')
print("\n")
print(postGres_cursor.fetchall())
print("\n")

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_cursor = sl_conn.cursor()
count = sl_cursor.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchall()
print(count)
print("\n")

# Will print a list of tuples
characters = sl_cursor.execute('SELECT * FROM charactercreator_character LIMIT 10;').fetchall()
print(characters)

# you need IF NOT EXIST so it doesn't keep creating it
create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	level INT,
	exp INT,
	hp INT,
	strength INT, 
	intelligence INT,
	dexterity INT,
	wisdom INT
)
'''

postGres_cursor.execute(create_character_table_query)
conn.commit()

############## Insert Character Data in POSTGRES ##############

for character in characters:

    insert_query = f''' INSERT INTO rpg_characters 
        (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES
        {character}
    '''
    postGres_cursor.execute(insert_query)

conn.commit()








# from the current video not loaded yet
# import os   
# import psycopg2
# from dotenv import load_dotenv

# # Load .env file and save credentials
# load_dotenv()

# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASS = os.getenv("DB_PASS")
# DB_HOST = os.getenv("DB_HOST")

# # Connect to ElephantSQL-hosted PostgreSQL
# conn = psycopg2.connect(dbname=DB_NAME, 
#                         user=DB_USER,
#                         password=DB_PASS, 
#                         host=DB_HOST)

# # A "cursor", a structure to iterate over db records to perform queries
# cursor = conn.cursor()

# # An example query
# cursor.execute('SELECT * from test_table;')

# # Note - nothing happened yet! We need to actually *fetch* from the cursor
# results = cursor.fetchall()
# # print(results)


# ############## Connect to SQLite3 DB for RPG data ##############

# import sqlite3

# sl_conn = sqlite3.connect("rpg_db.sqlite3")
# sl_cursor = sl_conn.cursor()
# characters = sl_cursor.execute('SELECT * FROM charactercreator_character LIMIT 10').fetchall()
# print(characters)

# ############## Create Character Table in PostGRES ##############

# create_character_table_query = '''
# CREATE TABLE IF NOT EXISTS rpg_characters (
#     character_id SERIAL PRIMARY KEY,
# 	name VARCHAR(30),
# 	level INT,
# 	exp INT,
# 	hp INT,
# 	strength INT, 
# 	intelligence INT,
# 	dexterity INT,
# 	wisdom INT
# )
# '''

# cursor.execute(create_character_table_query)
# conn.commit()

# ############## Insert Character Data in POSTGRES ##############

# for character in characters:

#     insert_query = f''' INSERT INTO rpg_characters 
#         (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES
#         {character}
#     '''
#     cursor.execute(insert_query)

# conn.commit()