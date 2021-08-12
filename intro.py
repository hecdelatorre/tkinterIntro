from tkinter import Tk, Label

root = Tk()
root.title('Hello World')
root.geometry('500x300')

label = Label(root, text = 'Hello, this is a tag')
# Label(root, text = 'Hello, this is a tag').pack()

label.pack()

root.mainloop()
