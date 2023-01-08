from tkinter import *
from tkinter.ttk import Combobox


def clicked():
    res = "Привет {}".format(combo.get())
    lbl.configure(text=res)


root = Tk()
root.title('Welcome')
root.geometry('400x400+300+300')

lbl = Label(root, text='Hi', font=("Arial Bold", 10))
lbl.grid(column=1, row=0)

btn = Button(root, text='dont press', bg="black", fg="red", command=clicked)
btn.grid(column=1, row=1)

txt = Entry(root, width=10, state='normal')
txt.grid(column=0, row=1)
txt.focus()

combo = Combobox(root)
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(0)
combo.grid(column=0, row=0)

root.mainloop()

from tkinter import *
from tkinter.ttk import Checkbutton

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
chk_state = BooleanVar()
chk_state.set(False)  # задайте проверку состояния чекбокса
chk = Checkbutton(window, text='Выбрать', var=chk_state)
chk.grid(column=0, row=0)
window.mainloop()

from tkinter import *
from tkinter.ttk import Radiobutton

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
rad1 = Radiobutton(window, text='Первый', value=1)
rad2 = Radiobutton(window, text='Второй', value=2)
rad3 = Radiobutton(window, text='Третий', value=3)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
window.mainloop()

from tkinter import *
from tkinter.ttk import Radiobutton


def clicked():
    lbl.configure(text=selected.get())


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
selected = IntVar()
rad1 = Radiobutton(window, text='Первый', value=1, variable=selected)
rad2 = Radiobutton(window, text='Второй', value=2, variable=selected)
rad3 = Radiobutton(window, text='Третий', value=3, variable=selected)
btn = Button(window, text="Клик", command=clicked)
lbl = Label(window)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)
lbl.grid(column=0, row=1)
window.mainloop()

from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('200x200')
txt = scrolledtext.ScrolledText(window, width=20, height=10)
txt.grid(column=0, row=0)
txt.insert(INSERT, 'Текстовое поле\n')
txt.delete(1.0, END)
window.mainloop()

from tkinter import *
from tkinter import messagebox


def clicked():
    messagebox.showinfo('лох', 'ы')
    messagebox.showwarning('Заголовок', 'Текст')
    messagebox.showerror('Заголовок', 'Текст')
    res = messagebox.askquestion('Заголовок', 'Текст')
    res = messagebox.askyesno('Заголовок', 'Текст')
    res = messagebox.askyesnocancel('Заголовок', 'Текст')
    res = messagebox.askokcancel('Заголовок', 'Текст')
    res = messagebox.askretrycancel('Заголовок', 'Текст')


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
btn = Button(window, text='Клик', command=clicked)
btn.grid(column=0, row=0)
window.mainloop()

from tkinter import *

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
spin = Spinbox(window, from_=0, to=100, width=5)
# spin = Spinbox(window, values=(3, 8, 11), width=5)
spin.grid(column=0, row=0)
window.mainloop()

from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 70
bar.grid(column=0, row=0)
window.mainloop()

from tkinter import *
from tkinter import Menu

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Новый', command=clicked)
new_item.add_command(label='Новwй')
new_item.add_separator()
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
window.mainloop()

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Первая')
tab_control.add(tab2, text='Вторая')
lbl1 = Label(tab1, text='label1', padx=50, pady=5)
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text='Вкладка 2')
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')
window.mainloop()
