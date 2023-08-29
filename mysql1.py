import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_db'
)

mycursor = mydb.cursor()

query = "SELECT * FROM person"
mycursor.execute(query)

results = mycursor.fetchall()

for x in results:
    listItems = dict(x)
    print(listItems)

mycursor.close()
mydb.close()