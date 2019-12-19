import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))


def message(s):
    l = s.split(':')[0]
    mes = s.split(':')[1]
    if l == 'Dan':
        c2.send(mes)
    if l == 'Alice':
        c1.send(mes)




s.listen(5)
while True:
   c1, addr = s.accept()
   c2, addr = s.accept()
   print ('Получил соединение от', addr)
   c1.send(bytes('Hi','utf8'))
   c2.send(bytes('Hi','utf8'))
   # print(c1.recv(1024))
   # print(c2.recv(1024))
   # c1.send(c2.recv(1024))
   # c2.send(c1.recv(1024))
   message(c1.recv(1024))
   message(c2.recv(1024))
   c1.close()
   c2.close()


