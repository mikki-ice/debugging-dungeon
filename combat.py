import monster
import player
import random
import ui
import world
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
            events.append(f"{enemy.name} dodged!")
        elif dmg == 0:
            events.append("You missed!")
        elif crit:
            events.append(f"CRITICAL HIT! You dealt {dmg} damage!")
        else:
            events.append(f"You dealt {dmg} damage!")
        # check if enemy alive
        if not enemy.is_alive:
            # if boss killed, GAME WON
            if is_boss == True:
                status = "game won"
                events.append(f"{enemy.name} TERMINATED!")
                events.append(f"Congratulations {character.name}!")
                events.append("Your Final Project is completed.")
            # regular enemy killed, continue on map
            else:
                status = "victory"
                events.append(f"{enemy.name} solved!")
            return status, events
        status = "continue"
    
    # heal
    elif action == "H":
        if character.hp_potions == 0:
            events.append("No coffee available")
            status = "no potions"
            return status, events
        else:
            healed = character.use_hp_potion()
            events.append(f"Coffee restored {healed} sanity!")
            status = "continue"
    
    # run away
    elif action == "R":
        # checks if boss. cant run from boss
        if is_boss == True:
            events.append("EscapeError: You are stuck in an Infinite Loop!")
            status = "continue"
        else:
            quit_roll = random.randint(1, 100)
            # higher than 50% chance to run away from combat
            if quit_roll > 40:
                status = "run"
                events.append("You successfully postponed all issues!")
                return status, events
            else:
                events.append("EscapeError: Could not escape!")
                status = "continue"
    else:
        events.append("Wrong key")
        status = "invalid"
        return status, events
    
    # enemy attacks (after player attack/heal/unsuccessfull run)
    # adds second position to events list
    dmg, dodge, crit = attack(enemy, character)
    if dodge:
        events.append("You dodged!")
    elif dmg == 0:
        events.append("Enemy missed!")
    elif crit:
        events.append(f"CRITICAL ERROR! {enemy.name} reduced Your sanity by {dmg}!")
    else:
        events.append(f"{enemy.name} reduced Your sanity by {dmg}!")

    # check if player alive
    if not character.is_alive:
        status = "defeated"
        # if killed by boss, special game over 
        if is_boss == True:
            events.append("RecursionError: Maximum frustration level exceeded!")
            events.append("STACK OVERFLOW")
            events.append("GAME OVER")
        # if killed by regular mob
        else:
            events.append("You have been defeated!")

    return status, events


def start_combat(character, enemy, is_boss=False):
    round_number = 1
    # checks if boss fight
    if is_boss == True:
        print("You enter the final part of Your code...")
        print(f"WARNING: {enemy.name} detected!")
    else:
    # start of combat, random encounter
        print(f"An unexpected {enemy.name} appears!")
    while True:
        # prints basic stats
        print("=====================================================")
        print(f"Student Sanity: {character.hp}/{character.max_hp}")
        print(f"{enemy.name} HP: {enemy.hp}/{enemy.max_hp}")
        print()
        print(f"Coffee available: {character.hp_potions}")
        print("=====================================================")
        # ask for input loop
        while True:
            print("[A] Debug | [H] Drink Coffee | [R] Run away from problems")
            key_pressed = input("> ").strip().upper()

            # start combat round
            status, events = combat_round(character, enemy, key_pressed, is_boss)

            if status not in ("invalid", "no potions", "run"):
                print(f"ROUND {round_number}")

            for position in events:
                print(position)
            # no potions
            if status == "no potions":
                continue
            # invalid key
            if status == "invalid":
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
        print(f"You gained {xp_gained} points of Python Experience!")
        if levels_amount > 0:
            print(f"You gained {levels_amount} {p.plural_noun('level', levels_amount)}!")
    return status
        


# testing random things
if __name__ == "__main__":     
    plr = player.Player("Warrior")
    syntax_error1 = monster.generate_monster("SyntaxError")

    # print(plr.is_alive)
    # print(syntax_error1.is_alive)
    # print(combat_round(plr, syntax_error1, "A"))
    # print(plr)
    # print(syntax_error1)


    print(start_combat(plr, syntax_error1))
