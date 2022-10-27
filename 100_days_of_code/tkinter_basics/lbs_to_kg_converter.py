from tkinter import *

window = Tk()
window.title("Pounds to Kilos Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

result = 0

def calculate_kgs():
    print("Button clicked")
    lbs = int(lbs_input.get())
    kgs_result = lbs * 0.45359237
    print(type(lbs))
    print(type(kgs_result))
    result_label.config(text=round(kgs_result, 2))
    

# Labels
lbs_label = Label(text="lbs", font=("Arial", 14))
lbs_label.grid(column=2, row=0)

kgs_label = Label(text="kgs", font=("Arial", 14))
kgs_label.grid(column=2, row=1)

input_label = Label(text="is equal to", font=("Arial", 14))
input_label.grid(column=0, row=1)

result_label = Label(text=result, font=("Arial", 14))
result_label.grid(column=1, row=1)

# Button
button = Button(text="Calculate", command=calculate_kgs, width=24)
button.grid(column=1, row=2)

# Input
lbs_input = Entry(width=15, font=("Arial", 14), justify="center")
lbs_input.grid(column=1, row=0)

window.mainloop()