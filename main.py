import combat
import monster
import random
import player
import world




def main():
    name = welcome("Student name: ")
    character = player.Player(name)
    current_map = world.Map()
    show_map(current_map)
    # commands loop
    while True:
        show_help()
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
            # if move forward is possible, move and roll for random encounter
            if current_map.move_forward():
                print("You move forward")
                character.potion_regen()
                # checks if its time for boss fight
                if current_map.is_boss_tile():
                    status = boss_fight(character)
                # if not boss, roll for random encounter
                else:
                    status = random_encounter(character)
                if status == "defeated":
                    death(character)
                    break
                elif status == "game won":
                    break
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
        if 3 > len(player_name) or len(player_name) > 16:
            print("Name needs to be between 3 and 16 characters")
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
          "W to move forward, A and D to change direction\n"
    "C. stats | H. help | M. show map | QUIT to quit")

def goodbye(char):
    print(f"Good bye {char.name}.")

def death(char):
    print(f"Rest {char.name}, few more tutorial and You can do it!")

def show_map(current_map):
    print(current_map.display_map(), end="")

# roll for random monster encounter
def random_encounter(char):
    encounter_chance = 20
    chance_roll = random.randint(1, 100)
    if chance_roll <= encounter_chance:
        regular_monsters = ["SyntaxError", "TypeError", "ZeroDivisionError"]
        weights = [6, 3, 1]
        random_monster = random.choices(regular_monsters, weights)[0]
        new_monster = monster.generate_monster(random_monster)
        combat_status = combat.start_combat(char, new_monster)
        return combat_status
    else:
        return

def boss_fight(char):
    boss = monster.generate_monster("Infinite Loop")
    final_status = combat.start_combat(char, boss, is_boss=True)
    return final_status


if __name__ == "__main__":
    main()
    # regular_monsters = ["SyntaxError", "TypeError", "ZeroDivisionError"]
    # weights = [4, 3, 1]
    # random_monster = random.choices(regular_monsters, weights)
    # print(random_monster)
    # print(random_monster[0])