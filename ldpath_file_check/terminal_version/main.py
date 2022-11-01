from os import listdir
from os.path import isfile, join
import pandas as pd
from tkinter import *
from tkinter import messagebox

# ---------------------------- FILE NAME READER ------------------------------- #

#Ask for file path
file_path = input("Please enter file path to read files from:")

# Using input prompt
file_list = [f for f in listdir(file_path) if isfile(join(file_path, f))]

# Hardcoded file path
# files = [f for f in listdir("L:\Cellular_Pathology\TalkingPoint Server\Outsourcing\Import Completed") if isfile(join("L:\Cellular_Pathology\TalkingPoint Server\Outsourcing\Import Completed", f))]

# ---------------------------- EXPORT AS CSV / TXT ------------------------------- #

df = pd.DataFrame(file_list, columns=["File name"])
df.to_csv('file_names.csv', index=False)

# # Write list to text file
# filenames = open("files.txt", "a")
# filenames.write(str(file_list))
# filenames.close()