import project
import player

def test_get_name(monkeypatch):
    # setattr(/module,class,place containing attribute to be changed/, /name of attribute to be changed(of name of function to be changed)/, /new value, replacement, mock/)
    # lambda - shorter form of def function so no need to write whole function. lamba /arguments that original function needed/ : /return value that we want/
    monkeypatch.setattr("builtins.input", lambda _: "Student")
    assert project.get_name("Input name: ") == "Student"

    # iterate over few wrong names, accept only correct one in the end
def test_get_name_incorrect(monkeypatch):
    # list of names. iter([list, of, things]) = iterator, next() will take one by one from iterator list until end
    names = iter(["st", "12345", "Student1", "John Harvard", "Student"])
    monkeypatch.setattr("builtins.input", lambda _: next(names))
    assert project.get_name("Input name: ") == "Student"

    # high roll, so no chance for random encounter
def test_random_encounter_roll_100(monkeypatch):
    char = player.Player("Student")
    monkeypatch.setattr(project.random, "randint", lambda a, b:100)
    assert project.random_encounter(char) == None

    # monkeypatch encounter roll to 1, random.choices to SyntaxError monster, and return value from start_combat
def test_random_encounter_roll_1(monkeypatch):
    char = player.Player("Student")
    monkeypatch.setattr(project.random, "randint", lambda a, b:1)
    monkeypatch.setattr(project.random, "choices", lambda a, b:["SyntaxError"])
    monkeypatch.setattr(project.combat, "start_combat", lambda a, b:"victory")
    assert project.random_encounter(char) == "victory"

def test_boss_fight(monkeypatch):
    char = player.Player("Student")
    # monkeypatch checks if boss_fight() correctly sets is_boss to true and goes into boss fight, not regular encounter
    monkeypatch.setattr(project.combat, "start_combat", lambda char, boss, is_boss=False:"game won" if is_boss == True else "error")
    assert project.boss_fight(char) == "game won"

