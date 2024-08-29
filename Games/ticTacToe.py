#A python program to simulate the Tic Tac Toe Game.

#A tic tac toe consists of a matric of 3 rows and 3 coloumns

import os

#By default the marks to be used by both players are hardcoded
P1_mark = 'X'
P2_mark = 'O'

#Function to initialize the game board at the start of every new game
def initialize_board():
	game_board = {'1':' ', '2':' ', '3': ' ',
			      '4':' ', '5':' ', '6': ' ',
			      '7':' ', '8':' ', '9':' '}
	return game_board

#Dispplay function to display the tic tac toe board.
def display_board(board):
	os.system('cls')
	print(board['1']+" |"+board['2']+" |"+board['3'])
	print("--|--|--")
	print(board['4']+" |"+board['5']+" |"+board['6'])
	print("--|--|--")
	print(board['7']+" |"+board['8']+" |"+board['9'])
	return None


#Start by checking if players want to play
def check_intention():
	play_choice = 'Wrong'
	while play_choice == 'Wrong':
		choice = input("Do you want to play the game of Tic Tac Toe? (Y or N):")
		if choice == 'Y':
			play_choice = 'Right'
			setup_players()
		elif choice == 'N':
			print("Thank you for your time. GOODBYE!")
			break
		else:
			print("Choose only Y or N")
	return None


#Funtion to accept user input.
def setup_players():
	print("Lets Play TIC TAC TOE")
	print('\n'*5)
	game_board = initialize_board()
	player = input("Who wants to go first Player 1 or Player 2. Just enter the numbers 1 or 2: ")
	display_board(game_board)
	if player == '1':
		play_game(game_board, 'Player1')
	else:
		play_game(game_board, 'Player2')
	return None

#Check who won the game:
def check_win(B, M, CP):
	if (B['1'] == B['2'] == B['3'] == M or
		B['1'] == B['4'] == B['7'] == M or 
		B['1'] == B['5'] == B['9'] == M or
		B['4'] == B['5'] == B['6'] == M or
		B['7'] == B['8'] == B['9'] == M or
		B['7'] == B['5'] == B['3'] == M or
		B['3'] == B['6'] == B['9'] == M or
		B['2'] == B['5'] == B['8'] == M ):
		display_board(B)
		print("WE HAVE A WINNER!! CONGRATULATIONS "+CP)
		return True
	else:
		return False


#The Actual Game
def play_game(game_board, current_player):
	noOfTurns = 0
	board_pos = ['1','2','3','4','5','6','7','8','9']
	game = True
	while noOfTurns < 9 and game:
		print("TURN: "+current_player)
		pos = input("Please enter a position on board: ")
		if pos in board_pos and game_board[pos] == ' ':
			noOfTurns += 1
			if current_player == 'Player1':
				game_board[pos] = P1_mark
				display_board(game_board)
				if check_win(game_board, P1_mark, current_player):
					game = False
					break
				current_player = 'Player2'
			else:
				game_board[pos] = P2_mark
				display_board(game_board)
				if check_win(game_board, P2_mark, current_player):
					game = False
					break
				current_player = 'Player1'

		else:
			print("Position Not in range 1-9 or Position already Used")

	if noOfTurns == 9 and game:
		print("OOPS THE GAME ENDED IN A DRAW")

	replay()
	return None

#Code to check if player want to replay
def replay():
	ch = input("Do you want to play again 'Y' or 'N': ")
	if ch == 'Y':
		os.system('cls')
		setup_players()
	else:
		print("THANKS FOR PLAYING GOODBYE")
	return None

#Introduction to the game:
def introduce_game():
	os.system('cls')
	print("****************WELCOME TO THE GAME OF TIC TAC TOE****************")
	print("This is a 2 player game. Both players have to play on a single computer")
	print("Player 1 is assigned 'X' and Player 2 is assigned 'O'")
	print("The positions on the board are same as a Telephone Dial Pad")
	print("To play each player needs to choose between 1-9. Player cannot use an already played position")
	print("The player who completes a mark in 3 positions either Horizontally, Vertically or Diagonally wins the game. Or it will be a draw")
	check_intention()

introduce_game()