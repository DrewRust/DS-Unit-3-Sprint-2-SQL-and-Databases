import os
import sqlite3
import psycopg2
import pandas as pd
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
postGres_cursor2 = conn.cursor()


read_titanic = pd.read_csv (r'titanic.csv', nrows=20)
# print(read_titanic.columns)
print(read_titanic.shape)
# # print(read_titanic.head(20))
print(read_titanic.dtypes)
# print(read_titanic['Name'].head(5))


create_titanic_table_query = '''
CREATE TABLE IF NOT EXISTS titanic (
    id SERIAL PRIMARY KEY,
    survived INT,
	name VARCHAR(60),
	sex VARCHAR(10),
	age REAL,
	fare REAL,
	pclass INT, 
	siblings_spouses_aboard INT,
	parents_children_aboard INT
)
'''

postGres_cursor2.execute(create_titanic_table_query)
conn.commit()

def insertVaribleIntoTable(id, survived, name, sex, age, fare, pclass, siblings_spouses_aboard, parents_children_aboard):
    sqlite_insert_with_param = '''
    INSERT INTO titanic
    (id, survived, name, sex, age, fare, pclass, siblings_spouses_aboard, parents_children_aboard)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''
    data_tuple = (id, survived, name, sex, age, fare, pclass, siblings_spouses_aboard, parents_children_aboard)
    postGres_cursor2.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()

# THIS WORKS! Still need to debug why it won't run the function above but should work!
for ind in read_titanic.index:
    x = 1
    print(
        x, 
        read_titanic['Survived'][ind], 
        read_titanic['Name'][ind], 
        read_titanic['Sex'][ind], 
        read_titanic['Age'][ind], 
        read_titanic['Fare'][ind], 
        read_titanic['Pclass'][ind], 
        read_titanic["Siblings/Spouses Aboard"][ind], 
        read_titanic["Parents/Children Aboard"][ind]
        )
    # insertVaribleIntoTable(
    #     x, 
    #     read_titanic['Survived'][ind], 
    #     read_titanic['Name'][ind], 
    #     read_titanic['Sex'][ind], 
    #     read_titanic['Age'][ind], 
    #     read_titanic['Fare'][ind], 
    #     read_titanic['Pclass'][ind], 
    #     read_titanic["Siblings/Spouses Aboard"][ind], 
    #     read_titanic["Parents/Children Aboard"][ind]
    #     )
postGres_cursor2.close()