from tkinter import Tk, IntVar, Radiobutton, Label, StringVar

root = Tk()
root.title('Radio Button')

nakanoList = [
    ('Ichika', 'Nakano 1'),
    ('Nino', 'Nakano 2'),
    ('Miku', 'Nakano 3'),
    ('Yotsuba', 'Nakano 4'),
    ('Itsuki', 'Nakano 5')
]

nakanoVar = StringVar()
nakanoVar.set('Miku')

for text, nakano in nakanoList:
    Radiobutton(root, text=text, variable=nakanoVar, value=nakano).pack()


lb = Label(root, textvariable=nakanoVar)
lb.pack()

root.mainloop()
