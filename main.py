from turtle import Screen, Turtle
import pandas
from state_names import StateNames

screen = Screen()
screen.tracer(0)
turtle = Turtle()
screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.update()
state_names = StateNames()
states_found = []


while len(states_found) < 49:
    screen.update()
    user_input = screen.textinput(title=f"you guessed {len(states_found)}/50", prompt="name a state".title())
    state_data = pandas.read_csv("50_states.csv", index_col=None)
    all_states = state_data.state.to_list()

    if user_input is None:
        missing_states = [state for state in all_states if state not in states_found]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    for state in all_states:
        if user_input.lower() == state.lower():
            x_val = int(state_data[state_data.state == state].x)
            y_val = int(state_data[state_data.state == state].y)
            states_found.append(state)
            state_names.write_state(x_val, y_val, state)

screen.mainloop()