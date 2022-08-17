import socket
import time
import os

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP = input("coloca la ip del servidor a conectar: ")

client.connect((f"{IP}",9999))

def reciever():
  while True:
     print("esperando archivo del servidor...")
     data = client.recv(1024)
     name = input("introduce un nombre al archivo y su formato correspondiente enviado desde el servidor: ")
     print("Creando archivo pasando los datos..")
     with open(f"{name}","wb") as f:
       f.write(data)
       print("archivo recibido con exito")
       break

reciever()



