                                            # Tic Tac Toe 
#for two player

#importing required libraries
import random
import os


#for clearind output screen 
clear_output = lambda : os.system('clear') #'clear' for Terminal and 'cls' for cmd

#first functions are defined 

#for displaying Tic Tac Toe Board
def display_board(board):
    clear_output()
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('-----------')
    print(f' {board[7]} | {board[8]} | {board[9]} ')    


#taking input from player for selecting their marker
def player_input():
    player = ''
    while player != 'X' and player != 'O':
        player = input("Please pick a marker 'X' or 'O' : ").upper()
    if player == 'X':
        return ('X','O')
    else:
        return ('O', 'X')

#allocated marker to that position
def place_marker(board, marker, position):
    board[position] = marker


#checks for which players wins or match is drawn
def win_check(board, mark):
    return (board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark or
            board[7] == board[8] == board[9] == mark or board[1] == board[4] == board[7] == mark or
            board[2] == board[5] == board[8] == mark or board[3] == board[6] == board[9] == mark or
            board[1] == board[5] == board[9] == mark or board[3] == board[5] == board[7] == mark)


#randomly chooses the player which player's first turn
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


#checks postion of board is empty or not
def space_check(board, position):
    return board[position] == ' '


#checks the board is empty or not
def full_board_check(board):
    for x in range(1, 10):
        if  space_check(board, x):
            return False
    return True


#asks player for postion to mark their mark on the board
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose the position between 1-9 : '))
    return position

#simply returns true 
def reply():
    return True


#main program starts here



board = [0,1,2,3,4,5,6,7,8,9]
display_board(board)              #displays position layout
print('\nWelcome to Tic Tac Toe!')
print('\nPosition Chart')

while True:
    board = [' ']*10		  #initially displaying empty board
    turn = choose_first()         #randomly choosing player's turns
    print('\n' + turn + ' First Turn\n')
    

	#allocate markers according to player's choice whose turn's first
    if turn == 'Player 1':
        player1_marker, player2_marker = player_input()
    else:
        player2_marker, player1_marker = player_input()
    
    game_on = True
    
    	
	#game play stars from here

    while game_on:
        
        #Player1 Turn
        if turn == 'Player 1':
            
            display_board(board)   #initially displaying board
	        
            print('\n' + turn + ' Turn\n')
	        
            position = player_choice(board) #marker's position is stored in posiyion variable

	    #it checks that postion given by player is empty or not if empty then allocate that position to player's marker
            place_marker(board, player1_marker, position) 
            
            if full_board_check(board): #check's board is filled or not
                
                display_board(board)
	            
                print('\nMatch Tie\n')
                game_on = False
                
            elif win_check(board, player1_marker): #checks that player win or not
                
                display_board(board)
                print('\nCONGRATULATIONS ! Player 1 Won\n')
		        
                game_on = False
            
            else:	#if both the above condition does not satify then it should be player 2 turn

                turn = 'Player 2'
        
        else:
            
            display_board(board)	#initially displaying board
	        
            print('\n' + turn + ' Turn\n')
	        
            position = player_choice(board) #marker's position is stored in posiyion variable

	    #it checks that postion given by player is empty or not if empty then allocate that position to player's marker
            place_marker(board, player2_marker, position)
            
            if full_board_check(board): #check's board is filled or not
                
                display_board(board)
                
                print('\nMatch Tie\n')
                game_on = False
                
            elif win_check(board, player2_marker): #checks that player win or not
                
                display_board(board)
	    	    
                print('\nCONGRATULATIONS ! Player 2 Won\n')
                game_on = False
            
            else:	 #if both the above condition does not satify then it should be player 2 turn
                
                turn = 'Player 1'
                
    result = input('Do you want again, Enter Yes or No : ').capitalize() #ask the players if they want to play again 
        
    if result == 'Yes':
            reply()
    else:
        break # comes out of the loop and end the program


#OUTPUT:

'''

sanket@sanket-X555LAB:~/Documents/py$ python TicTacToe.py 
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 

Welcome to Tic Tac Toe!

Position Chart

Player 1 First Turn

Please pick a marker 'X' or 'O' : x
   |   |   
-----------
   |   |   
-----------
   |   |   

Player 1 Turn

Choose the position between 1-9 : 1
 X |   |   
-----------
   |   |   
-----------
   |   |   

Player 2 Turn

Choose the position between 1-9 : 9
 X |   |   
-----------
   |   |   
-----------
   |   | O 

Player 1 Turn

Choose the position between 1-9 : 3
 X |   | X 
-----------
   |   |   
-----------
   |   | O 

Player 2 Turn

Choose the position between 1-9 : 2
 X | O | X 
-----------
   |   |   
-----------
   |   | O 

Player 1 Turn

Choose the position between 1-9 : 7
 X | O | X 
-----------
   |   |   
-----------
 X |   | O 

Player 2 Turn

Choose the position between 1-9 : 5
 X | O | X 
-----------
   | O |   
-----------
 X |   | O 

Player 1 Turn

Choose the position between 1-9 : 4
 X | O | X 
-----------
 X | O |   
-----------
 X |   | O 

CONGRATULATIONS ! Player 1 Won

Do you want again, Enter Yes or No : no       
sanket@sanket-X555LAB:~/Documents/py$ 


'''