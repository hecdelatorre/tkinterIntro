from tkinter import Tk, Button, Toplevel, Label
from PIL import ImageTk, Image

root = Tk()
root.title('Hello World')

# Solution 1
# def open():
#     img = ImageTk.PhotoImage(Image.open('img/img3.jpg'))
#     top = Toplevel()
#     top.title('Hello World, new window')
#     Label(top, text='I am text, in second window').pack()
#     Label(top, image=img).pack()
#     top.mainloop()
# Button(root, text='Click', command=open).pack()

# Solution 2
# def open():
#     global img
#     img = ImageTk.PhotoImage(Image.open('img/img4.jpg'))
#     top = Toplevel()
#     top.title('Hello World, new window')
#     Label(top, text='I am text, in second window').pack()
#     Label(top, image=img).pack()
#     top.mainloop()
# Button(root, text='Click', command=open).pack()

# Solution 3
def open(img):
    top = Toplevel()
    top.title('Hello World, new window')
    Label(top, text='I am text, in second window').pack()
    Label(top, image=img).pack()
    top.mainloop()

img = ImageTk.PhotoImage(Image.open('img/img2.jpg'))
Button(root, text='Click', command=lambda: open(img)).pack()

root.mainloop()
