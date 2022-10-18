#Bibliotecas
from time import sleep
import sys
from mfrc511 import SimpleMFRC522
import RPi.GPIO as GPIO
import mysql.connector

#Iniciar el sensor
reader = SimpleMFRC522()

#Conexión
cnx= mysql.connector.connect(user='joseernestolan', password='1590', host='192.168.1.93', database='codigoIoT')

#Cursor
cursor = cnx.cursor()

#Cuerpo del programa
try:
    #Lectura unica
    id, text = reader.read()
    print("ID: %S\nText: %S" % (id,text))
    sleep(1)

except KeyboardInterrupt:
    #Cerrar
    cursor.close()
    cnx.close()
    GPIO.cleanup()
    raise