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


dei=['#','X','O','X','O','X','O','X','O','X']
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



def place_marker(board,marker,position):
	board[position]= marker 


def win_check(board,mark):
	return ((board[7] == mark and board[8] == mark and board[9] == mark)  
    (board[4] == mark and board[5] == mark and board[6] == mark) 
    (board[1] == mark and board[2] == mark and board[3] == mark) 
    (board[7] == mark and board[4] == mark and board[1] == mark) 
    (board[8] == mark and board[5] == mark and board[2] == mark) 
    (board[9] == mark and board[6] == mark and board[3] == mark) 
    (board[7] == mark and board[5] == mark and board[3] == mark) 
    (board[9] == mark and board[5] == mark and board[1] == mark))


import random

def choose_first():
	if random.randint(0,1)==0:
		return 'Player 2'
	else:
		return 'Player 1'


def space_check(board,position):
	board[position]==' '


def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
		return True

def player_choice(board):
	position=0

	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
		 position=int(input("Choose your next position: (1-9): "))

	return position



def replay():
	return input("Do you want to play again? Enter Yes/no").lower().startswith('y')


print("Welcome to Tic-Tac-Toe !")

while True:
	theboard=[' ']*10
	player1_marker,player2_marker=player_input()
	turn=choose_first()
	print(turn + "will go first.")

	play_game=input("Are you ready to play? Enter yes or no: ")
	if play_game.lower()[0] == 'y':
		gameon=True
	else:
		gameon=False


	while gameon:
		if turn=='Player 1':
			display_board(theboard)
			position=player_choice(theboard)
			place_marker(theboard,player1_marker,position)

			if win_check(theboard,player1_marker):
				display_board(theboard)
				print("Congratulations! You have won the game")
				gameon=False
			else:
				if full_board_check(theboard):
					display_board(theboard)
					print("The game is a draw")
					break
				else:
					turn='Player 2'		


	else:

		display_board(theboard)
		position=player_choice(theboard)
		place_marker(theboard,player2_marker,position)

		if win_check(theboard,player2_marker):
			display_board(theboard)
			print("Player 2 has won the game!!")
			gameon=False
		else:
			if full_board_check(theboard):
				display_board(theboard)
				print("The game is a draw")
				break
			else:
				turn='Player 1'

	if not replay():
		break

   



		






