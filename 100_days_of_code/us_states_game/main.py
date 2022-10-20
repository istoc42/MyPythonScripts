import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
us_map = turtle.Turtle()
us_map.hideturtle()

s = pandas.read_csv("us_states_game/50_states.csv")

label = turtle.Turtle()
label.penup()
label.hideturtle()
font = ("Courier", 8, "normal")

score = 0
correct_answers = []

game_is_on = True
while game_is_on:
    # Show score in textinput title
    answer_state = screen.textinput(
        title=f"{score}/50 Guess the state", prompt="Name a state:").title()  # Text input must recognise answer in lower case.

    print(f"User entered: '{answer_state}'.")  # Answer verification
    if answer_state == "Exit":
        game_is_on = False
    # Check if answer already entered
    if answer_state not in correct_answers:
        # Check if answer from text input is inside the state table
        if answer_state in s.state.unique():
            print("Correct!")
            correct_answers.append(answer_state)  # Add to correct answer list

            score += 1     # Track score

            # Get coords from answer_state in csv
            state = s[s.state == answer_state]
            new_x = int(state.x)
            new_y = int(state.y)
            print(f'x: {new_x}, y: {new_y}')
            label.hideturtle()
            label.goto(new_x, new_y)

            # TODO Create turtle with state name travel to coords
            label.write(arg=f"{answer_state}", font=font)

    else:
        print(f"{answer_state} already entered.")

    # End game if score reaches 50/50
    if score >= 50:
        game_is_on = False

# Generate a list of states that were not guessed as a csv
states_to_learn = s.state.tolist()
for answer in correct_answers:
    states_to_learn.remove(answer)

states_to_learn_data = pandas.DataFrame(states_to_learn)
states_to_learn_data.to_csv("states_to_learn.csv")
