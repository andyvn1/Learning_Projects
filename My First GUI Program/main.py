from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

def button_clicked():
    global num
    my_label.config(text=input.get())


#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Entry
input = Entry(width=10)
input.grid(column=3, row=2)

#Button
button_2 = Button(text="Click Me", command=button_clicked)
button_2.grid(column=2, row=0)

window.mainloop()
