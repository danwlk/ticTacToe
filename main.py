from tkinter import *
import random


# Function to handle the next player's turn
def next_turn(row, column):
    global player

    # Check if the button is empty and there's no winner
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # Set the player's symbol on the button
        buttons[row][column]['text'] = player

        # Check for a winner or tie game
        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=("Player: " + players[0] if player == players[1] else players[1]))

        elif check_winner() is True:
            label.config(text=(players[0] + " WINS"))

        elif check_winner() == "TIE":
            label.config(text="TIE!")


# Function to check if there's a winner or a tie game
def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="yellow")
            buttons[row][1].config(bg="yellow")
            buttons[row][2].config(bg="yellow")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="yellow")
            buttons[1][column].config(bg="yellow")
            buttons[2][column].config(bg="yellow")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="yellow")
        buttons[1][1].config(bg="yellow")
        buttons[2][2].config(bg="yellow")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="yellow")
        buttons[1][1].config(bg="yellow")
        buttons[2][0].config(bg="yellow")
        return True

    elif not empty_spaces():
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="grey")
        return "TIE"

    else:
        return False


# Function to check if there are any empty spaces left
def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    return spaces != 0


# Function to start a new game
def new_game():
    global player

    # Randomly choose the starting player
    player = random.choice(players)
    label.config(text="Player: " + player)

    # Clear the buttons and their background colors
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


# Create the main window
window = Tk()
window.title("Tic-Tac-Toe")

# Define player symbols and set the starting player randomly
players = ["X", "O"]
player = random.choice(players)

# Initialize the 3x3 grid of buttons
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# Create and configure the player label
label = Label(text="Player: " + player, font=('Times', 40))
label.pack(side="top")

# Create a reset button to start a new game
reset_button = Button(text="Restart", font=('Times', 20), command=new_game)
reset_button.pack(side="top")

# Create a frame to hold the game grid
frame = Frame(window)
frame.pack()

# Create and arrange the buttons in the game grid
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('Times', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Start the Tkinter main event loop
window.mainloop()
