#take the output from the game and give it to the player, then take the output from the player 
#and give it to the game, and soo forth.
from G1 import get_G1_move,train,zero_player_in_games_state
from game import next_game_state,initialise
from game import WIN,LOSE,CONT,SCRAM 
from player import display_game_state,get_player_move
G1 = 0
human = 1




def playgame (player1_input,player2_input):
	player1 = player1_input
	player2 = player2_input
	player_type = player1
	game_state,player,win_lose = initialise()
	move = 0
	game_histories = [[],[]]
	'''
	the difference between player and currrent player is:
	player_type stores whether the player is a Ai (ie G1) or a human 
	player stores either 0 or 1 this is because the pragram needs to know whether this is the first or second player playing 
	'''

	#display the game start output
	print("--------------game start--------------")
	display_game_state(game_state)
	while win_lose == CONT:
		print("----next turn----")
		print("player: "+str(player))
		#get the move
		if player_type == G1:
			zeroed_gamestate = zero_player_in_games_state(game_state,player)
			print("basic game_state after game_state zeroed"+str(game_state))
			#this is making the player playing in the gamestate = to 0 and the opposition 0 
			move = get_G1_move(game_state,player)
			#add the move to the game_histories might want to add this to the g1 instead later on 
			game_histories[player].append([zeroed_gamestate,move])
		elif player_type == human:
			move = get_player_move(game_state,player)

		
		#get the next game state
		win_lose,game_state,player = next_game_state(game_state,move,player)
		player_type = player1 if player_type==player2 else player2
		
		#display the gamestate
		display_game_state(game_state)
		


	if win_lose == WIN:
		print ("player "+ str(player)+" has one the game")	
	elif win_lose ==  LOSE:
		print ("player "+ str(player)+" has lost the game")
		player = 1 if player == 0 else 0
	#train the G1 model	
	train(player,game_histories,"model.sav")




