# -*- coding: utf-8 -*-
# function that can print out a board
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('- '+'- '+'- ')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('- '+'- '+'- ')
    print(board[1]+'|'+board[2]+'|'+board[3])
    
#function that can take in a player input and assign their marker as 'X' or 'O'
def player_input():
    choise='w'
    d={}
    while choise not in ['X','O']  :
        choise=input('Hello player1\ndo you want to be X or O: ')
        if choise == 'X':
            d['player2']='O'
            d['player1']=choise
        elif choise == 'O':
            d['player2']='X' 
            d['player1']=choise
        else:
            print('sorry a wrong input please choose X or O')
    return d   
#function that takes in the board list object
def place_marker(board, marker, position):
    board[position]=marker
#function that takes in a board and a mark (X or O) and then checks to see if that mark has won
def win_check(board, mark):
    if board[1]==board[2]==board[3]==mark or board[4]==board[5]==board[6]==mark or board[7]==board[8]==board[9]==mark or board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark or board[3]==board[6]==board[9]==mark or board[1]==board[5]==board[9]==mark or board[7]==board[5]==board[3]==mark:
        return True
    else:
        return False
        
# function that  randomly decide which player goes first    
import random

def choose_first():
    ran=random.randint(1,2)
    if ran==1:
        return 'player1'
    else:
        return 'player2'
# function that returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):
    if board[position] not in ['X','O']:
        return True
#function that checks if the board is full and returns a boolean value
def full_board_check(board):
    for x in board:
        if x in ['X','O']:
            pass
        else:
            return False
    return True  
#function that asks for a player's next position
def player_choice(board):
    position=0
    a='ert'
    while position not in range(1,10) or a==5  :
        position=input('choose your next step (1-9): ')
        if int(position) in range (1,10) :
                if space_check(board,int(position))==True :
                    return int(position)
                else:
                    print('This position is full please enter a diferent position')
                    a=5
                    
                    
        else:
            print('wrong input please enter a position (1-9)') 
#function that asks the player if they want to play again
def replay():
    choise='w'
    while choise  not in ['Y','N']:
        
        choise=input('do you want to play again? (Y or N): ')
        if choise == 'Y':
            return True
        elif choise == 'N':
            return False
        else:
            print('a wrong input choose Y or N')   
#function that asks the player if they ready to start play
def ready() :
    a='r'
    while a not in ['Y','N']:
        a=input('ready to play? (Y or N) ')
        if a == 'Y':
            return True
        elif a == 'N':
            return False
        else:
            print('a wrong input choose Y or N')  
#main 
print('Welcome to Tic Tac Toe!')
while True:
    
    

    board = ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    d=player_input()
    turn=choose_first()
    
    print(turn + ' will go first')
    play_game=ready()
    while play_game==True:
        if turn=='player1':
            display_board(board)
            
            position=player_choice(board)    
            place_marker(board, d[turn], position)
            if win_check(board,d[turn])==True:
                display_board(board)
                print(turn + ' win')
                
                play_game=False
            elif full_board_check(board)==True:
                display_board(board)
                print('the game is a draw')
                play_game=False
            else:
                turn='player2'
        else:
            display_board(board)
            
                
            position=player_choice(board)    
            place_marker(board, d[turn], position)
            if win_check(board,d[turn])==True:
                display_board(board)
                print(turn + ' win')
                play_game=False
            elif full_board_check(board)==True:
                display_board(board)
                print('the game is a draw')
                play_game=False
            else:
                turn='player1'
    if not replay():
        
         break
    