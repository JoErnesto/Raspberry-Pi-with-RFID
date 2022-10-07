
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import mysql.connector


cnx = mysql.connect(user='joseernestolan', password='1590', host='192.168.1.93', database='codigoIoT')

cursor = cnx.cursor()

reader = SimpleMFRC522()

try:
    while True:
        print("COlocar el tag")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        query_insert = "INSERT INTO RFID (nombre,texto,rfid) VALUES ('Jose Ernesto','" + text + "'," + str(id)+");"

        cursor.execute(query_insert)

        cnx.commit()
        print("Query cargado")

        sleep(5)

except KeyboardInterrupt:
    cursor.close()
    cnx.close()
    GPIO.cleanup()
    raise