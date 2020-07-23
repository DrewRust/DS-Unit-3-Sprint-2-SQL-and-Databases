import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')

# # How Many Unique Characters? (This works but complicated)
# curs_3 = conn.cursor()
# query_3 = '''
# SELECT character_id,
# name,
# level, 
# exp, 
# hp, 
# strength, 
# intelligence, 
# dexterity, 
# wisdom
# FROM charactercreator_character;
# '''
# curs_3.execute(query_3)
# result3 = curs_3.execute(query_3).fetchall()
# columns3 = list(map(lambda x:x[0], curs_3.description))
# df3 = pd.DataFrame(data=result3, columns=columns3)

# # Armory Item Count (This works but complicated)
# curs_4 = conn.cursor()
# query_4 = '''
# SELECT item_id,
# name,
# "value", 
# weight 
# FROM armory_item;
# '''
# curs_4.execute(query_4)
# result4 = curs_4.execute(query_4).fetchall()
# columns4 = list(map(lambda x:x[0], curs_4.description))
# df4 = pd.DataFrame(data=result4, columns=columns4)

# Character Count (A simpler way than above)
curs_1 = conn.cursor()
query_1 = '''
SELECT
	COUNT("name")
FROM
	charactercreator_character;
'''
curs_1.execute(query_1)
result1 = curs_1.execute(query_1).fetchall()


# Armory Item Count (A simpler way than above)
curs_2 = conn.cursor()
query_2 = '''
SELECT
	COUNT("name")
FROM
	armory_item;
'''
curs_2.execute(query_2)
result2 = curs_2.execute(query_2).fetchall()


# Thief Count
curs_5 = conn.cursor()
query_5 = '''
SELECT
	COUNT(character_ptr_id)
FROM
	charactercreator_thief;
'''
curs_5.execute(query_5)
result5 = curs_5.execute(query_5).fetchall()


# Cleric Count
curs_6 = conn.cursor()
query_6 = '''
SELECT
	COUNT(character_ptr_id)
FROM
	charactercreator_cleric;
'''
curs_6.execute(query_6)
result6 = curs_6.execute(query_6).fetchall()


# Fighter Count
curs_7 = conn.cursor()
query_7 = '''
SELECT
	COUNT(character_ptr_id)
FROM
	charactercreator_fighter;
'''
curs_7.execute(query_7)
result7 = curs_7.execute(query_7).fetchall()


# Mage Count
curs_8 = conn.cursor()
query_8 = '''
SELECT
	COUNT(character_ptr_id)
FROM
	charactercreator_mage;
'''
curs_8.execute(query_8)
result8 = curs_8.execute(query_8).fetchall()


# Armory Items that are weapons
curs_9 = conn.cursor()
query_9 = '''
SELECT
	COUNT(item_ptr_id)
FROM
	armory_weapon;
'''
curs_9.execute(query_9)
result9 = curs_9.execute(query_9).fetchall()


# How many Items does each character have? (Return first 20 rows)
# (Return first 20 rows)
curs_10 = conn.cursor()
query_10 = '''
SELECT
	COUNT(item_id),
	character_id
FROM
	charactercreator_character_inventory
GROUP BY
	character_id;
'''
curs_10.execute(query_10)
result10 = curs_10.execute(query_10).fetchall()
columns10 = list(map(lambda x:x[0], curs_10.description))
df10 = pd.DataFrame(data=result10, columns=columns10)


# How many Weapons does each character have? (Return first 20 rows)
# Could change the order of the columns to match below but otherwise it works.
curs_11 = conn.cursor()
query_11 = '''
SELECT
	armory_item.item_id,
	armory_weapon.item_ptr_id,
	charactercreator_character_inventory.character_id
FROM
	armory_item
	JOIN charactercreator_character_inventory ON armory_item.item_id = charactercreator_character_inventory.item_id
	JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id;
'''
curs_11.execute(query_10)
result11 = curs_11.execute(query_11).fetchall()
columns11 = list(map(lambda x:x[0], curs_11.description))
df11 = pd.DataFrame(data=result11, columns=columns11)
pd_series11 = (df11['character_id'].value_counts()) # turn into series
frame = {'weapon_count': pd_series11} # now that I have count turn back into df
final_frame = pd.DataFrame(frame)
final_frame.index.name = 'character_id'
final_frame = final_frame.sort_values(by='character_id', ascending=True)
final_frame.reset_index(inplace=True)


# On average, how many Items does each Character have?
average_items = df10["COUNT(item_id)"].mean()

# On average, how many Weapons does each character have?
average_weapons = final_frame['weapon_count'].mean()

# Setting Variables
# unique_names = (df3['name'].nunique())
# unique_items = (df4['name'].nunique())
result1 = result1[0]
result2 = result2[0]
result5 = result5[0]
result6 = result6[0]
result7 = result7[0]
result8 = result8[0]
result9 = result9[0]
not_weapons = int(result2[0]) - int(result9[0])
char_total = int(result5[0]) + int(result6[0]) + int(result7[0]) + int(result8[0]) 


print("\n\nThere are " + str(result1[0]) + " TOTAL characters.\n-----")
print("There are " + str(result5[0]) + " characters who are thiefs.")
print("There are " + str(result6[0]) + " characters who are clerics.")
print("There are " + str(result7[0]) + " characters who are fighters.")
print("There are " + str(result8[0]) + " characters who are mages.\n________")
print(str(result5[0]) + " + " + str(result6[0]) + " + " + str(result7[0]) + " + " + str(result8[0]) + " = " + str(char_total))
print("\n" + str(result2[0]) + " Total items in the armory.\n------")
print("There are " + str(result9[0]) + " Total Armory Items are weapons.\n" + str(not_weapons) + " of the items are NOT weapons.")
print("________\n" + str(result9[0]) + " + " +  str(not_weapons) + " = " + str(result2[0]))
print("\nBelow are the first 20 Armory Item Counts for each Character.")
print(df10.head(20))
print("\nBelow are the first 20 Weapon Counts for each Character ID.")
print(final_frame.head(20))
print("\nThe average items that each character has is " + str(round(average_items, 2)))
print("\nThe average weapons that each character has is " + str(round(average_weapons, 2)) + "\n")
print("\n")






