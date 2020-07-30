#### imports
import os
import sqlite3
import psycopg2
import pandas as pd
from dotenv import load_dotenv

#### loading .env credentials
load_dotenv()

#### credentials 
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")

#### establish connection to sqlite
conn = psycopg2.connect(dbname=DB_NAME, 
                        user=DB_USER,
                        password=DB_PASS, 
                        host=DB_HOST)
#### create cursor object to connection
postGres_cursor2 = conn.cursor()

#### read in titanic csv
read_titanic = pd.read_csv (r'titanic.csv', nrows=20)

#### create empty SQL table if it doesn't already exist
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
#### point table columns to cursor object
postGres_cursor2.execute(create_titanic_table_query)
#### commit to table plus or postgreSql
conn.commit()
#### function to add individual passengers from csv inputs
def insertPassengerIntoTable(id, survived, name, sex, age, fare, pclass, siblings_spouses_aboard, parents_children_aboard):
    passenger = (id, survived, name, sex, age, fare, pclass, siblings_spouses_aboard, parents_children_aboard)

    insert_query = f''' INSERT INTO titanic 
        (id, survived, name, sex, age, fare, pclass, siblings_spouses_aboard, parents_children_aboard)
    VALUES
        {passenger}
    '''
    postGres_cursor2.execute(insert_query)

#### Calling the above function below for as many rows that are in the .csv file
#### x is to create id's for each passenger
x = 1
for ind in read_titanic.index:
    insertPassengerIntoTable(
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
    x += 1
conn.commit()
     
#### testing out the function it works!
#### insertVaribleIntoTable(2, 1, "Mr. George Smith", "female", 11, 56.5, 3, 6, 5)

#### close cursor and connection
postGres_cursor2.close()
conn.close()




