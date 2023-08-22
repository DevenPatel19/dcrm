# Installed MYSQL on my computer
# Installed MYSQL workbench
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='root'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE mtgbroker")

print("All Done!")
