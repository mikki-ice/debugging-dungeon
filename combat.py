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


if __name__ == "__main__":     
    character = player.Player("Jelad")
    rat = monster.generate_monster("Rat")

    print(rat)
    print(attack(character, rat))
    print(rat)
    print(attack(character, rat))
    print(rat)
    print(attack(character, rat))
    print(rat)
    print(attack(character, rat))
    print(rat)