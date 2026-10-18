import player

def main():
    name = welcome("Character name: ")
    character = player.Player(name)
    show_help()
    # commands loop
    while True:
        key = input("> ").strip()
        if key == "1":
            stats(character)
        elif key == "2":
            show_help()
        elif key == "3":
            goodbye(character)
            break
        else:
            show_help()


# welcome message and get character name
def welcome(n):
    print("Welcome to my first text based RPG, have fun and please be gentle.")
    while True:
        player_name = input(n).strip().title()
        if 4 > len(player_name) or len(player_name) > 12:
            print("Name needs to be between 4 and 12 characters")
            continue
        elif not player_name.isalpha():
            print("Name needs to have alphabetic letters only")
            continue
        return player_name

# character stats
def stats(char):
    print(char)

def show_help():
    print("Available commands:\n1. stats | 2. help | 3. quit")

def goodbye(char):
    print(f"Good bye {char.name}")



if __name__ == "__main__":
    main()
