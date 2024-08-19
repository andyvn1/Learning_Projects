from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    numbers_list = [random.choice(numbers) for num in range(random.randint(2, 4))]
    symbols_list = [random.choice(symbols) for sym in range(random.randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, string=f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    if len(website_entry.get()) == 0 or len(username_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Empty Fields", message="One or more input fields are empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website_entry.get()}", message=f"These are the details entered:\n"
                                                                               f"Email: {username_entry.get()}\n"
                                                                               f"Password: {password_entry.get()}\n"
                                                                               f"Is it ok to save? ")
        if is_ok:
            with open("datta.txt", mode="a") as data:
                s = f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}"
                data.write("\n")
                data.write(s)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#creating canvas
canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

#entries and labels -Website -Email/Username -Password
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
username_entry = Entry(width=39)
username_entry.insert(0, "JohnDoe@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Buttons
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=36, highlightthickness=0, command=add)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
