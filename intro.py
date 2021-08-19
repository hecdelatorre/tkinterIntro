from tkinter import Tk, Label

root = Tk()
root.title('Hello World')
root.geometry('500x300')

lb1 = Label(root, text = 'Hello, this is a tag')
lb2 = Label(root, text = 'Hello, this is a tag')
# Label(root, text = 'Hello, this is a tag').pack()

lb1.grid(row=0, column=0)
lb2.grid(row=0, column=1)

root.mainloop()
