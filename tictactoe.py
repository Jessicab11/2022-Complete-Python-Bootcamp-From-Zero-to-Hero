def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#first player chooses their playing piece
def piece_pick():
    piece = "wrong"
    #acceptable_value = ["O", "X"]
    while piece not in ["X", "O"]:
        piece = input("First player, choose X or O: ").upper()
        if piece not in ["X", "O"]:
            clear_output()
            print("Invalid input, please choose X or O.")  
    else:
        if piece == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

#who goes first
import random
def first_player():
    if random.randint(0,1) == 0:
        return "Player 2"
    else:
        return "Player 1"
    
#player chooses their position
def position_pick(board):
    pick = "wrong"
    while pick not in [1,2,3,4,5,6,7,8,9]:
        pick = int(input("Please choose a position 1-9."))
        if pick not in [1,2,3,4,5,6,7,8,9]:
            clear_output()
            print("Invalid input, please choose a position 1-9.")
    return pick

#win condition
def win_condition(board, mark):
    return((board[7] == mark and board[8] == mark and board[9] == mark or
            board[4] == mark and board[5] == mark and board[6] == mark or
            board[1] == mark and board[2] == mark and board[3] == mark or
            board[7] == mark and board[4] == mark and board[1] == mark or
            board[8] == mark and board[5] == mark and board[2] == mark or
            board[9] == mark and board[6] == mark and board[3] == mark or
            board[7] == mark and board[5] == mark and board[3] == mark or
            board[9] == mark and board[5] == mark and board[1] == mark))

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

game_on = True

while True:
    
    theboard = [' ']*10
    playermarker1, playermarker2 = piece_pick()
    turn = first_player()
    print(turn + ' will go first!')
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on == True:
        if turn == "Player 1":
            display_board(theboard)
            pick = position_pick(theboard)
            place_marker(theboard, playermarker1, pick)
            
            if win_condition(theboard, playermarker1):
                display_board(theboard)
                print("You win!")
                game_on = False
            else:
                turn = "Player 2"
                
        else:
            display_board(theboard)
            pick = position_pick(theboard)
            place_marker(theboard, playermarker2, pick)
            if win_condition(theboard, playermarker2):
                display_board(theboard)
                print("You win!")
                game_on = False
            else:
                turn = "Player 1"
    if not replay():
        break
