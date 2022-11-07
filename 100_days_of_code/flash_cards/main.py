from tkinter import *
from pandas import *
from random import choice

BACKGROUND_COLOUR = "#b1ddc6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 30, "bold")
WINDOW_HEIGHT = 750
WINDOW_WIDTH = 900
current_card = {}
to_learn = {}

# ---------------------------- FUNCTIONALITY ------------------------------- #

# Read the data from russian_words.csv in the data folder
try:
    data = read_csv("flash_cards/data/phrases_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("flash_cards/data/russian_phrases.csv")    
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():    
    # Pick a RANDOM russian word and put it in the flash card.
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    
    # When you press the right or wrong buttons, its should generate a new random word
    canvas.itemconfig(card_title, text="Russian", fill="#000000")
    canvas.itemconfig(card_word, text=current_card["Russian"], fill="#000000")
    canvas.itemconfig(card_bg, image=card_front_img)
    
    # After a 3000ms delay flip the card and display the english translation
    flip_timer = window.after(10000, flip_card)

def flip_card():
    # Card image should change to card_back.png, text colour to white, title from english to french.
    canvas.itemconfig(card_title, text="English", fill="#ffffff")
    canvas.itemconfig(card_word, text=current_card["English"], fill="#ffffff")
    canvas.itemconfig(card_bg, image=card_back_img)

def is_known():
    to_learn.remove(current_card)    
    data = DataFrame(to_learn)
    data.to_csv("flash_cards/data/phrases_to_learn.csv", index=False)
    next_card()
    


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOUR)
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+50+50')

flip_timer = window.after(10000, flip_card)

canvas = Canvas(width=800, height=526, bd=0, bg=BACKGROUND_COLOUR, highlightthickness=0)
card_front_img = PhotoImage(file=f"flash_cards\images\card_front.png")
card_back_img = PhotoImage(file=f"flash_cards\images\card_back.png")
card_bg = canvas.create_image(400, 0, image=card_front_img, anchor="n")
card_title = canvas.create_text(400, 150, text="Russian", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="хорошо", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

wrong_btn_img = PhotoImage(file=f"flash_cards\images\wrong.png")
wrong_btn = Button(image=wrong_btn_img, borderwidth=0, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

right_btn_img = PhotoImage(file=f"flash_cards/images/right.png")
right_btn = Button(image=right_btn_img, borderwidth=0, highlightthickness=0, command=is_known)
right_btn.grid(column=1, row=1)

next_card()

window.mainloop()