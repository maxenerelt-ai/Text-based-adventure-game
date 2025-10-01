# ME CC SN SP 6th Tic Tac Toe

import random
# Variables
user_input = input("Hey welcome to our tic tac toe game please choose X or O please!").capitalize() 
numbers_avaliable = [1,2,3,4,5,6,7,8,9]
turns = 1
board = ["-","-","-","-","-","-","-","-","-"]
game_end = False 
ai_choice = "0"
player_choice = "0"
if user_input == "X":
    ai_choice = "O"
elif user_input == "O":
    ai_choice = "X"


#User input Max
if user_input == "X":
    print("You picked X!")
elif user_input == "O":
    print("You picked O!")
else:
    print("You picked neither O or X, please pick O or X PLEASE!")

#Tic tac toe Board Santi

def game_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

def change_board(num, turn):
    num = num - 1
    if num == 0:
        board[0] = turn    
    elif num == 1:
        board[1] = turn
    elif num == 2:
        board[2] = turn
    elif num == 3:
        board[3] = turn
    elif num == 4:
        board[4] = turn
    elif num == 5:
        board[5] = turn
    if num == 6:
        board[6] = turn
    if num == 7:
        board[7] = turn
    elif num == 8:
        board[8] = turn
    
    
while game_end == False: 
    if turns % 2 == 1 and user_input == "X":
        game_board()
        player_choice = int(input("Choose a number from 1 to 9?"))
        if player_choice >= 1 or player_choice <= 9:
            change_board(player_choice, user_input) 
            turns += 1
    elif turns % 2 == 1 and user_input == "O":
        game_board
        player_choice = int(input("Choose a number from 1 to 9?"))
        if player_choice >= 1 or player_choice <= 9: 
            change_board(player_choice, user_input)
        turns += 1
        
    else:
        game_board()
        ai_pick = random.choice(numbers_avaliable)
        if ai_pick == player_choice:
            ai_pick = random.choice(numbers_avaliable)
            change_board(ai_pick, ai_choice)
            turns +=1
        else:
            change_board(ai_pick, ai_choice)
            turns +=1
        

        

#winning combos Charlie 
def winner_combos(player): 
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False
while game_end == False: 
    if turns % 2 == 1 and user_input == "X":
        game_board()
        player_choice = int(input("Choose a number from 1 to 9?"))
        if 1 <= player_choice <= 9 and player_choice in numbers_avaliable:
            change_board(player_choice, user_input) 
            numbers_avaliable.remove(player_choice)
            if winner_combos(user_input):
                game_board()
                print("You win!")
                game_end = True
            turns += 1
#sophie
    elif turns % 2 == 1 and user_input == "O":
        game_board()
        player_choice = int(input("Choose a number from 1 to 9?"))
        if 1 <= player_choice <= 9 and player_choice in numbers_avaliable: 
            change_board(player_choice, user_input)
            numbers_avaliable.remove(player_choice)
            if winner_combos(user_input):
                game_board()
                print("You win!")
                game_end = True
            turns += 1
#sophie     
    else:
        game_board()
        ai_pick = random.choice(numbers_avaliable)
        change_board(ai_pick, ai_choice)
        numbers_avaliable.remove(ai_pick)
        if winner_combos(ai_choice):
            game_board()
            print("ai wins!")
            game_end = True
        turns +=1
    if turns > 9: 
        game_board()
        print("It's a tie!") 
        game_end = True
