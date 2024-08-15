import pandas
import turtle

STATES_DATA_FILE = "50_states.csv"
MISSED_STATES_FILE = "missed_states.csv"
STATE_COL = "state"
X_COL = "x"
Y_COL = "y"
ALIGN = "center"
FONT = ("calibri", 8, 'normal')
EXIT_GAME = "exit"


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

guessed_states = []

data = pandas.read_csv(STATES_DATA_FILE)
all_states = [state.lower() for state in data[STATE_COL].values]
total_states = len(all_states)


def write_missed_states(correct_guesses):
    """
    Function to write the users missed states into a file for them to learn later.
    :param correct_guesses: The correctly guessed states being recorded by the system as the user plays the game.
    :return: None
    """
    missed_states = [state for state in data[STATE_COL].values if state not in correct_guesses]
    # for state in data[STATE_COL].values:
    #     if state not in correct_guesses:
    #         missed_states.append(state)
    # missed_states_dict = {
    #     "Missing States": missed_states
    # }
    missing_states_df = pandas.DataFrame(missed_states)
    missing_states_df.to_csv(MISSED_STATES_FILE)


def state_not_guessed(guess: str, guessed: list) -> bool:
    """
    Function to check if the user has already correctly guessed the state.
    :param guess: The user's current guess
    :param guessed: The list of all correctly guessed states made by the user
    :return: Boolean to indicate if state has not been guessed yet.
    """
    for state in guessed:
        if guess.lower() == state.lower():
            return False
    return True


first_attempt = True

while len(guessed_states) < total_states:

    if first_attempt:
        pop_up_title = f"Guess the State"
        first_attempt = False
    else:
        pop_up_title = f"{len(guessed_states)}/{total_states} States Correct"

    answer_state = screen.textinput(title=pop_up_title, prompt="What's another state's name?").lower()

    if answer_state.lower() == EXIT_GAME:
        write_missed_states(guessed_states)
        exit()

    for state in data[STATE_COL].values:

        if answer_state == state.lower() and state_not_guessed(answer_state, guessed_states):
            guessed_states.append(state)
            x_coord = data[state == data[STATE_COL]][X_COL].item()
            y_coord = data[state == data[STATE_COL]][Y_COL].item()
            writer.goto(x_coord, y_coord)
            writer.write(f"{state}", align=ALIGN, font=FONT)

turtle.mainloop()

