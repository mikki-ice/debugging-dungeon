import player
import world

def main():
    name = welcome("Character name: ")
    character = player.Player(name)
    current_map = world.Map()
    show_help()
    # commands loop
    while True:
        key = input("> ").strip().upper()
        if key == "C":
            stats(character)
        elif key == "H":
            show_help()
        elif key == "M":
            show_map(current_map)
        elif key == "QUIT":
            goodbye(character)
            break
        elif key == "W":
            if current_map.move_forward():
                print("You move forward")
            else:
                print("You hit the wall!")
        elif key == "D":
            current_map.turn_right()
            print("You turned right")
        elif key == "A":
            current_map.turn_left()
            print("You turned left")
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
    print("Available commands:\n"
          "W A D to move\n"
    "C. stats | H. help | M. show map | QUIT to quit")

def goodbye(char):
    print(f"Good bye {char.name}")

def show_map(current_map):
    print(current_map.display_map(), end="")


if __name__ == "__main__":
    main()
