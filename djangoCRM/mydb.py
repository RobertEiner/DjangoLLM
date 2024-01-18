import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    passwd = 'root'


)


cursorObject = dataBase.cursor()

# create database
cursorObject.execute('Create database djangoDB')

print('DB created')