from tkinter import *
import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
# csv reading
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

french_word_dictionary = data.to_dict(orient="records")
french_word = {}
# print(french_word_dictionary)


def know_card():
    global french_word, french_word_dictionary
    french_word_dictionary.remove(french_word)
    generate_word()
    df = pandas.DataFrame(french_word_dictionary)
    df.to_csv("./data/words_to_learn.csv")


def flip_card():
    global after_id
    window.after_cancel(after_id)
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(english_text, text=french_word["English"], fill="white")
    after_id = window.after(3000, flip_card)


def generate_word():
    global french_word, french_word_dictionary
    french_word = random.choice(french_word_dictionary)
    canvas.itemconfig(image, image=card_front)
    canvas.itemconfig(title_text, text=f"French", fill="black")
    canvas.itemconfig(english_text, text=french_word["French"], fill="black")
    window.after(3000, flip_card)


# user Interface
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)
after_id = window.after(3000, flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
image = canvas.create_image(410, 260, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
english_text = canvas.create_text(400, 300, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
check_button = Button(image=right_image, command=know_card)
check_button.grid(row=1, column=1)

cross_button = Button(image=wrong_image, command=generate_word)
cross_button.grid(row=1, column=0)

generate_word()


window.mainloop()