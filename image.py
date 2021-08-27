from tkinter import Tk, Label
from PIL import ImageTk, Image

root = Tk()

# img = Image.open('img.png')
# img.show()

img = ImageTk.PhotoImage(Image.open('img/img1.jpg'))
lb = Label(image=img)
lb.pack()

root.mainloop()
