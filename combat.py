import monster
import player
import random
import ui
import inflect
p = inflect.engine()


def attack(attacker, defender):
    # start state
    dodge = False
    critical = False
    final_damage = 0

    # check if attack was dodged, if yes, return
    dodge_roll = random.uniform(0, 100)
    dodge_chance = min(50, 3 + defender.dexterity)
    if dodge_chance > dodge_roll:
        dodge = True
        return final_damage, dodge, critical
    
    # calculate regular damage
    regular_damage = max(0, attacker.attack - defender.defense)
    final_damage = regular_damage * random.triangular(0.8, 1.2, 1.0)

    # check if crit 
    if regular_damage > 0:
        crit_roll = random.uniform(0, 100)
        crit_chance = max(0, 0.5 * attacker.dexterity)
        if crit_chance > crit_roll:
            crit_mult = random.triangular(1.5, 2.5, 1.8)
            final_damage = final_damage * crit_mult
            critical = True
    final_damage = round(final_damage)
    # use take_damage method from class
    defender.take_damage(final_damage)
    # return int, bool, bool
    return final_damage, dodge, critical

def combat_round(character, enemy, action, is_boss = False):
    events = []
    status = "" # continue, victory, defeated, run, invalid, no potions, game_won

    # player attacks
    # adds first position to events list
    if action == "A":
        dmg, dodge, crit = attack(character, enemy)
        if dodge:
            events.append(f"{ui.RED}{enemy.name}{ui.RESET} avoided your patch!")
        elif dmg == 0:
            events.append("Patch failed! No damage dealt.")
        elif crit:
            events.append(f"{ui.ORANGE}CRITICAL PATCH!{ui.RESET} {ui.GREEN}{dmg}{ui.RESET} damage dealt!")
        else:
            events.append(f"{ui.GREEN}{dmg}{ui.RESET} damage dealt!")
        # check if enemy alive
        if not enemy.is_alive:
            # if boss killed, GAME WON
            if is_boss == True:
                status = "game won"
                events.append(f"{ui.RED}{enemy.name}{ui.RESET} TERMINATED!")
                events.append(f"{ui.GREEN}Congratulations {character.name}!{ui.RESET}")
                events.append(f"{ui.GREEN}Your Final Project is successfuly debugged and submited.{ui.RESET}")
            # regular enemy killed, continue on map
            else:
                status = "victory"
                events.append(f"{ui.GREEN}{enemy.name} status: RESOLVED!{ui.RESET}")
            return status, events
        status = "continue"
    
    # heal
    elif action == "H":
        if character.hp_potions == 0:
            events.append(f"No coffee available.")
            status = "no potions"
            return status, events
        else:
            healed = character.use_hp_potion()
            events.append(f"{ui.GREEN}Coffee restored {healed} sanity!{ui.RESET}")
            status = "continue"
    
    # run away
    elif action == "R":
        # checks if boss. cant run from boss
        if is_boss == True:
            events.append(f"{ui.RED}EscapeError: You are stuck in an Infinite Loop!{ui.RESET}")
            status = "continue"
        else:
            quit_roll = random.randint(1, 100)
            # higher than 50% chance to run away from combat
            if quit_roll > 40:
                status = "run"
                events.append("TODO: Fix this later. Escape successfull!")
                return status, events
            else:
                events.append(f"{ui.RED}EscapeError: Could not escape!{ui.RESET}")
                status = "continue"
    else:
        events.append("Wrong key")
        status = "invalid"
        return status, events
    
    # enemy attacks (after player attack/heal/unsuccessfull run)
    # adds second position to events list
    dmg, dodge, crit = attack(enemy, character)
    if dodge:
        events.append("Exception handled, You dodged!")
    elif dmg == 0:
        events.append("Exception failed to execute, no sanity lost!")
    elif crit:
        events.append(f"{ui.ORANGE}CRITICAL EXCEPTION!{ui.RESET} {ui.RED}{enemy.name}{ui.RESET} reduced Your sanity by {ui.RED}{dmg}!{ui.RESET}")
    else:
        events.append(f"{ui.RED}{enemy.name}{ui.RESET} reduced Your sanity by {ui.RED}{dmg}{ui.RESET}!")

    # check if player alive
    if not character.is_alive:
        status = "defeated"
        # if killed by boss, special game over 
        if is_boss == True:
            events.append(f"{ui.RED}RecursionError: Maximum frustration level exceeded!{ui.RESET}")
            events.append(f"{ui.RED}STACK OVERFLOW{ui.RESET}")
            events.append(f"{ui.RED}GAME OVER{ui.RESET}")
        # if killed by regular mob
        else:
            events.append(f"{ui.RED}You have been defeated!{ui.RESET}")

    return status, events


