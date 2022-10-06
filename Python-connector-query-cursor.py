import mysql.connector

cnx= mysql.connector.connect(user='joseernesto', password='1234', host='localhost', database='codigoIoT')

cursor = cnx.cursor()
query = ("SELECT id,nombre,temperatura FROM clima WHERE id=3364;")

#Cursor

cursor.execute(query)

res = cursor.fetchall()

for x in res:
    print(x)


#cnx.close()