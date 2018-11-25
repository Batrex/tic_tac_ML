#some functions to get the input of a move from the player 

def create_display_game_state(game_state):
    display_game_state = [2,2,2,2,2,2,2,2,2]
    index = 0
    for ToChange in game_state:
        if ToChange == 2:
            ToChange = "."
        elif ToChange == 0:
            ToChange = "X"
        elif ToChange == 1:
            ToChange = "O"
        display_game_state[index] = ToChange
        index = index + 1
    return(display_game_state)

def display_game_state(game_state):
    display_game_state = create_display_game_state(game_state)
    console = " ----------- \n" +\
             "| "+display_game_state[0]+" | "+display_game_state[1]+" | "+display_game_state[2]+" |\n" +\
             "| "+display_game_state[3]+" | "+display_game_state[4]+" | "+display_game_state[5]+" |\n" +\
             "| "+display_game_state[6]+" | "+display_game_state[7]+" | "+display_game_state[8]+" |\n" +\
             " ----------- \n"
    print(console)


def get_player_move(game_state,player):
    display_game_state(game_state)
    next_move = input('what is your move}-')
    if next_move not in ('0','1','2','3','4','5','6','7','8','9'):
        while next_move not in ('0','1','2','3','4','5','6','7','8','9'):
            next_move = input('please enter a number under 9}-')
    next_move = int(next_move)
    return (next_move)
