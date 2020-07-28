# app/mongo_queries.py

import os
import json
import pymongo
from dotenv import load_dotenv
from pdb import set_trace as breakpoint
from my_sql_to_mongo import put_sqltable_in_dict

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/drew_rust?retryWrites=true&w=majority"
print("\n")
print("----------------")
print("\n")
print("URI:", connection_uri)
print("\n")
client = pymongo.MongoClient(connection_uri)
print("----------------")
print("\n")
print("CLIENT:", type(client), client)
print("\n")
# print("These are your database names: \n")
# print(client.list_database_names())
# print("\n")

# db = client.sample_analytics
# print("These are the list of collection names: \n")
# print(db.list_collection_names())
# print("\n")
# customers = db.customers
# print("These are how many customer documents we have: \n")
# print(customers.count_documents({}))
# print("\n")

#
#### Write JSON Data from RPG DB to MongoDB
#
# Read the JSON file 
# (copied from: 
# https://raw.githubusercontent.com/LambdaSchool/Django-RPG/master/testdata.json)

# with open('test_data_json.txt') as json_file:
#     rpg_data = json.load(json_file)

# # Create an rpg_data database
my_db = client.rpg_data

# importing this from the other file my_sql_to_mongo
dictionary = put_sqltable_in_dict()
# print(dictionary)

# create armory_items table on mongodb
armory_table = my_db.armory_collection
armory_table.insert_many(dictionary)
print(armory_table.count_documents({}))

# # Create a characters collection in the rpg_data DB
# character_table = my_db.characters

# # Insert the JSON data into characters collection
# character_table.insert_many(rpg_data)
# print(character_table.count_documents({}))


# breakpoint()

# (Pdb) customers = db.customers
# (Pdb) dir(customers)
# (Pdb) customers.count_documents({})

# (Pdb) all_customers = customers.find()
# (Pdb) df = pd.DataFrame(all_customers)
# (Pdb) df.shape
# (501, 10)
# (Pdb) df.tail()


# (Pdb) customers.find_one()

# crud - acronymn for create the data, read the data etc. 