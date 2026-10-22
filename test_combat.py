import combat
import player
import monster


# using monkepatch to set value(so test is possible) instead of using random value.
def test_regular_attack(monkeypatch):
    # player lvl1 = hp-50, atk-10, def-5, dex-2
    char = player.Player("Student")
    # enemy = (name, hp, atk, def, dex, xp)
    enemy = monster.Monster("Test", 50, 10, 5, 1, 50)
    # setattr(/module,class,place containing attribute to be changed/, /name of attribute to be changed(of name of function to be changed)/, /new value, replacement, mock/)
    # lambda - shorter form of def function so no need to write whole function. lamba /arguments that original function needed/ : /return value that we want/
    monkeypatch.setattr(combat.random, "uniform", lambda a, b: 100)
    monkeypatch.setattr(combat.random, "triangular", lambda a, b, c: 1.0)

    dmg, dodge, crit = combat.attack(char, enemy)
    assert dmg == 5
    assert dodge == False
    assert crit == False
    assert enemy.hp == 45


def test_dodge(monkeypatch):
    # player lvl1 = hp-50, atk-10, def-5, dex-2
    char = player.Player("Student")
    # enemy = (name, hp, atk, def, dex, xp)
    enemy = monster.Monster("Test", 50, 10, 5, 1, 50)
    # setattr(/module,class,place containing attribute to be changed/, /name of attribute to be changed(of name of function to be changed)/, /new value, replacement, mock/)
    # lambda - shorter form of def function so no need to write whole function. lamba /arguments that original function needed/ : /return value that we want/
    monkeypatch.setattr(combat.random, "uniform", lambda a, b: 0)
    monkeypatch.setattr(combat.random, "triangular", lambda a, b, c: 1.0)

    dmg, dodge, crit = combat.attack(char, enemy)
    assert dmg == 0
    assert dodge == True
    assert crit == False
    assert enemy.hp == 50

# if attack <= defenders defense  == zero damage.
def test_zero_dmg(monkeypatch):
    # player lvl1 = hp-50, atk-10, def-5, dex-2
    char = player.Player("Student")
    # enemy = (name, hp, atk, def, dex, xp)
    enemy = monster.Monster("Test", 50, 10, 10, 1, 50)
    # setattr(/module,class,place containing attribute to be changed/, /name of attribute to be changed(of name of function to be changed)/, /new value, replacement, mock/)
    # lambda - shorter form of def function so no need to write whole function. lamba /arguments that original function needed/ : /return value that we want/
    monkeypatch.setattr(combat.random, "uniform", lambda a, b: 100)
    monkeypatch.setattr(combat.random, "triangular", lambda a, b, c: 1.0)

    dmg, dodge, crit = combat.attack(char, enemy)
    assert dmg == 0
    assert dodge == False
    assert crit == False
    assert enemy.hp == 50

def test_enemy_killed(monkeypatch):
    # player lvl1 = hp-50, atk-10, def-5, dex-2
    char = player.Player("Student")
    # enemy = (name, hp, atk, def, dex, xp)
    enemy = monster.Monster("Test", 5, 10, 5, 1, 50)
    # setattr(/module,class,place containing attribute to be changed/, /name of attribute to be changed(of name of function to be changed)/, /new value, replacement, mock/)
    # lambda - shorter form of def function so no need to write whole function. lamba /arguments that original function needed/ : /return value that we want/
    monkeypatch.setattr(combat.random, "uniform", lambda a, b: 100)
    monkeypatch.setattr(combat.random, "triangular", lambda a, b, c: 1.0)

    dmg, dodge, crit = combat.attack(char, enemy)
    assert dmg == 5
    assert dodge == False
    assert crit == False
    assert enemy.hp == 0
    assert enemy.is_alive == False

def test_player_killed(monkeypatch):
    # player lvl1 = hp-50, atk-10, def-5, dex-2
    char = player.Player("Student")
    # enemy = (name, hp, atk, def, dex, xp)
    enemy = monster.Monster("Test", 50, 55, 5, 1, 50)
    # setattr(/module,class,place containing attribute to be changed/, /name of attribute to be changed(of name of function to be changed)/, /new value, replacement, mock/)
    # lambda - shorter form of def function so no need to write whole function. lamba /arguments that original function needed/ : /return value that we want/
    monkeypatch.setattr(combat.random, "uniform", lambda a, b: 100)
    monkeypatch.setattr(combat.random, "triangular", lambda a, b, c: 1.0)

    dmg, dodge, crit = combat.attack(enemy, char)
    assert dmg == 50
    assert dodge == False
    assert crit == False
    assert char.hp == 0
    assert char.is_alive == False

# boss killed
def test_game_won(monkeypatch):
    # player lvl1 = hp-50, atk-10, def-5, dex-2
    char = player.Player("Student")
    # enemy = (name, hp, atk, def, dex, xp)
    enemy = monster.Monster("Test", 1, 5, 1, 1, 50)
    # setattr(/module,class,place containing attribute to be changed/, /name of attribute to be changed(of name of function to be changed)/, /new value, replacement, mock/)
    # lambda - shorter form of def function so no need to write whole function. lamba /arguments that original function needed/ : /return value that we want/
    monkeypatch.setattr(combat.random, "uniform", lambda a, b: 100)
    monkeypatch.setattr(combat.random, "triangular", lambda a, b, c: 1.0)
    status, events = combat.combat_round(char, enemy, "A", True)
    assert enemy.hp == 0
    assert status == "game won"

# pressed wrong key, attack didnt happen (both ways)
def test_invalid_action():
    # player lvl1 = hp-50, atk-10, def-5, dex-2
    char = player.Player("Student")
    # enemy = (name, hp, atk, def, dex, xp)
    enemy = monster.Monster("Test", 1, 5, 1, 1, 50)
    status, events = combat.combat_round(char, enemy, "X", False)
    assert status == "invalid"
    assert enemy.hp == 1
    assert char.hp == 50
