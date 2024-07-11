import mysql.connector

mydb = mysql.connector.connect(
    host="online",
    user="root",
    passwd="9800"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE ONLINE")
