import random
from socket import *
import time

HOST = 'localhost'
PORT = 9999
ADDR = (HOST, PORT)
tcpSock = socket(AF_INET, SOCK_STREAM)
tcpSock.bind(ADDR)
tcpSock.setblocking(True)
tcpSock.listen(1)


c, addr = tcpSock.accept()
while True:
    try:
        message = input("podaj wartosc\n")
        c.send((message + "\n").encode("utf-8"))
    except:
        break

c.close()
tcpSock.close()
