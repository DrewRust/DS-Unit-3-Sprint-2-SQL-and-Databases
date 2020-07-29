import os
import json
import pymongo
from dotenv import load_dotenv
from pdb import set_trace as breakpoint
#### importing from my_sql_to_mong.py the function put_sqltable_in_dict
from my_sql_to_mongo import put_sqltable_in_dict

#### loading .env file and credentials for MongoDB
load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

#### Connecting to MongoDB
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

#### This prints clients from a sample db
# print("These are your database names: \n")
# print(client.list_database_names())
# print("\n")

#### This prints from the column sample_analytics
# db = client.sample_analytics
# print("These are the list of collection names: \n")
# print(db.list_collection_names())
# print("\n")

#### This prints from customers
# customers = db.customers
# print("These are how many customer documents we have: \n")
# print(customers.count_documents({}))
# print("\n")


#### Creates an rpg_data database called my_db
my_db = client.rpg_data



#### Characters ####

#### Write JSON Data from RPG DB to MongoDB
#### Read the JSON file 
#### (copied from: 
#### https://raw.githubusercontent.com/LambdaSchool/Django-RPG/master/testdata.json)

#### This uses the test_data_json.txt file and loads it into rpg_data
# with open('test_data_json.txt') as json_file:
#     rpg_data = json.load(json_file)

#### Create a "characters" collection in the rpg_data DB
# character_table = my_db.characters

#### Insert the JSON data into "characters" collection
# character_table.insert_many(rpg_data)
# print(character_table.count_documents({}))



#### armory_items ####
#### importing this from the other file my_sql_to_mongo

qu= 'SELECT * FROM armory_item'
dictionary = put_sqltable_in_dict(qu)
print(dictionary)

### create armory_items table on mongoDB
### it will show up as "armory_collection"

armory_table = my_db.armory_collection
armory_table.insert_many(dictionary)

### prints how many armory_table documents
print(armory_table.count_documents({}))




#### mage_characters ####
#### Will print the mage's table (id, has_pet (true or false), mana_count)
#### importing this from the other file my_sql_to_mongo
query_mage = '''
SELECT * FROM charactercreator_mage;
'''

dictionary2 = put_sqltable_in_dict(query_mage)
print(dictionary2)

mage_table = my_db.mage_collection
mage_table.insert_many(dictionary2)

#### prints how many mage_table documents
print(mage_table.count_documents({}))




#### Used to debug and run code in the terminal below live before the code finishes 
# breakpoint()

#### Examples of running code in the terminal below
#### (Pdb) is the indication of breakpoint 
#### (Pdb) customers = db.customers
#### (Pdb) dir(customers)
#### (Pdb) customers.count_documents({})

#### (Pdb) all_customers = customers.find()
#### (Pdb) df = pd.DataFrame(all_customers)
#### (Pdb) df.shape
#### (501, 10)
#### (Pdb) df.tail()


#### (Pdb) customers.find_one()

#### crud - acronymn for create the data, read the data, update, and delete the data