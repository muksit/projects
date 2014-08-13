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

def printboard():
	print board[1] +"|"+ board[2] +"|"+ board[3]
	print board[4] +"|"+ board[5] +"|"+ board[6]
	print board[7] +"|"+ board[8] +"|"+ board[9]

def startgame():
	print "Here is what the board positions look like:"
	print "1"  + "|" + "2"  + "|" + "3" 
	print "4"  + "|" + "5"  + "|" + "6" 
	print "7"  + "|" + "8"  + "|" + "9" 
	for i in range(10):
		if i%2 == 0:
			askplayer1()
			printboard()
			if checkwin() == True:
				print "Win! Player 2 sucks!"
				break
		else:
			askplayer2()
			printboard()
			if checkwin() == True:
				print "Win! Player 1 sucks!"
				break


def askplayer1():
	try:
		player1move = int(raw_input("player 1, where do you want to draw your X?"))
		if player1move in range(1,10) and board[player1move] == "_" or board[player1move] == " ":
			board[player1move] = "X"
		else:
			print "sorry that isn't a valid position please try again"
			askplayer1()

	except (ValueError):
		print "sorry that isn't a valid position please try again"
		askplayer1()

	
	

def askplayer2():
	try:
		player2move = int(raw_input("player 2, where do you want to draw your 0?"))
		if player2move in range(1,10)and board[player2move] == "_" or board[player2move] == " ":
			board[player2move] = "0"
		else:
			print "sorry that isn't a valid position please try again"
			askplayer2()

	except (ValueError):
		print "sorry that isn't a valid position please try again"
		askplayer2()
	


def checkwin():
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
		 


startgame()
