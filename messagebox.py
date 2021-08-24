from tkinter import Tk, messagebox, Button

root = Tk()
root.title('Messagebox')

def click_showwarning(): messagebox.showwarning('Warning', 'Message')
def click_info(): messagebox.showinfo('Info', 'Message')
def click_error(): messagebox.showerror('Error', 'Message')

def click_ask(): 
    res = messagebox.askquestion('Ask', 'Message')
    messagebox.showinfo('Yes', 'Chose Yes') if res == 'yes' else messagebox.showinfo('No', 'Chose No')

def click_okcancel(): 
    res = messagebox.askokcancel('Ask', 'Message')
    messagebox.showinfo('Ok', 'Chose Ok') if res else messagebox.showinfo('Cancel', 'Chose Cancel')

def click_askyesno(): 
    res = messagebox.askyesno('Ask', 'Message')
    messagebox.showinfo('Yes', 'Chose Yes') if res else messagebox.showinfo('No', 'Chose No')

def click_askyesnocancel(): 
    res = messagebox.askyesnocancel('Ask', 'Message')
    if res: messagebox.showinfo('Yes', 'Chose Yes')
    elif res is False: messagebox.showinfo('No', 'Chose No')
    elif res is None: messagebox.showinfo('Cancel', 'Chose Cancel')

Button(root, text='showwarning', command=click_showwarning).pack()
Button(root, text='info', command=click_info).pack()
Button(root, text='error', command=click_error).pack()
Button(root, text='ask', command=click_ask).pack()
Button(root, text='Ok cancel', command=click_okcancel).pack()
Button(root, text='Yes - No', command=click_askyesno).pack()
Button(root, text='Yes - No - Cancel', command=click_askyesnocancel).pack()

root.mainloop()
