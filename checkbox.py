from tkinter import Tk, Checkbutton, StringVar, Button, Label

root = Tk()
root.title('Checkbox')
root.geometry('500x300')

var = StringVar()
var.set('No')

def mostrar():
    l = Label(root, text=var.get())
    l.pack()

c = Checkbutton(root, text='Soy un Checkbox', variable=var, onvalue='Si', offvalue='No')
c.pack()

Button(root, text='Click', command=mostrar).pack()
root.mainloop()
