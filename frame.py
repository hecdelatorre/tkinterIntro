from tkinter import Tk, LabelFrame, Label, Button

root = Tk()
root.title('Frame')

# frame = LabelFrame(root, text='Login', padx=10, pady=10, borderwidth=3)
frame = LabelFrame(root, padx=20, pady=10, borderwidth=3)
frame.pack(padx=20, pady=20)

lb = Label(frame, text="I'm in a frame")
btn = Button(frame, text='Exit', command=root.quit)
lb.pack()
btn.pack()

root.mainloop()
