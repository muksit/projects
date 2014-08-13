board = {
		1 :'_',
		2 :'_',
		3 :'_',
		4 :'_',
		5 :'_',
		6 :'_',
		7 :' ',
		8 :' ',
		9 :' '
		}

def print_board():
	print board[1] +"|"+ board[2] +"|"+ board[3]
	print board[4] +"|"+ board[5] +"|"+ board[6]
	print board[7] +"|"+ board[8] +"|"+ board[9]

def start_game():
	print "Here is what the board positions look like:"
	print "1"  + "|" + "2"  + "|" + "3" 
	print "4"  + "|" + "5"  + "|" + "6" 
	print "7"  + "|" + "8"  + "|" + "9" 
	for i in range(10):
		if i%2 == 0:
			ask_player1()
			print_board()
			if check_win() == True:
				print "Win! Player 2 sucks!"
				break
		else:
			ask_player2()
			print_board()
			if check_win() == True:
				print "Win! Player 1 sucks!"
				break

def ask_player1():
	try:
		player1_move = int(raw_input("player 1, where do you want to draw your X?"))
		if player1_move in range(1,10) and (board[player1_move] == "_" or board[player1_move] == " "):
			board[player1_move] = "X"
		else:
			print "sorry that isn't a valid position please try again"
			ask_player1()

	except ():
		print "sorry that isn't a valid position please try again"
		ask_player1()	

def ask_player2():
	try:
		player2_move = int(raw_input("player 2, where do you want to draw your 0?"))
		if player2_move in range(1,10) and (board[player2_move] == "_" or board[player2_move] == " "):
			board[player2_move] = "0"
		else:
			print "sorry that isn't a valid position please try again"
			ask_player2()

	except (ValueError):
		print "sorry that isn't a valid position please try again"
		ask_player2()

def check_win():
	if board[1] == board [2] == board [3] and board[1] != "_" and board[1] != " ":
		return True
	elif board[4] == board [5] == board [6] and board[4] != "_" and board[4] != " ":	
		return True
	elif board[7] == board [8] == board [9] and board[7] != "_" and board[7] != " ":	
		return True
	elif board[1] == board [4] == board [7] and board[1] != "_" and board[1] != " ":	
		return True	
	elif board[2] == board [5] == board [8] and board[2] != "_" and board[2] != " ":	
		return True
	elif board[3] == board [6] == board [9] and board[3] != "_" and board[3] != " ":	
		return True
	elif board[1] == board [5] == board [9] and board[1] != "_" and board[1] != " ":	
		return True
	elif board[3] == board [5] == board [7] and board[3] != "_" and board[3] != " ":	
		return True
		 


if __name__ == '__main__':
   start_game()
