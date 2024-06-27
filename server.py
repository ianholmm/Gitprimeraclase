import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',12345))
s.listen()


data, addr = s.recvfrom(1024)


s.sendto("message for client".encode(),addr)


print("Hola mundo")
print(data)
s.close()
