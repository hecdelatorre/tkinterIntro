from tkinter import Tk, Frame, StringVar, Entry, Label, Button

root = Tk()
root.title('Inches to centimeters')

def calculate(*arg):
    try:
        value = float(inches.get())
        c = str(value * 2.54)
        centimeters.set(c)
        inches_input.delete(0, len(c))
    except ValueError:
        inches_input.delete(0, len(inches.get()))
        centimeters.set('Error')

frame = Frame(root, pady=20, padx=30)
frame.grid(column=0, row=0)

inches = StringVar()
inches_input = Entry(frame, width=10, textvariable=inches)
inches_input.grid(column=1, row=0)

centimeters = StringVar()
Label(frame, textvariable=centimeters).grid(column=1, row=1)


Label(frame, text='Inches').grid(column=0, row=0)
Label(frame, text='Is equal to').grid(column=0, row=1)
Label(frame, text='Centimeters').grid(column=2, row=1)

Button(frame, text='Calculate', command=calculate).grid(column=2, row=2)

inches_input.focus()

root.bind("<Return>", calculate)
root.mainloop()
