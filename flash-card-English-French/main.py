from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
words_to_learn = {}
data = {}


#---------------------------Functions---------------------------------------------#
def next_card():
    global current_card, flip
    window.after_cancel(flip)
    current_card = random.choice(data_dic)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(front_image, image=front_image_1)
    window.after(3000, func=back_flip)

def know_the_word():
    global words_to_learn
    data_dic.remove(current_card)
    words_to_learn = data_dic
    next_card()


def back_flip():
    canvas.itemconfig(front_image, image=back_image)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    window.after_cancel("flip")


#---------------------------------------------------UI-----------------------------------#
#creating the window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

flip = window.after(3000, func=back_flip)

#creating canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image_1 = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
front_image = canvas.create_image(400, 260, image=front_image_1)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#creating red button
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_button_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong.grid(column=0, row=1)

#creating green button
right_button_image = PhotoImage(file="images/right.png")
right = Button(image=right_button_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=know_the_word)
right.grid(column=1, row=1)

#---------------------------------------------------------------reading csv-------------------------------------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_dic = data.to_dict(orient="records")

next_card()

window.mainloop()

print(words_to_learn)
df = pandas.DataFrame(words_to_learn)
df.to_csv("data/words_to_learn.csv", index=False)
