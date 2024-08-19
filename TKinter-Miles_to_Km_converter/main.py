from tkinter import *

#This app is a UI using Tinker that help convert miles to kilometers.

screen = Tk()
screen.title("Mile to Km Converter")
screen.minsize(width=300, height=50)
screen.config(padx=60, pady=10)
km = 0


def calculator():
    km = float(entry_box.get()) * 1.609344
    output_label.config(text=f"{round(km)}")


#Entry and label
entry_box = Entry(width=10)
entry_box.grid(column=1, row=0)

label = Label(text="Miles")
label.grid(column=2, row=0)

#output labels
operator_label = Label(text="is equal to")
operator_label.grid(column=0, row=1)

output_label = Label(text=f"0")
output_label.grid(column=1, row=1)

output_unit_label = Label(text="Km")
output_unit_label.grid(column=2, row=1)

#Calculate button
button = Button(text="Calculate", command=calculator)
button.grid(column=1, row=2)

screen.mainloop()
