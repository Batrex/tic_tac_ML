#import os, sys
WIN = 0
LOSE = 1
CONT = 2
SCRAM = 3

def check_valid_game_state(game_state):
    assert len(game_state)==9
    for space in game_state:
        assert space in [0,1,2]

def check_valid_move(game_state, move):
    check_valid_game_state(game_state)
    assert move in list(range(9))

def check_value_set_for_win(check_value_set,player):
    for i in check_value_set:
        if i != player:
            return CONT
    return WIN

def new_win_lose(win_lose,check_value_set,player):
    if win_lose == WIN or check_value_set_for_win(check_value_set,player)==WIN:
        return WIN
    else:
        return CONT

def check_win_lose(game_state,move,player):
    #check for three in a row!!
    win_lose = CONT
    for set_indicator in range(3):
        #first check for three in a row hoizontaly
        check_value_set = [game_state[set_indicator*3],game_state[set_indicator*3+1],game_state[set_indicator*3+2]]
        win_lose = new_win_lose(win_lose,check_value_set,player)
        #then check for for three in a row verticaly
        check_value_set = [game_state[set_indicator],game_state[set_indicator+3],game_state[set_indicator+6]]
        win_lose = new_win_lose(win_lose,check_value_set,player)
    #last check for three in a row on both diagonals
    check_value_set = [game_state[0],game_state[4],game_state[8]]
    win_lose = new_win_lose(win_lose,check_value_set,player)
    check_value_set = [game_state[2],game_state[4],game_state[6]]
    win_lose = new_win_lose(win_lose,check_value_set,player)
    return win_lose

def move_is_on_open_space(game_state,move):
    return game_state[move]==2

def check_if_game_is_scrambled(game_state):
    for i in game_state:
        if i == 2:
            return CONT
    return SCRAM
def add_move_to_game_state(game_state, move,player):
    game_state[move] = player
    return game_state

def change_player(player):
    player = 1 if player==0 else 0
    return(player)

def next_game_state(game_state,move,player):
    check_valid_move(game_state, move)
    next_player = player
    win_lose = LOSE
    curr_state = list(game_state)
    next_state = curr_state
    if  move_is_on_open_space(curr_state,move):
        next_state = add_move_to_game_state(curr_state,move,player)
        win_lose = check_win_lose(next_state, move,player)
        if win_lose == CONT:
            win_lose = check_if_game_is_scrambled(next_state)
    if win_lose == CONT:
        next_player = change_player(player)
    return (win_lose, next_state, next_player)

#initialize gives the gamestate,player,and win lose for at the begining of the game 

def initialise():
    return ([2,2,2,2,2,2,2,2,2],0,CONT)


