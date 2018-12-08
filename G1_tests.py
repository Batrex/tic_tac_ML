from collections import defaultdict
from G1 import *
#
# def test_train_0():
#     assert train(1,[[[[0, 0, 0, 1, 0, 0, 2, 0, 0], 6]],\
#      [[[0, 0, 0, 1, 0, 0, 0, 0, 0], 3],\
#      [[0, 0, 1, 1, 0, 0, 2, 0, 0], 2],\
#      [[0, 0, 1, 1, 0, 0, 2, 0, 0], 2]]]) ==

def test_load_to_save():
    examp_model= defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: [0,0])))
    examp_model[8][0][5][1] = 4
    examp_model[8][0][0][0] = 1
    save_model(examp_model,"examp.model")
    loaded = load_model("examp.model")
    assert loaded[8][0][5][1] == 4
    print("loaded-- "+str(loaded))
    print("loaded-- "+str(loaded[8][2][1]))
    assert loaded[8][2][0][0] == 0
    assert isinstance(loaded,dict)
    assert isinstance(loaded,defaultdict)

#examp model only for testing
examp_model = {(0,1):{"move1":[2,2],"move2":[3,1]},(1,2):{"move1":[3,0],"move2":[0,3]}}
def test_create_move_score_list():
    assert create_move_score_list(examp_model,[0,1]) == [["move1",1],["move2",2]]
def test_create_move_score_list1():
    assert create_move_score_list(examp_model,[1,2]) == [["move1",4],["move2",0.25]]

'''
model = defaultdict(lambda: defaultdict(lambda: [0,0]))
model[1][1][1] =+ 1
print(model)
new_model = _defaultdict_to_dict(model)
'''
print("result of the switch: "+str(zero_player_in_games_state([1,2,0,2,2,2,2,1,4,5],1)))