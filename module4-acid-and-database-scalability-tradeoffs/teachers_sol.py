
import os
import sqlite3
import psycopg2
import pandas as pd
from dotenv import load_dotenv
from psycopg2.extras import execute_values


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
print(conn)
print(postGres_cursor2)


read_titanic = pd.read_csv(r'titanic.csv')
print(read_titanic.shape)



sql = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived boolean, 
    pclass int4,
    full_name text,
    gender text,
    age int4,
    sib_spouse_count int4,
    parent_child_count int4,
    fare float8
);
"""
postGres_cursor2.execute(sql)
print(read_titanic.columns.tolist())


read_titanic["Survived"] = read_titanic["Survived"].values.astype(bool) 
read_titanic = read_titanic.astype("object") 

list_of_tuples = list(read_titanic.to_records(index=False))

insertion_query = f"INSERT INTO passengers (survived, pclass, full_name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(postGres_cursor2, insertion_query, list_of_tuples) 

conn.commit() 
print('Titanic Data successfully saved to Postgres!')


postGres_cursor2.close()
conn.close()