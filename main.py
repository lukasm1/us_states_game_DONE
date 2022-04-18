import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(height=491, width=725)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.listen()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) != 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    print(type(answer_state))

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # Option w CSV MDL>
    #    with open("50_states.csv") as states:
    #        states_data = csv.reader(states)
    #
    #        for row in states_data:
    #            if row[0] == answer_state:
    #                guessed_states.append(answer_state)
    #                t = turtle.Turtle()
    #                t.hideturtle()
    #                t.penup()
    #                t.goto(float(row[1]), float(row[2]))
    #                t.write(answer_state)

    #        else:
    #            pass
    # OPTION w PANDAS>

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# def get_mouse_click_coor(x, y):
#    print(x, y)

# screen.onscreenclick(get_mouse_click_coor)

screen.mainloop()
