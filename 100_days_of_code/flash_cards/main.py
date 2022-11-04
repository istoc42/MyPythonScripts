from tkinter import *
from pandas import *

BACKGROUND_COLOUR = "#b1ddc6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900
# ---------------------------- FUNCTIONALITY ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOUR)
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+50+50')

canvas = Canvas(width=800, height=526, bd=0, bg=BACKGROUND_COLOUR, highlightthickness=0)
card_front_img = PhotoImage(file=f"flash_cards\images\card_front.png")
canvas.create_image(400, 0, image=card_front_img, anchor="n")
canvas.create_text(400, 150, text="Russian", font=LANGUAGE_FONT)
canvas.create_text(400, 263, text="хорошо", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

wrong_btn_img = PhotoImage(file=f"flash_cards\images\wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0)
wrong_btn.grid(column=0, row=1)

right_btn_img = PhotoImage(file=f"flash_cards/images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0)
right_btn.grid(column=1, row=1)

window.mainloop()