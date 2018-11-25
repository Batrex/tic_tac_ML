from G1 import *
from collections import defaultdict
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
