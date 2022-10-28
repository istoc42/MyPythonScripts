from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    #Turn fields into string
    new_entry = f'\n{website_input.get()} | {email_user_input.get()} | {password_input.get()}'
    print(new_entry)
    
    is_ok = messagebox.askokcancel(title=f"{website_input.get()}", message=f"Details entered: \n\nWebsite: {website_input.get()}\nEmail: {email_user_input.get()}\nPassword: {password_input.get()}\n\nSave to Passwords.txt?")
    
    if is_ok:
        #Write the string to a file
        f = open("password-manager/passwords.txt", "a")
        f.write(new_entry)
        f.close()
        
        #Delete contents of previous entry
        website_input.delete(0,'end')
        password_input.delete(0,'end')
        
        #Place cursor back to starting position
        website_input.focus()

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

generate_pass_btn = Button(text="Generate")
generate_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()