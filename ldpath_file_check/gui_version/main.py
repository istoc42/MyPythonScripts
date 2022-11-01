from os import listdir
from os.path import isfile, join
import pandas as pd
from tkinter import *
from tkinter import messagebox

# ---------------------------- FILE NAME READER ------------------------------- #

#Ask for file path
# file_path = input("Please enter file path to read files from:")

# Using input prompt
# file_list = [f for f in listdir(file_path) if isfile(join(file_path, f))]

# Hardcoded file path
# files = [f for f in listdir("L:\Cellular_Pathology\TalkingPoint Server\Outsourcing\Import Completed") if isfile(join("L:\Cellular_Pathology\TalkingPoint Server\Outsourcing\Import Completed", f))]

# ---------------------------- EXPORT AS CSV / TXT ------------------------------- #

# df = pd.DataFrame(file_list, columns=["File name"])
# df.to_csv('file_names.csv', index=False)

# # Write list to text file
# filenames = open("files.txt", "a")
# filenames.write(str(file_list))
# filenames.close()

# ---------------------------- UI SETUP ------------------------------- #
FONT = "Arial", 14

window = Tk()
window.title("File Name Reader")
window.config(width=650, height=500, padx=40, pady=40)

input_label = Label(text="Enter directory to read: ", font=FONT)
input_label.grid(column=0, row=1)

output_label = Label(text="Enter output directory: ", font=FONT, justify="left")
output_label.grid(column=0, row=3)

input_entry = Text(height=3)
input_entry.grid(column=0, row=2, )
input_entry.focus()

output_entry = Text(height=3)
output_entry.grid(column=0, row=4, )

generate_csv_btn = Button(text="Generate CSV", font=FONT)
generate_csv_btn.grid(column=0, row=5, columnspan=2)



window.mainloop()