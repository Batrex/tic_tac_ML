#take the output from the game and give it to the player, then take the output from the player 
#and give it to the game, and soo forth.
from G1 import get_G1_move,train 
from game import next_game_state,initialise
from game import WIN,LOSE,CONT,SCRAM 
from player import display_game_state,get_player_move
G1 = 0
human = 1




def playgame (player1_input,player2_input):
	player1 = player1_input
	player2 = player2_input
	player_type = player1
	gamestate,player,winlose = initialise()
	move = 0
	'''
	the difference between player and currrent player is:
	player_type stores whether the player is a Ai (ie G1) or a human 
	player stores either 0 or 1 this is because the pragram needs to know whether this is the first or second player playing 
	'''
	while winlose == CONT:
		#get the move
		if player_type == G1:
			move = get_G1_move(gamestate,player)
		elif player_type == human:
			move = get_player_move(gamestate,player)
		#get the next game state
		winlose,gamestate,player = next_game_state(gamestate,move,player)
		print(winlose,gamestate,player)
		player_type = player1 if player_type==player2 else player2
		
	if winlose == WIN:
		print ("player "+ str(player)+" has one the game")
		display_game_state(gamestate)
	elif winlose ==  LOSE:
		print ("player "+ str(player)+" has lost the game")
		display_game_state(gamestate)




