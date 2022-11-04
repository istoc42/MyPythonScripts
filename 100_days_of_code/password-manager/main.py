from tkinter import *
from tkinter import messagebox
from random import choice, randint, sample
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_gen():
    
    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_numbers + pass_symbols
    password_string = ''.join(password_list)

    print("Characters generated: " + password_string)

    random_password = sample(password_list, len(password_list))
    random_password_string = ''.join(random_password)

    print(f'Your new password is: {random_password_string}')
    
    password_input.delete(0, 'end')
    password_input.insert(0, random_password_string)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    #Turn fields into string
    website_entry = website_input.get()
    email_entry = email_user_input.get()
    password_entry = password_input.get()
    new_data = {
        website_entry: {
            "email": email_entry,
            "password": password_entry,
        }
    }
    
    new_entry = f'\n{website_entry} | {email_entry} | {password_entry}'
    print(new_entry)
    
    if len(website_entry) == 0 or len(password_entry) == 0:
        messagebox.showerror("Oops!", "Please don't leave any fields empty!")
    else:
        #Write the string to a file
        try:
            with open("password-manager/passwords.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open("password-manager/passwords.json", "w") as data_file:
                #Saving new data            
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            
            with open("password-manager/passwords.json", "w") as data_file:
                #Update new data            
                json.dump(data, data_file, indent=4)
        finally:
            #Delete contents of previous entry
            website_input.delete(0,'end')
            password_input.delete(0,'end')
            
            #Place cursor back to starting position
            website_input.focus()
            
def find_password():
    website = website_input.get()
    # Check if website_entry matches an item in passwords.json
    try:
        with open("password-manager/passwords.json") as data_file:
            # Read passwords.json
            data = json.load(data_file)
    except FileNotFoundError:
        # Catch an exception that might occur trying to access the passwords.json showing a messagebox with the text "No Data File Found."
        messagebox.showerror(title="Error. File Not Found", message="No Data File Found.")
        # If yes, show a messagebox with the websites name and password
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
        else:
            # If website_entry does not exist inside the json, show a messagebox that reads "No details for the website exists."
            messagebox.showerror(title=f"Error. No details found for {website}.", message=f"No details for {website} exists.")

        
        
        
    
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="password-manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=41)
website_input.grid(column=1, row=1,columnspan=2)
website_input.focus()

email_user_input = Entry(width=41)
email_user_input.grid(column=1, row=2, columnspan=2)
email_user_input.insert(0, "shudso91@gmail.com")

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

search_btn = Button(text="Search", width=7, command=find_password)
search_btn.grid(column=2, row=1)

generate_pass_btn = Button(text="Generate", command=password_gen)
generate_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()