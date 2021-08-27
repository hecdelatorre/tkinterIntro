from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

root = Tk()
root.title('Carousel')

img1 = ImageTk.PhotoImage(Image.open('img/img1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('img/img2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('img/img3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('img/img4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('img/img5.jpg'))

listImg = [img1, img2, img3, img4, img5]

lb = Label(root, image=img1)
lb.grid(row=0, column=0, columnspan=3)

def nextImg(imgNum):
    global lb
    global backBtn
    global nextBtn

    lb.grid_forget()
    lb = Label(root, image=listImg[imgNum])

    backBtn = Button(root, text='<-', command=lambda: backImg(imgNum - 1))
    nextBtn = Button(root, text='->', command=lambda: nextImg(imgNum + 1))
    if imgNum == 4: nextBtn = Button(root, text='-', state='disabled')

    lb.grid(row=0, column=0, columnspan=3)
    backBtn.grid(row=1, column=0)
    nextBtn.grid(row=1, column=2)

def backImg(imgNum):
    global lb
    global backBtn
    global nextBtn

    lb.grid_forget()
    lb = Label(root, image=listImg[imgNum])

    backBtn = Button(root, text='<-', command=lambda: backImg(imgNum - 1))
    nextBtn = Button(root, text='->', command=lambda: nextImg(imgNum + 1))
    if imgNum == 0: backBtn = Button(root, text='-', state='disabled')

    lb.grid(row=0, column=0, columnspan=3)
    backBtn.grid(row=1, column=0)
    nextBtn.grid(row=1, column=2)


backBtn = Button(root, text='-', state='disabled')
nextBtn = Button(root, text='->', command=lambda: nextImg(1))

backBtn.grid(row=1, column=0)
nextBtn.grid(row=1, column=2)

root.mainloop()
