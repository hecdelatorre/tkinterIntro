from tkinter import Tk, Label

root = Tk()
root.title('Hello World')
root.geometry('500x300')

lb1 = Label(root, text = 'Hello, this is a tag -> 1')
lb2 = Label(root, text = 'Hello, this is a tag -> 2')
lb3 = Label(root, text = 'Hello, this is a tag -> 3')
# Label(root, text = 'Hello, this is a tag').pack()

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=1)
lb3.grid(row=1, column=2)

root.mainloop()
