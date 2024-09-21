from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#b1ddc6"
FONT_NAME = "Ariel"
current_card = {}
words = {}

# --------------- FLASHCARD CONTROL ------------ #


def change_flashcard():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{current_card["French"]}", fill="black")
    canvas.itemconfig(card_image, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card["English"]}", fill="white")


def is_known():
    words.remove(current_card)
    data = pd.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_flashcard()


# ----------------- READING CSV ------------------ #

try:
    data_csv = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data_csv = pd.read_csv("data/french_words.csv")
    words = original_data_csv.to_dict(orient="records")
else:
    words = data_csv.to_dict(orient="records")

# ------------------ UI SETUP ------------------- #

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 293, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
correct_button = Button(image=right_image, highlightthickness=0, command=is_known)
correct_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=wrong_image, highlightthickness=0, command=change_flashcard)
incorrect_button.grid(column=0, row=1)

change_flashcard()

window.mainloop()
