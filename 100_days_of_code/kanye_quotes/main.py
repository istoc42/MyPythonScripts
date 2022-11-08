from tkinter import *
import requests

def get_quote():
    # Make a get() request to API
    response = requests.get("https://api.kanye.rest", verify=False) # Only use 'verify=False' at work
    
    # Raise an exception if the request returned an unsuccessful status code
    response.raise_for_status()
    
    # Parse JSON to obtain qoute text
    new_quote = response.json()["quote"]

    # Display quote in the quote_text widget
    canvas.itemconfig(quote_text, text=new_quote)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="kanye_quotes\\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye_quotes\\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()