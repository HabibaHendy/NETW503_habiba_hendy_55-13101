import socket
import select
import sys
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=5607
client_socket.setblocking(1)
client_socket.connect(('127.0.0.1',port))
while True:
    message=input("enter your message: ")
    if message=="CLOSE SOCKET":
        client_socket.close()
    m_as_b= bytes(message,'utf-8')
    client_socket.send(m_as_b)
    data=client_socket.recv(1024)
    decoded_string =data.decode('utf-8')
    if decoded_string!= "":
        print("received message:",decoded_string)
    