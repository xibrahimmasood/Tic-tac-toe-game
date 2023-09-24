#Tic tac toe game

def display_board(board):
    print('\n'* 100)
    print('   |   |')
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
def player_input():
    marker = 'dffdvfd'
    while marker not in ['X','O']:
        marker = input('Do you want to be X or O:  ').capitalize()
        
        if marker not in ['X','O']:
            print('Invalid Choice')
    if marker == 'X':
        return ['X','O']
    else:
        return ['O','X']
    
def place_marker(board,marker,position):
    board[position] = marker 

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in list(range(1,10)) or not space_check(board,position):
        position = int(input('Choose your position (1-9): '))
        return position
    
def replay():
    return input('Do you wishto continue ? Yes or No').lower()[0] == 'y'

print('Welcome to tic tac toe! ')

while True:
    theboard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first ')

    play_game = input('Are you ready to play the game. Enter Yes or No ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1_marker, position)
    
        if win_check(theboard,player1_marker):
            display_board(theboard)
            print('Congrats player 1 has won the game')
            game_on = False
    
        else:
            if full_board_check(theboard):
                display_board(theboard)
                print('The game is draw')
                break
            else:
                turn = 'Player 2'
    
        if turn == 'Player 2':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,player2_marker,position)

        if win_check(theboard, player2_marker):
            display_board(theboard)
            print('Player 2 has won! ')
            game_on = False

        else:
            if full_board_check(theboard):
                display_board(theboard)
                print('The game is draw')
                break
            else:
                turn = 'Player 1'
    if not replay():
        break



    



