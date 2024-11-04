import pandas as pd
from tkinter import *
import random

BACKGROUND = '#b1ddc6'
FRONT = '#d8efd3'
BACK = '#95d2b3'
TITLE_FONT = ("Georgia", "28", "bold")
WORD_FONT = ("Helvetica", "18", "italic")

df = pd.read_csv('./data/french_words.csv')
to_learn = df.to_dict(orient="records")
current_card = {}
print(to_learn)


def next_card():
    global flip_timer, current_card
    display.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = display.after(3000, func=unknown)


def unknown():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn_csv", index=False)
    next_card()


display = Tk()
display.title("Flash Cards")
display.config(padx=50, pady=50, background=BACKGROUND)

flip_timer = display.after(3000, func=unknown)

canvas = Canvas(width=800, height=576)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=TITLE_FONT)
card_word = canvas.create_text(400, 250, text="", font=WORD_FONT)
canvas.config(background=BACKGROUND, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, command=unknown)
wrong.grid(row=1, column=0)

correct_img = PhotoImage(file="./images/right.png")
correct = Button(image=correct_img, highlightthickness=0, command=is_known)
correct.grid(row=1, column=1)

next_card()

display.mainloop()
