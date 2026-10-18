import player

def main():
    name = welcome("Character name: ")
    character = player.Player(name)
    print(character)
    character.take_damage(50)
    print(f"{character.hp}/{character.max_hp}")
    character.heal(40)
    print(f"{character.hp}/{character.max_hp}")


# welcome message and get character name
def welcome(name):
    print("Welcome to my first text based RPG, have fun and please be gentle.")
    while True:
        player_name = input(name)
        if len(player_name) > 12:
            print("Try shorter name")
            continue
        return player_name

main()
