import mysql.connector

cnx = mysql.connector.connect(user='joseernesto', password='1234', host='127.0.0.1', database='codigoIoT')

cursor = cnx.cursor()

query_insert = "INSERT INTO RFID (nombre,texto,rfid) VALUES ('Jose Ernesto','Test Python 2',12345678);"

cursor.execute(query_insert)

cnx.commit()
print("Query Done")

cursor.close()
cnx.close()