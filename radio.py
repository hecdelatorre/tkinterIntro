from tkinter import Tk, IntVar, Radiobutton, Label

root = Tk()
root.title('Radio Button')

r = IntVar()
r.set(2)

Radiobutton(root, text='Option 1', variable=r, value=1).pack()
Radiobutton(root, text='Option 2', variable=r, value=2).pack()

lb = Label(root, textvariable=r)
lb.pack()

root.mainloop()
