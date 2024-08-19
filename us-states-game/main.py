import turtle
import pandas

#Gui that read user input and position the name of the State in each respective state in the map and then write
# the missing states to a csv file


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

tex_box = turtle.Turtle()
tex_box.penup()
tex_box.hideturtle()
list_of_state = []
guess_list = []
guess = 0

while not guess == 51:
    if guess == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(title=f"Guess {len(guess_list)}/50",
                                        prompt="What's another state's name?").title()
    list_of_state = data["state"].tolist()

    if answer_state == "Exit":
        break

    if list_of_state.__contains__(answer_state):

        state_row = data[data["state"] == answer_state].to_dict()
        state = state_row["state"][data[data["state"] == answer_state].index[0]]
        x_cor = state_row["x"][data[data["state"] == answer_state].index[0]]
        y_cor = state_row["y"][data[data["state"] == answer_state].index[0]]

        tex_box.goto(x_cor, y_cor)
        tex_box.write(state, align="left")

        guess_list.append(state)
        guess += 1

    elif len(guess_list) == 50:
        turtle.write("Congratulations You Win", align="center", font=("Aerial", 20, "normal"))
        guess = 51

states_to_learn = []
for state in list_of_state:
    if state not in guess_list:
        states_to_learn.append(state)
df = pandas.DataFrame(states_to_learn)
df.to_csv("states_missing.csv")
