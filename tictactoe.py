# ME CC SN SP 6th Tic Tac Toe

import random

# Variables (everyone)
user_input = input("Hey, welcome to our tic tac toe game! Please choose X or O: ").upper()
numbers_available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turns = 1
board = ["-"] * 9
game_end = False
ai_choice = "O" if user_input == "X" else "X"

# Validate user input (Max)
if user_input == "X":
    print("You picked X!")
elif user_input == "O":
    print("You picked O!")
else:
    print("You picked neither O nor X, please pick O or X next time!")
    exit()

# Print the tic-tac-toe board (Santi)
def game_board():
    print()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()

# Board position change (Charlie)
def change_board(num, turn):
    board[num - 1] = turn

# Check for winner (Santi)
def winner_combos(player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

# Main game loop 
while not game_end: #(Charlie)
    game_board()

    if turns % 2 == 1:
        # Player's turn
        try:
            player_choice = int(input("Choose a number from 1 to 9: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if player_choice in numbers_available:
            change_board(player_choice, user_input)
            numbers_available.remove(player_choice)

            if winner_combos(user_input): #(Sophie)
                game_board()
                print("Congrats! You win! The opponent loses!")
                game_end = True
            else:
                turns += 1
        else:
            print("Invalid move! That number is taken or out of range.")
    else:
        # AI's turn (Sophie)
        ai_pick = random.choice(numbers_available)
        print(f"Opponent chooses: {ai_pick}")
        change_board(ai_pick, ai_choice)
        numbers_available.remove(ai_pick)

        if winner_combos(ai_choice):
            game_board()
            print("The opponent wins!")
            game_end = True
        else:
            turns += 1