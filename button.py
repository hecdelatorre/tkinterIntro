from tkinter import Tk, Button, Label

root = Tk()
root.title('Button')
root.geometry('500x300')

lb = Label(root, text = 'Text label')
def click():
    lb.pack()

btn = Button(root, text='Clik Here', command=click, fg='#2E3436', bg='#BABDB6')
btn.pack()

root.mainloop()
