import sqlite3 as sql
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

db = sql.connect('user_l_p')
# Create Cursor
c = db.cursor()


def is_wrong(a):
    """Проверяет правильность пароля и логина"""
    symbol = '!@#$%^&*()-=/*-+?><'
    res = False
    if len(a) < 5:
        res = True
    else:
        for i in a:
            for k in symbol:
                if i == k:
                    res = True
                    break
    return res


def enter():
    """Записывает в бд ваш логин и пароль"""
    if not (login.get() == '' or pass_w.get() == '' or is_wrong(pass_w.get()) or is_wrong(login.get())):
        res = (login.get(), pass_w.get())
        c.execute("INSERT INTO userpass VALUES " + str(res))
        messagebox.showinfo(message='Data written')
    else:
        lbl_err.configure(text='Error, try again.')
    login.delete(0, END)
    pass_w.delete(0, END)
    login.focus()


def show_list():
    """Выводит список всех логинов и паролей"""
    reg = Toplevel(window)
    reg.title('registration')
    reg.geometry('285x400+800+400')
    reg.minsize(262, 340)
    reg.maxsize(262, 340)
    scr = scrolledtext.ScrolledText(reg, width=30, height=20)
    scr.place(x=0, y=0)
    c.execute("SELECT * FROM userpass")
    items = c.fetchall()
    for el in items:
        scr.insert(CURRENT, el[0] + ' ' + el[1] + "\n")
    scr.configure(state=DISABLED)


def delete_list():
    """Удаление своего логина и пароля"""
    if not (login.get() == '' or pass_w.get() == ''):
        c.execute("DELETE FROM userpass WHERE login = '" + login.get()+"'" + " AND password = '" + pass_w.get() +"'")
        messagebox.showinfo(message='Data deleted')
    else:
        lbl_err.configure(text='Error, try again.')
    login.delete(0, END)
    pass_w.delete(0, END)
    login.focus()


window = Tk()
window.title('Welcome')
window.geometry('285x108+800+400')
window.minsize(285, 108)
window.maxsize(285, 108)

lbl = Label(window, text='Hi, enter you login and password')
lbl.place(x=5, y=5)

lbl_err = Label(window, text='Your pass should = only letters\nand numbers and >4 symbols')
lbl_err.place(x=5, y=65)

btn = Button(window, text='press for\nregistration', command=enter)
btn.place(x=190, y=34)

btn_reg = Button(window, text='press for list', command=show_list)
btn_reg.place(x=190, y=78)

btn_del = Button(window, text='press to delete', command=delete_list)
btn_del.place(x=190, y=5)

login = Entry(window, width=10, state='normal')
login.place(x=5, y=40)
login.focus()

pass_w = Entry(window, width=10, state='normal')
pass_w.place(x=120, y=40)

window.mainloop()

db.commit()

db.close()
