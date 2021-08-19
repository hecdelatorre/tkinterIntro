from tkinter import Tk, Entry, Button, Label

root = Tk()
root.title('Inputs')
root.geometry('500x300')

e = Entry(root, width=40)
e.pack()
e.insert(0, 'Enter text')

def click():
    text = e.get()
    if len(text) != 0: 
        lb.configure(text=text) 
        e.delete(0, len(text))
    else: lb.configure(text='Please enter a valid text')

btn = Button(root, text='Clik Here', command=click, fg='#2E3436', bg='#BABDB6')
btn.pack()

lb = Label(root, text='Label text')
lb.pack()

root.mainloop()
