import random
from collections import defaultdict
from game import WIN,LOSE
import pickle
import logging
log = logging.getLogger(__name__)



def _defaultdict_to_dict(model):
    model_dict = {}
    for game_state in model:
        for move in model[game_state]:
            model_dict[game_state] = dict(model[game_state])
            model_dict[game_state][move] = model[game_state][move]
    return(model_dict)

def _dict_to_defaultdict(model_dict):
    model = defaultdict(lambda: defaultdict(lambda: [0,0]))
    for game_state in model_dict:
        for move in model_dict[game_state]:
            for win_lose in model_dict[game_state][move]:
                model[game_state][move] = model_dict[game_state][move]
    return model

def save_model(model,filename):
    #print("saving  - "+str(model)+" - to disk with the filename: "+filename+" -")
    pickle.dump(_defaultdict_to_dict(model), open(filename,'wb'))

def load_model(filename):
    loaded_model = pickle.load( open(filename, 'rb'))
    return(_dict_to_defaultdict(loaded_model))

def zero_player_in_games_state(game_state,player):
    zeroed_gamestate = game_state.copy()
    if player == 1:
        for index,item in enumerate(zeroed_gamestate):
            if item == 0:
                zeroed_gamestate[index] = 1
            elif item == 1:
                zeroed_gamestate[index] = 0
    return(zeroed_gamestate)


def add_moves_to_model(win_lose,player_moves,model):
    for game_move in player_moves:
        game_state = game_move[0]
        move = game_move[1]
        model[tuple(game_state)][move][win_lose] += 1


def train(winning_player,game_histories,model_name):
    #load the model
    model = load_model(str(model_name))
    #for the winning_player
    winning_player_moves = game_histories[winning_player]
    add_moves_to_model(WIN,winning_player_moves,model)
    #for the losing player
    losing_player = 1 if winning_player == 0 else 0
    losing_player_moves = game_histories[losing_player]
    add_moves_to_model(LOSE,losing_player_moves,model)
    #save the model
    savable_model = _defaultdict_to_dict(model)
    save_model(savable_model,str(model_name))

##--- chose the move ---##

def create_move_score_list(model,game_state):
    move_scores_raw = model[tuple(game_state)] #get the moves and scores for this game state
    move_scores = []
    for i in range(9):
        move_scores.append([i,(move_scores_raw[i][0])-(move_scores_raw[i][1]/2)])
    return(move_scores)

def order_moves(move_scores):
    return(sorted(move_scores, key=lambda move_scores: move_scores[1], reverse = True))
    #this will sort the move 'mini lists' by their second item, the score  

def chose_move(move_scores,verbose):
    counter = 0
    while True:
        chance = random.random()
        if chance > 0.5:
            counter+=1
            if counter >= len(move_scores):
                counter = 0
        else:
            if verbose:
                print("move_scores: "+str(move_scores))
                print("----move calculated----")
                print("move: "+str(move_scores[counter][0]))
            return(move_scores[counter][0])


def get_G1_move(game_state,player,game_histories,verbose):
    model = load_model("model.sav") 
    zeroed_gamestate = zero_player_in_games_state(game_state,player)
    if verbose:
        print("----calculating move----")
        print("basic game_state after game_state zeroed"+str(game_state))
        #this is making the player playing in the gamestate = to 0 and the opposition 0 
        print("zeroed gamestate used by G1"+str(game_state))
    move = chose_move(order_moves(create_move_score_list(model,zeroed_gamestate)),verbose)
    #add the move to the game_histories might want to add this to the g1 instead later on 
    game_histories[player].append([zeroed_gamestate,move])
    return(move)