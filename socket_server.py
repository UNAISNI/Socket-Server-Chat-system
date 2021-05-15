import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',8080))
server_socket.listen(10)
print("[+] listing for connection on 127.0.0.1:8080")

while True:
    cond,addr = server_socket.accept()
    print("[+] Got a Connection on", addr)
    while True:
     data = cond.recv(1024)
     if(data.decode() == 'bye'):
         break
     print("[+] Client Send:",data.decode())
     server_data = input("Enter the Data: ")
     cond.send(server_data.encode())

    cond.close()
    print("[+] Client Disconnected")