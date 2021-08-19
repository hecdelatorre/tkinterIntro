from tkinter import Tk, Entry, Button, Label

root = Tk()
root.title('Inputs')
root.geometry('500x300')

e = Entry(root, width=40)
e.pack()
e.insert(0, 'Enter text')

def count(text, counter=0):
    for _ in text: counter += 1
    return counter

def click():
    text = e.get()
    end = count(text)
    if end != 0: 
        lb.configure(text=text) 
        e.delete(0, end)
    else: lb.configure(text='Please enter a valid text')


btn = Button(root, text='Clik Here', command=click, fg='#2E3436', bg='#BABDB6')
btn.pack()

lb = Label(root, text='Label text')
lb.pack()

root.mainloop()
