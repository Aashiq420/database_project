import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='lifechoices', 
    password='@Lifechoices1234',
    database='dentistry',
    auth_plugin='mysql_native_password')

mycursor = mydb.cursor()
xy = mycursor.execute('Select * from Dentists')
for i in mycursor:
    print(i)

print(mydb)