def start_combat(character, enemy, is_boss=False):
    # adds all events to one list
    combat_log = []
    # counts rounds
    round_number = 1
    # intro on top of combat screen
    intro = ""
    # checks if boss fight
    if is_boss == True:
        intro = f"You enter the final part of Your code...\n{ui.RED}CRITICAL WARNING: {enemy.name} detected!{ui.RESET}"
    else:
    # start of combat, random encounter
        intro = f"WARNING: Unhandled {ui.RED}{enemy.name}{ui.RESET} encountered!"
    while True:
        # prints whole combat screen
        display_combat(character, enemy, intro, round_number, combat_log)
        # ask for input loop
        while True:
            print(f"{ui.RED}[A]{ui.RESET} Apply Patch | {ui.GREEN}[H]{ui.RESET} Drink Coffee | {ui.ORANGE}[R]{ui.RESET} Add to TODO (Run)")
            key_pressed = input("> ").strip().upper()

            # start combat round
            status, events = combat_round(character, enemy, key_pressed, is_boss)
            if status not in ("invalid", "no potions"):
                combat_log.append("---------------------------------")
                combat_log.append(f"Debugging Attempt #{round_number}")
                combat_log.extend(events)

            # no potions
            if status == "no potions":
                display_combat(character, enemy, intro, round_number, combat_log)
                print(events[0])
                continue
            # invalid key
            if status == "invalid":
                display_combat(character, enemy, intro, round_number, combat_log)
                print(events[0])
                continue

            break   

        # continue combat
        if status == "continue":
            round_number += 1
            continue
        # combat finished
        elif status in ("victory", "defeated", "run", "game won"):
            break
    # gain xp and level if victory
    if status == "victory":
        xp_gained = enemy.xp_reward
        levels_amount = character.add_xp(xp_gained)
        combat_log.append(f"{ui.GREEN}+{xp_gained} Python Experience(XP) earned!{ui.RESET}")
        if levels_amount > 0:
            combat_log.append(f"{ui.GREEN}LEVEL UP! Your python skills have improved by {levels_amount} {p.plural_noun('level', levels_amount)}!{ui.RESET}")

    display_combat(character, enemy, intro, round_number, combat_log)
    input("\nPress Enter to continue...")
    return status


# each round is completly new screen but looks like refresh. clear screen + new stats + longer combat log
def display_combat(character, enemy, intro, round_number, combat_log):
    ui.clear_screen()
    print(intro)
    # prints basic stats
    print("=====================================================")
    print(f"{ui.GREEN}Developer{ui.RESET} Sanity: {character.hp}/{character.max_hp}")
    print(f"{ui.RED}{enemy.name}{ui.RESET} Integrity: {enemy.hp}/{enemy.max_hp}")
    print()
    print(f"Coffee remaining: {character.hp_potions}")
    print("=====================================================")

    # prints full combat log, line by line
    for log in combat_log:
        print(log)





# testing random things
if __name__ == "__main__":     
    plr = player.Player("Warrior")
    syntax_error1 = monster.generate_monster("SyntaxError")

    # print(plr.is_alive)
    # print(syntax_error1.is_alive)
    # print(combat_round(plr, syntax_error1, "A"))
    # print(plr)
    # print(syntax_error1)

    start_combat(plr, syntax_error1)
    print("XXX TEST DONE")
