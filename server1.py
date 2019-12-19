import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
   c1, addr = s.accept()
   c2, addr = s.accept()
   print ('Получил соединение от', addr)
   c1.send(bytes('Hello, I am a server Bob. I will help you to speak with your friends. So, lets go to speak!','utf8'))
   c2.send(bytes('Hello, I am a server Bob. I will help you to speak with your friends. So, lets go to speak!','utf8'))
  # print(c1.recv(1024))
  # print(c2.recv(1024))
   c1.send(c2.recv(1024))
   c2.send(c1.recv(1024))
   c1.close()
   c2.close()


