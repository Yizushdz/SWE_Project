import mysql.connector

# create database connection with Django settings
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpassword",
)

# middleware to handle database connection
cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE 3340database")
print("hello data base 3340")