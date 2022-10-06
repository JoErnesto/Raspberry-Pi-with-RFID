import mysql.connector

cnx = mysql.connector.connect(user='joseernesto', password='1234', host='127.0.0.1', database='codigoIoT')
print(cnx)
cnx.close()
