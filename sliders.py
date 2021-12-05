from tkinter import Tk, Scale, Button

root = Tk()
root.title('Hello: Sliders')

vertical = Scale(root, from_=0, to=200, command=lambda _: enviar())
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient='horizontal')
horizontal.pack()

def enviar():
    hor = horizontal.get()
    ver = vertical.get()

    print(f'Horizontal: {hor}\nVertical: {ver}')

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()
