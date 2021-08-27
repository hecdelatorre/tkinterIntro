from tkinter import Tk, Label
from PIL import ImageTk, Image

root = Tk()

# img = Image.open('img.png')
# img.show()

img = ImageTk.PhotoImage(Image.open('img.png'))
lb = Label(image=img)
lb.pack()

root.mainloop()
