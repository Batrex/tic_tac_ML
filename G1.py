import random
from collections import defaultdict
from game import WIN, LOSE
import pickle

def _defaultdict_to_dict(model):
    return {
        gamestate:{
            move:{
                winlose:model[gamestate][move][winlose]
                for winlose in model[gamestate][move]
            }
            for move in model[gamestate]
        }
        for gamestate in model
    }

def _dict_to_defaultdict(model_dict):
    model = defaultdict(lambda: defaultdict(lambda: [0,0]))
    for gamestate in model_dict:
        for move in model_dict[gamestate]:
            for winlose in model_dict[gamestate][move]:
                model[gamestate][move][winlose] = model_dict[gamestate][move][winlose]
    return model

def save_model(model,filename):
    print("saving  - "+str(model)+" - to disk with the filename: "+filename+" -")
    pickle.dump(_defaultdict_to_dict(model), open(filename,'wb'))

def load_model(filename):
    loaded_model = pickle.load( open(filename, 'rb'))
    print('loaded file: '+filename+' - with value - '+str(loaded_model)+" -")
    return(_dict_to_defaultdict(loaded_model))

def add_moves_to_model(win_lose,player_moves,model):
    for game_move in player_moves:
        game_state = game_move[0]
        move = game_move[1]
        model[tuple(game_state)][move][win_lose] += 1
        print("model:"+str(win_lose)+str(model[tuple(game_state)][move]))


def train(winning_player,game_histories):
    #load the model
    raw_model = load_model("model_G1.model")
    model = _dict_to_defaultdict("raw_model")
    #for the winning_player
    winning_player_moves = game_histories[winning_player]
    add_moves_to_model(WIN,winning_player_moves,model)
    #for the losing player
    losing_player = 1 if winning_player == 0 else 0
    losing_player_moves = game_histories[losing_player]
    add_moves_to_model(LOSE,losing_player_moves,model)
    #save the model
    savable_model = _defaultdict_to_dict(model)
    save_model(savable_model,"model_G1.model")

##--- chose the move ---##

def create_move_score_list(model,game_state):
    move_scores_raw = model[tuple(game_state)] #get the moves and scores for this game state
    move_scores = []
    for i in range(9):
        print(move_scores_raw[i])
        move_scores.append([i,(move_scores_raw[i][0]+1)/(move_scores_raw[i][1]+1)])
    return(move_scores)

def order_moves(move_scores):
    return(sorted(move_scores, key=lambda move_scores: move_scores[1]))
    #this will sort the move 'mini lists' by their second item, the score  

def chose_move(move_scores):
    counter = 0
    while True:
        chance = random.random()
        if chance > 0.5:
            counter+=1
            if counter >= len(move_scores):
                counter = 0
        else:
            print("move_scores"+str(move_scores))
            print("counter"+str(counter))
            return(counter)


def get_G1_move(game_state,player):
    raw_model = load_model("model.sav")
    model = _dict_to_defaultdict(raw_model)
    print(str(type(model))) 
    return(chose_move(order_moves(create_move_score_list(model,game_state))))
