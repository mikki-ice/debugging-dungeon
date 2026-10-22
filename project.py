import combat
import monster
import player
import random
import ui
import world




def main():
    ui.clear_screen()
    welcome()
    name = get_name("Initialize character. Enter your name: ")
    character = player.Player(name)
    current_map = world.Map()
    log = ""
    # commands loop
    while True:
        ui.clear_screen()
        show_map(current_map)
        show_help()
        print(log)
        key = input("> ").strip().upper()
        if key == "C":
            log = (character)
        elif key == "QUIT":
            print(goodbye(character))
            break
        elif key == "W":
            # if move forward is possible, move and roll for random encounter
            if current_map.move_forward():
                log = "You move forward"
                character.potion_regen()
                # checks if its time for boss fight
                if current_map.is_boss_tile():
                    status = boss_fight(character)
                # if not boss, roll for random encounter
                else:
                    status = random_encounter(character)
                if status == "defeated":
                    print(death(character))
                    break
                elif status == "game won":
                    break
            else:
                log = "You hit the wall!"
        elif key == "D":
            current_map.turn_right()
            log = "You turned right"
        elif key == "A":
            current_map.turn_left()
            log = "You turned left"
        else:
            log =  "Incorrect key"


def welcome():
    print("==================================================")
    print(f"          {ui.BLUE}CS50P: DEBUGGING DUNGEON{ui.RESET}")
    print("==================================================")
    print("Your final project is almost complete.\n"
          "Just one final test...\n"
          "pytest project.py\n"
          f"{ui.RED}ERROR!!! Your code has become self-aware!{ui.RESET}\n\n"
          "Something went terribly wrong.\n"
          "Somehow you ended up inside your own code!\n"
          "Find your way through the dungeon.\n"
          "Debug the errors\n"
          f"Escape the {ui.RED}Infinite Loop{ui.RESET}\n"
          f"{ui.GREEN}Good luck, Student\n{ui.RESET}"
          "==================================================\n")


# get character name
def get_name(n):
    while True:
        player_name = input(n).strip().title()
        if 3 > len(player_name) or len(player_name) > 16:
            print("Name needs to be between 3 and 16 characters")
            continue
        elif not player_name.isalpha():
            print("Name needs to have alphabetic letters only")
            continue
        return player_name


def show_help():
    print(f"AVAILABLE COMMANDS\n"
          f"{ui.GREEN}[W]{ui.RESET} move forward | {ui.GREEN}[A/D]{ui.RESET} rotate left/right\n"
          f"{ui.GREEN}[C]{ui.RESET} inspect variables (stats) | {ui.RED}[QUIT]{ui.RESET} terminate program (and yourself in it)")

def goodbye(char):
    return f"{ui.RED}Process terminated. Your bugs are still there, {char.name}.{ui.RESET}"

def death(char):
    return f"{ui.RED}GAME OVER:{ui.RESET} {char.name} has been defeated by their own code. Time to watch that lecture again!"

def show_map(current_map):
    print(current_map.display_map(), end="")

# roll for random monster encounter
def random_encounter(char):
    encounter_chance = 10
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