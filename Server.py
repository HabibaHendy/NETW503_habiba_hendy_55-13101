import threading
import socket
import select
import sys 
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=5606
server_socket.bind(('127.0.0.1',port)) 
server_socket.listen()
server_socket.setblocking(1)
def threaded(client, add):
     print("[NEW CONNECTION] " + str(add) + " connected.")
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
def main():
     print(" Server is starting...")
     while True:
          client,add = server_socket.accept()
          #threading.Lock().acquire()
          threading.Thread(target=threaded,args=(client,add)).start()
          print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
if __name__ == "__main__":
     main()