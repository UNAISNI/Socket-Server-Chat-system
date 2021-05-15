import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1",8080));
print("[+] Trying To Connect 127.0.0.1:8080")

while True:
    data = input("Enter the data: ")
    client_socket.send(data.encode())
    server_socket = client_socket.recv(1024)
    if(server_socket == ""): break
    if(data == "bye"): break
    print("[+] Server Send:",server_socket.decode())
client_socket.close()