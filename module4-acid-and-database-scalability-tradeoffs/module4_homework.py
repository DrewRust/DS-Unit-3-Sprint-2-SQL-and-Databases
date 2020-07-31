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
# print(conn)
# print(postGres_cursor2)
# postGres_cursor2.execute('SELECT COUNT(*) FROM passengers;')
# print("\n")
# print(postGres_cursor2.fetchall())
# print("\n")
# postGres_cursor2.execute('SELECT * FROM passengers LIMIT 10;')
# print(postGres_cursor2.fetchall())
# print("\n")
# postGres_cursor2.execute("SELECT * FROM passengers LIMIT 20;")
# for row in postGres_cursor2:
#   print(row)


query1 = '''
SELECT
	column_name,
	data_type,
	character_maximum_length
FROM
	INFORMATION_SCHEMA.COLUMNS
WHERE
	table_name = 'passengers';
'''
# postGres_cursor2.execute(query1)
# print("\n")
# print(postGres_cursor2.fetchall())
print("\nColumns:\n")
postGres_cursor2.execute(query1)
for row in postGres_cursor2:
  print(row)


query2 = '''
SELECT
	COUNT(*) FILTER (WHERE survived = TRUE)
FROM
	passengers;
'''
postGres_cursor2.execute(query2)
postGres_cursor2.execute(query2)
survived = (postGres_cursor2.fetchall()[0])
print("\nTotal survivors: " + str(survived[0]))


query3 = '''
SELECT
	COUNT(*) FILTER (WHERE survived = FALSE)
FROM
	passengers;
'''
postGres_cursor2.execute(query3)
deaths = (postGres_cursor2.fetchall()[0])
print("\nTotal deaths: " + str(deaths[0]) + "\n")


query4 = '''
SELECT
	COUNT(*) FILTER (WHERE pclass = 1)
FROM
	passengers;
'''
postGres_cursor2.execute(query4)
firstClass = (postGres_cursor2.fetchall()[0])
print("First Class: " + str(firstClass[0]) + "\n")


query5 = '''
SELECT
	COUNT(*) FILTER (WHERE pclass = 2)
FROM
	passengers;
'''
postGres_cursor2.execute(query5)
secondClass = (postGres_cursor2.fetchall()[0])
print("Second Class: " + str(secondClass[0]) + "\n")

query6 = '''
SELECT
	COUNT(*) FILTER (WHERE pclass = 3)
FROM
	passengers;
'''
postGres_cursor2.execute(query6)
thirdClass = (postGres_cursor2.fetchall()[0])
print("Third Class: " + str(thirdClass[0]) + "\n")



query7 = '''
SELECT
	count(*)
FROM
	passengers
WHERE
	pclass = 1
	AND survived = TRUE;
'''
postGres_cursor2.execute(query7)
pclass1survived = (postGres_cursor2.fetchall()[0])
print("P-Class 1 Survivors: " + str(pclass1survived[0]) + "\n")



query8 = '''
SELECT
	count(*)
FROM
	passengers
WHERE
	pclass = 2
	AND survived = TRUE;
'''
postGres_cursor2.execute(query8)
pclass2survived = (postGres_cursor2.fetchall()[0])
print("P-Class 2 Survivors: " + str(pclass2survived[0]) + "\n")


query9 = '''
SELECT
	count(*)
FROM
	passengers
WHERE
	pclass = 3
	AND survived = TRUE;
'''
postGres_cursor2.execute(query9)
pclass3survived = (postGres_cursor2.fetchall()[0])
print("P-Class 3 Survivors: " + str(pclass3survived[0]) + "\n")


query7a = '''
SELECT
	count(*)
FROM
	passengers
WHERE
	pclass = 1
	AND survived = FALSE;
'''
postGres_cursor2.execute(query7a)
pclass1died = (postGres_cursor2.fetchall()[0])
print("P-Class 1 died: " + str(pclass1died[0]) + "\n")



