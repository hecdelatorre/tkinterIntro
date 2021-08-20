from tkinter import Tk, Entry, Button, Label, StringVar

root = Tk()
root.title('Inputs')
root.geometry('500x300')

e = Entry(root, width=40)
e.pack()
e.insert(0, 'Enter text')

def click():
    text = e.get()
    if len(text) != 0: 
        # lb.configure(text=text) 
        textvar.set(text)
        print(textvar.get())
        e.delete(0, len(textvar.get()))
    else: textvar.set('Please enter a valid text')

btn = Button(root, text='Clik Here', command=click, fg='#2E3436', bg='#BABDB6')
btn.pack()

textvar = StringVar()

lb = Label(root, textvariable=textvar)
lb.pack()

root.mainloop()
