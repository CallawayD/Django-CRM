import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Shadydog1'
)

# prepare a cursor object
cursorobject = dataBase.cursor()

# Create a database
cursorobject.execute("CREATE DATABASE elderco")

print("All Done!")