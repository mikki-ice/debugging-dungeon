import monster
import pytest

def test_generate():
    mon = monster.generate_monster("SyntaxError")
    assert mon.name == "SyntaxError"

def test_generate_error():
    with pytest.raises(ValueError):
        mon = monster.generate_monster("Monster")

def test_monster_stats():
    mon = monster.generate_monster("SyntaxError")
    min_hp, max_hp = monster.MONSTERS["SyntaxError"]["max_hp"]
    assert min_hp <= mon.hp <= max_hp
    min_attack, max_attack = monster.MONSTERS["SyntaxError"]["attack"]
    assert min_attack <= mon.attack <= max_attack
    min_defense, max_defense = monster.MONSTERS["SyntaxError"]["defense"]
    assert min_defense <= mon.defense <= max_defense
    min_dexterity, max_dexterity = monster.MONSTERS["SyntaxError"]["dexterity"]
    assert min_dexterity <= mon.dexterity <= max_dexterity
    min_xp_reward, max_xp_reward = monster.MONSTERS["SyntaxError"]["xp_reward"]
    assert min_xp_reward <= mon.xp_reward <= max_xp_reward

def test_monster_damage():
    mon = monster.generate_monster("SyntaxError")
    hp_after = mon.hp - 10
    mon.take_damage(10)
    assert mon.hp == hp_after
    assert mon.is_alive == True

def test_monster_death():
    mon = monster.generate_monster("SyntaxError")
    mon.take_damage(50)
    assert mon.hp == 0
    assert mon.is_alive == False