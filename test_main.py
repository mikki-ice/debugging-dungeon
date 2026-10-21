import builtins
import combat
import main
import player
import pytest
import random

def test_welcome_correct(monkeypatch):
    # setattr(/module,class,place containing attribute to be changed/, /name of attribute to be changed(of name of function to be changed)/, /new value, replacement, mock/)
    # lambda - shorter form of def function so no need to write whole function. lamba /arguments that original function needed/ : /return value that we want/
    monkeypatch.setattr("builtins.input", lambda _: "Student")
    assert main.get_name("Input name: ") == "Student"

    # iterate over few wrong names, accept only correct one in the end
def test_welcome_incorrect(monkeypatch):
    # list of names. iter([list, of, things]) = iterator, next() will take one by one from iterator list until end or StopIteration
    names = iter(["st", "12345", "Student1", "John Harvard", "Student"])
    monkeypatch.setattr("builtins.input", lambda _: next(names))
    assert main.get_name("Input name: ") == "Student"

    # high roll, so no chance for random encounter
def test_no_encounter(monkeypatch):
    char = player.Player("Student")
    monkeypatch.setattr(main.random, "randint", lambda a, b:100)
    assert main.random_encounter(char) == None

    # monkeypatch encounter roll to 1, random.choices to SyntaxError monster, and return value from start_combat
def test_encounter(monkeypatch):
    char = player.Player("Student")
    monkeypatch.setattr(main.random, "randint", lambda a, b:1)
    monkeypatch.setattr(main.random, "choices", lambda a, b:["SyntaxError"])
    monkeypatch.setattr(main.combat, "start_combat", lambda a, b:"victory")
    assert main.random_encounter(char) == "victory"

