import mysql.connector

cnx = mysql.connector.connect(user='joseernesto@joseernesto', password='1590', host='192.168.1.93', database='employees')
cnx.close()