query8a = '''
SELECT
	count(*)
FROM
	passengers
WHERE
	pclass = 2
	AND survived = FALSE;
'''
postGres_cursor2.execute(query8a)
pclass2died = (postGres_cursor2.fetchall()[0])
print("P-Class 2 died: " + str(pclass2died[0]) + "\n")


query9a = '''
SELECT
	count(*)
FROM
	passengers
WHERE
	pclass = 3
	AND survived = FALSE;
'''
postGres_cursor2.execute(query9a)
pclass3died = (postGres_cursor2.fetchall()[0])
print("P-Class 3 died: " + str(pclass3died[0]) + "\n")


query10 = '''
SELECT
	AVG(age)
FROM
	passengers
WHERE
	survived = True;
'''
postGres_cursor2.execute(query10)
avgagesurvive = (postGres_cursor2.fetchall()[0])
print("Average age of survivors: " + str(avgagesurvive[0]) + "\n")


query11 = '''
SELECT
	AVG(age)
FROM
	passengers
WHERE
	survived = False;
'''
postGres_cursor2.execute(query11)
avgagedeath = (postGres_cursor2.fetchall()[0])
print("Average age of dead: " + str(avgagedeath[0]) + "\n")


query12 = '''
SELECT
	AVG(age)
FROM
	passengers
WHERE
	pclass = 1;
'''
postGres_cursor2.execute(query12)
avgageagepclass1 = (postGres_cursor2.fetchall()[0])
print("Average age of first class: " + str(avgageagepclass1[0]) + "\n")

query13 = '''
SELECT
	AVG(age)
FROM
	passengers
WHERE
	pclass = 2;
'''
postGres_cursor2.execute(query13)
avgageagepclass2 = (postGres_cursor2.fetchall()[0])
print("Average age of second class: " + str(avgageagepclass2[0]) + "\n")

query14 = '''
SELECT
	AVG(age)
FROM
	passengers
WHERE
	pclass = 3;
'''
postGres_cursor2.execute(query14)
avgageagepclass3 = (postGres_cursor2.fetchall()[0])
print("Average age of third class: " + str(avgageagepclass3[0]) + "\n")



query15 = '''
SELECT
	pclass,
	AVG(fare)
FROM
	passengers
GROUP BY
	pclass
ORDER BY
	pclass;
'''
postGres_cursor2.execute(query15)
avgfarebyclass = (postGres_cursor2.fetchall())
print("Average fare by class: " + str(avgfarebyclass) + "\n")


query16 = '''
SELECT
	pclass,
	AVG(sib_spouse_count)
FROM
	passengers
GROUP BY
	pclass
ORDER BY
	pclass;
'''
postGres_cursor2.execute(query16)
avgsibspousebyclass = (postGres_cursor2.fetchall())
print("Average siblings / spouse count by class: " + str(avgsibspousebyclass) + "\n")


query17 = '''
SELECT
    survived,
	AVG(sib_spouse_count)
FROM
	passengers
GROUP BY
	survived
ORDER BY
	survived;
'''
postGres_cursor2.execute(query17)
avgsibspousebysurvival = (postGres_cursor2.fetchall())
print("Average siblings / spouse count by survival: " + str(avgsibspousebysurvival) + "\n")


query16a = '''
SELECT
	pclass,
	AVG(parent_child_count)
FROM
	passengers
GROUP BY
	pclass
ORDER BY
	pclass;
'''
postGres_cursor2.execute(query16a)
avgparentchildcountbyclass = (postGres_cursor2.fetchall())
print("Average parent / child count by class: " + str(avgparentchildcountbyclass) + "\n")


query17a = '''
SELECT
    survived,
	AVG(parent_child_count)
FROM
	passengers
GROUP BY
	survived
ORDER BY
	survived;
'''
postGres_cursor2.execute(query17a)
avgparentchildcountbysurvival = (postGres_cursor2.fetchall())
print("Average siblings / spouse count by survival: " + str(avgparentchildcountbysurvival) + "\n")


postGres_cursor2.close()
conn.close()