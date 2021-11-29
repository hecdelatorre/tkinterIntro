from tkinter import Tk, filedialog, Button
from tkinter.messagebox import showinfo

root = Tk()
root.title('Open file')
root.resizable(False, False)
root.geometry('300x150')

def selectFile():
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))
    filename = filedialog.askopenfile(title='Open a file', initialdir='~', filetypes=filetypes)
    showinfo(title='Select File', message=f'{filename}')
    
Button(root, text='Open a file', command=selectFile).pack(expand=True)

root.mainloop()
