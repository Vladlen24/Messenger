from tkinter import *
from PIL import Image, ImageTk
window = Tk() #object of Tkinter class - registration_window
window.title("Messenger")
window.geometry('400x250+500+250') #setting size of the window
window.resizable(False, False) #user can not change size of the window
load = Image.open("sky.jpg")#adding sky wallpapers
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
img.place(x=-10, y=-10)
global output #messages, that user sends
global reg_login, reg_password, aut_login, aut_password #login and password from the first registration window
reg_login = ''
reg_password = ''
aut_login = ''
aut_password = ''

class client:
    #client window
    def __init__(self):
        self.log = '' #login == IP of our user
        self.IP = '' # login of another user, speaking with us
        self.output = ''
    def message_out(self):
        self.text0.configure(state='normal') #we unblock textwindow and write there quickly
        self.output = self.text.get('1.0', 'end') # we save text, that user printed
        self.text0.insert(1.0, self.output) #text from small textwindow prints to big textwindow
        self.text.delete('1.0', 'end') #we delete printed text
        self.text0.configure(state='disabled') #we block textwindow quickly
    def create(self): #creating user window
        self.root = Toplevel()
        self.root.title("user " + self.log)
        self.root.geometry(str(self.root.winfo_screenwidth() - 100) + 'x' + str(self.root.winfo_screenheight() - 100) + '+0+0')
        self.root.resizable(False, False)
        render = ImageTk.PhotoImage(load)
        img = Label(self.root, image=render)
        img.image = render
        img.place(x=-10, y=-10)
        self.text = Text(self.root, width=100, height=1, bg="white", fg='black', wrap=WORD) #small textwindow
        self.text.place(relx = .35, rely = .9)
        self.text0 = Text(self.root, width=100, height=30, bg="white", fg='black', wrap=WORD) #big textwindow
        self.text0.place(relx=.35, rely=.15)
        self.text0.configure(state='disabled') #blocking of big textwindow
        self.scroll = Scrollbar(self.root, command=self.text0.yview) # adding scroll, it isn't very important thing
        self.scroll.pack(side=RIGHT, fill = Y)
        self.text0.config(yscrollcommand=self.scroll.set)
        self.enter_button = Button(self.root, text='отправить', command=self.message_out) #send button, uses message_out method
        self.enter_button.place(relx = .92, rely = .94) #just button can send messages, not enter yet
    def message_in(self, mess):
        self.text0.configure(state='normal') #unblock big textwindow
        self.text0.insert(1.0, mess) #printing to big textwindow text from another user
        mess = '' #now, we haven't new messages
        self.text0.configure(state='disabled')#block big textwindow



text1 = Label(text = "Регистрация пользователя") #creating registration text object
text1.place(relx = .25, rely = .08) #putting registration text in it's place

text2 = Label(text = "Логин: ") #creating registration login text object
text2.place(relx = .06, rely = .2) #putting registration login text in it's place
sign_up_login = Entry(window, width = 20, bd = 3) #creating sign_up_login entry
sign_up_login.place(relx = .3, rely = .2) #putting sign_up_login entry in it's place
text3 = Label(text = "Пароль: ") #creating registration login text object
text3.place(relx = .06, rely = .36) #putting registration login text in it's place
sign_up_password = Entry(window, width = 20, bd = 3) #creating sign_up_password entry
sign_up_password.place(relx = .3, rely = .35) #putting sign_up_password entry in it's place

def reg(): #registration button
    global reg_login, reg_password
    reg_login = sign_up_login.get()
    sign_up_login.delete(0, END)
    reg_password = sign_up_password.get()
    sign_up_password.delete(0, END)
reg_button = Button(text='Ввод', command=reg)
reg_button.place(relx= .7, rely = .27)


text4 = Label(text = "Авторизация пользователя") #creating authorization text object
text4.place(relx = .25, rely = .58) #putting authorization text in it's place

text5 = Label(text = "Логин: ") #creating authorization login text object
text5.place(relx = .06, rely = .7) #putting authorization login text in it's place
sign_in_login = Entry(window, width = 20, bd = 3) #creating sign_in_login entry
sign_in_login.place(relx = .3, rely = .7) #putting sign_in_login entry in it's place
text6 = Label(text = "Пароль: ") #creating authorization login text object
text6.place(relx = .06, rely = .86) #putting authorization login text in it's place
sign_in_password = Entry(window, width = 20, bd = 3) #creating sign_in_password entry
sign_in_password.place(relx = .3, rely = .85) #putting sign_in_password entry in it's place

def aut(): #authorization button
    global aut_login, aut_password
    aut_login = sign_in_login.get()
    sign_in_login.delete(0, END)
    aut_password = sign_in_password.get()
    sign_in_password.delete(0, END)
aut_button = Button(text='Ввод', command=aut)
aut_button.place(relx= .7, rely = .77)


window.mainloop()