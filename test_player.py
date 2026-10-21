from player import Player
import pytest

def test_take_damage():
    player = Player("Student")
    player.take_damage(20)
    assert player.hp == 30
    assert player.is_alive == True

def test_take_damage_death():
    player = Player("Student")
    player.take_damage(50)
    assert player.hp == 0
    assert player.is_alive == False

    player = Player("Student")
    player.take_damage(51)
    assert player.hp == 0
    assert player.is_alive == False

def test_negative_dmg():
    player = Player("Student")
    with pytest.raises(ValueError):
        player.take_damage(-1)

def test_heal():
    player = Player("Student")
    player.take_damage(10)
    player.heal(10)
    assert player.hp == 50

def test_overheal():
    player = Player("Student")
    player.take_damage(10)
    player.heal(100)
    assert player.hp == 50

def test_negative_heal():
    player = Player("Student")
    with pytest.raises(ValueError):
        player.take_damage(10)
        player.heal(-10)

def test_xp():
    player = Player("Student")
    player.add_xp(50)
    assert player._xp == 50

    player = Player("Student")
    player.add_xp(120)
    assert player._xp == 20
    assert player._level == 2

    player = Player("Student")
    player.add_xp(650)
    assert player._xp == 50
    assert player._level == 4

def test_negative_xp():
    player = Player("Student")
    with pytest.raises(ValueError):
        player.add_xp(-100)

def test_levelup():
    player = Player("Student")
    player.level_up()
    assert player._level == 2
    assert player._xp == 0
    assert player.max_hp == 70
    assert player.attack == 15
    assert player.defense == 7
    assert player.dexterity == 3
    assert player.hp == 70

def test_potion_heal():
    player = Player("Student")
    player.take_damage(40)
    player.use_hp_potion()
    assert player.hp == 32
    assert player.hp_potions == 1

def test_potion_fullhp():
    player = Player("Student")
    player.use_hp_potion()
    assert player.hp == 50
    assert player.hp_potions == 1

def test_no_potions():
    player = Player("Student")
    player._hp_potions = 0
    player.take_damage(40)
    player.use_hp_potion()
    assert player.hp == 10

def test_potion_regen():
    player = Player("Student")
    player._hp_potions = 1
    player.potion_regen()
    player.potion_regen()
    player.potion_regen()
    assert player.hp_potions == 1
    player.potion_regen()
    assert player.hp_potions == 2

    player = Player("Student")
    player._hp_potions = 1
    player.potion_regen()
    player.potion_regen()
    player.potion_regen()
    assert player.hp_potions == 1
    player.potion_regen()
    assert player.hp_potions == 2
    player.potion_regen()
    player.potion_regen()
    player.potion_regen()
    player.potion_regen()
    assert player.hp_potions == 2
