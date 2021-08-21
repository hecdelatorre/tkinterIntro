from tkinter import Tk, Button

root = Tk()
root.title('Quit')
root.geometry('150x50')

Button(root, text='Exit', fg='#FFFFFF', bg='#888A85', command=root.quit).pack()

root.mainloop()
