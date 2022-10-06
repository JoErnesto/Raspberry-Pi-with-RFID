import mysql.connector

cnx = mysql.connector.connect(user='joseernesto', password='1234', host='127.0.0.1', database='codigoIoT')
query = ("SELECT id,fecha,nombre,temperatura FROM clima WHERE id=3364;")

res = cnx.cmd_query(query)

#imrpimir resultado
print("Respuesta:")
print(res)

cnx.close()
