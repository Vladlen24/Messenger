import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))


def login(s):
    nik = s.split(':')[0]
    pas = s.split(':')[1]
    a = []
    k = 0
    f = open('users.txt','r')
    for i in f:
        f.read(i)
        a.append(i)
        if s == i:
            k+=1
    if k == 1:
        g = open('online.txt','a')
        g.write(s+'\n')
        return True


def sign(s):
    nik = s.split(':')[0]
    pas = s.split(':')[2]
    k = 0
    f = open('users.txt','r')
    for i in f:
        f.read(i)
        if s == i:
            k+=1
    if k == 0:
        g = open('users.txt','a')
        g.write(s+'\n')
        return True


def message(s):
    l = s.split(':')[0]
    mes = s.split(':')[1]
    #if l == 'Dan':
    c2.send(mes)
    #if l == 'Alice':
    c1.send(mes)



s.listen(5)
while True:
    c1, addr = s.accept()
    c2, addr = s.accept()
    print ('Получил соединение от', addr)
    c1.send(bytes('Hi','utf8'))
    c2.send(bytes('Hi','utf8'))
    while True:
        mess1 = str(c1.recv(1024))
        mess2 = str(c2.recv(1024))
        #f = open('online.txt','r')
        #for i in f:
        #    f.read(i)
        if mess1.split(':')[1] == 'reg':
            sign(mss1)
            c1.send(sign(mess1))

        if mess1.split(':')[1] == 'aut':
            login(mss1)
            c1.send(login(mess1))

        if mess2.split(':')[1] == 'reg':
            sign(mss2)
            c2.send(sign(mess2))

        if mess2.split(':')[1] == 'aut':
            login(mss2)
            c2.send(login(mess2))

        if login(mess1) == True:
            m1 = str(c1.recv(1024))
            m2 = str(c2.recv(1024))

            if m1.split(':')[1] == 'Dan':
                l = s.split(':')[0]
                mes = s.split(':')[2]
                print(c1.recv(1024))
                print(c2.recv(1024))
                c2.send(mes)
                c1.send(mes)

        if login(mess2) == True:
            m1 = str(c1.recv(1024))
            m2 = str(c2.recv(1024))

            if m2.split(':')[1] == 'Alice':
                l = s.split(':')[0]
                mes = s.split(':')[2]
                print(c1.recv(1024))
                print(c2.recv(1024))
                c2.send(mes)
                c1.send(mes)

    c1.close()
    c2.close()

#while True:
#    a = []
#    c, addr = s.accept()
#    a.append(c)
#    print ('Получил соединение от', addr)
#    c.send(bytes('Hi','utf8'))
#    mes = str(c.recv(1024)).split(':')[1]
#    if mes != '':
#        for i in range len(a):
#            message(a[i], mes)
