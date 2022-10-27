from tkinter import *

window = Tk()
window.title("Grid challenge")
window.minsize(width=500, height=500)
window.config(padx=120, pady=220)

lbl = Label(text="Label!", font=("Arial", 24, "bold"))
lbl.grid(column=0, row=0)
lbl.config(padx=50, pady=50)

btn1 = Button(text="Button 1")
btn1.grid(column=1, row=1)

btn2 = Button(text="Button 2")
btn2.grid(column=2, row=0)

input = Entry(width=20)
input.grid(column=3, row=2)

window.mainloop()