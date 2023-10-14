import socket
import select
import sys 
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=5607
server_socket.bind(('127.0.0.1',port)) 
server_socket.listen(1)
server_socket.setblocking(1)
while True:
    client,add = server_socket.accept()
    while True:
            data =client.recv(1024)
            decoded_string =data.decode('utf-8')
            if decoded_string=="CLOSE SOCKET":
                client.close()
                break
            else:
                send_message=decoded_string.upper()
                print (send_message)
                m_as_b= bytes(send_message,'utf-8')
                client.send(m_as_b)
        
        