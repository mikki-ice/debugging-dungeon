from world import Map

def test_start_pos():
    map = Map()
    assert map._start_pos_x == 16
    assert map._start_pos_y == 3

def test_turn_r():
    map = Map()
    assert map._direction == "W"
    map.turn_right()
    assert map._direction == "N"
    map.turn_right()
    assert map._direction == "E"
    map.turn_right()
    assert map._direction == "S"
    map.turn_right()
    assert map._direction == "W"

def test_turn_l():
    map = Map()
    assert map._direction == "W"
    map.turn_left()
    assert map._direction == "S"
    map.turn_left()
    assert map._direction == "E"
    map.turn_left()
    assert map._direction == "N"
    map.turn_left()
    assert map._direction == "W"

def test_foward():
    map = Map()
    assert map.move_forward() == True
    map = Map()
    map.turn_right()
    assert map.move_forward() == False
    map = Map()
    map.turn_right()
    map.turn_right()
    assert map.move_forward() == False
    map = Map()
    map.turn_left()
    assert map.move_forward() == False

def test_collision():
    map = Map()
    # space
    assert map.is_walkable(0, 0) == False
    map = Map()
    # dot
    assert map.is_walkable(15, 0) == True
    map = Map()
    # Y
    assert map.is_walkable(14, 11) == False
    map = Map()
    # X
    assert map.is_walkable(14, 1) == False
    map = Map()
    # W
    assert map.is_walkable(3, 5) == False
    map = Map()
    # B
    assert map.is_walkable(22, 17) == True
    map = Map()
    # S
    assert map.is_walkable(16, 3) == False


def test_out_of_map():
    map = Map()
    assert map.is_walkable(-1, 1) == False
    map = Map()
    assert map.is_walkable(100, 1) == False
    map = Map()
    assert map.is_walkable(1, -100) == False

def test_boss_tile():
    map = Map()
    map._player_pos_x = 22
    map._player_pos_y = 17
    assert map.is_boss_tile() == True
    map = Map()
    assert map.is_boss_tile() == False
