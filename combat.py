import monster
import player
import random
import world


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

def combat_round(character, enemy):
    events = []
    # player starts attack
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
        status = "victory"
        events.append(f"{enemy.name} defeated!")
        return status, events
    status = "continue"
    # enemy attacks
    dmg, dodge, crit = attack(enemy, character)
    if dodge:
        events.append("You dodged!")
    elif dmg == 0:
        events.append("Enemy missed!")
    elif crit:
        events.append(f"CRITICAL HIT! Enemy hits for {dmg} damage!")
    else:
        events.append(f"Enemy hits for {dmg} damage!")
    # check if player alive
    if not character.is_alive:
        status = "defeated"
        events.append(f"You have been defeated!")
        return status, events
    return status, events




    # player_dead = False
    # monster_dead = False
    # attack(character, enemy)
    # if not enemy.is_alive:
    #     monster_dead = True
    #     return monster_dead
    # attack(enemy, character)
    # if not character.is_alive:
    #     player_dead = True
    #     return player_dead

if __name__ == "__main__":     
    plr = player.Player("Jelad")
    rat = monster.generate_monster("Rat")

    print(plr.is_alive)
    print(rat.is_alive)
    print(combat_round(plr, rat))
    print(plr.is_alive)
    print(rat.is_alive)

