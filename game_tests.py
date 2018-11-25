from game import *

# tests for game win loss states
def test_open_space():
    assert move_is_on_open_space(
    [ 1,0,0,\
      0,0,0,\
      0,0,0], 0) == False

def test_win_lose_1():
    assert check_win_lose(
    [ 1,1,1,\
      0,0,0,\
      0,0,0], 8,1) == WIN

def test_win_lose_2():
    assert check_win_lose(
    [ 0,0,0,\
      1,1,1,\
      0,0,0], 0,1) == WIN

def test_win_lose_3():
    assert check_win_lose(
    [ 0,0,0,\
      0,0,0,\
      1,1,1], 0,1) == WIN

def test_win_lose_4():
    assert check_win_lose(
    [ 0,1,0,\
      0,1,0,\
      0,1,0], 0,1) == WIN
def test_win_lose_5():
    assert check_win_lose(
    [ 1,0,0,\
      1,0,0,\
      1,0,0], 8,1) == WIN
def test_win_lose_6():
    assert check_win_lose(
    [ 0,0,1,\
      0,0,1,\
      0,0,1], 0,1) == WIN
def test_win_lose_7():
    assert check_win_lose(
    [ 1,0,0,\
      0,1,0,\
      0,0,1], 7,1) == WIN

def test_win_lose_8():
    assert check_win_lose(
    [ 0,0,1,\
      0,1,0,\
      1,0,0], 0,1) == WIN


# tests for validity of game states
def assert_valid_game_state(game_state, is_valid):
    error_was_thrown = False
    try:
        check_valid_game_state(game_state)
    except AssertionError:
        error_was_thrown = True
    if is_valid:
        assert not error_was_thrown
    else:
        assert error_was_thrown

def test_invalid_game_state_0():
    assert_valid_game_state([0,1,2], is_valid=False)

def test_invalid_game_state_1():
    assert_valid_game_state([0,1,2,0,1,2,0,3,2], is_valid=False)

def test_invalid_game_state_2():
    assert_valid_game_state([], is_valid=False)

def test_invalid_game_state_3():
    assert_valid_game_state([0,1,2,0,1,2,0,1,2,1], is_valid=False)

def test_valid_game_state_0():
    assert_valid_game_state([0,0,0,0,0,0,0,0,0], is_valid=True)

def test_valid_game_state_1():
    assert_valid_game_state([0,1,2,0,1,2,0,1,2], is_valid=True)

# tests for validity of moves
def assert_valid_move(game_state, move, is_valid):
    error_was_thrown = False
    try:
        check_valid_move(game_state, move)
    except AssertionError:
        error_was_thrown = True
    if is_valid:
        assert not error_was_thrown
    else:
        assert error_was_thrown

def test_invalid_game_move_0():
    assert_valid_move([0,1,2,0,1,2,0,1,2], 10, is_valid=False)

def test_invalid_game_move_1():
    assert_valid_move([0,1,2,0,1], 0, is_valid=False)

def test_valid_game_move_0():
    assert_valid_move([0,1,2,0,1,2,0,1,2], 0, is_valid=True)
#test the next move is added to the gamestate
def test_next_move_added0 ():
    assert add_move_to_game_state([0,0,0,\
                                0,0,0,\
                                0,0,0],1,1)\
    ==[0,1,0,\
       0,0,0,\
       0,0,0]

def test_next_move_added1():
    assert add_move_to_game_state([0,2,0,\
                                0,2,2,\
                                0,0,0],7,2)\
    ==[0,2,0,\
       0,2,2,\
       0,2,0]

# test the whole game
def test_next_game_state():
    assert next_game_state([2,2,2,2,2,2,2,2,2],4,1)\
     == (CONT,[2,2,2,2,1,2,2,2,2],2)
# note to self,fix next game state tests, remember 2 = space and the players are 0 and 1  
def test_next_game_state1():
    assert next_game_state([2,1,1,0,2,0,0,0,0],0,1)\
     == (LOSE,[2,1,1,0,2,0,0,0,0],1)

def test_next_game_state2():
    assert next_game_state([0,1,1,0,0,0,0,0,0],0,1)\
     == (WIN,[1,1,1,0,0,0,0,0,0],1)

def test_next_game_state3():
    assert next_game_state([0,0,0,0,0,0,0,0,0],4,2)\
     == (CONT,[0,0,0,0,2,0,0,0,0],1)

def test_next_game_state4():
    assert next_game_state([1,2,1,1,2,2,2,1,0],8,1)\
     == (SCRAM,[1,2,1,1,2,2,2,1,1],1)

def test_next_game_state5():
    assert next_game_state([1,1,1,1,1,1,1,1,0],8,1)\
     == (WIN,[1,1,1,1,1,1,1,1,1],1)
