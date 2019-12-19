import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

print(host)
s.listen(5)
while True:
   c, addr = s.accept()    
   print ('Получил соединение от', addr)
   c.send(bytes('Hello','utf8'))
   print(c.recv(1024))
   c.close()

