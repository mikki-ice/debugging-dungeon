import random

# monster typ templates (nested dictionary) MONSTERS[name][atribute] to get names atribute value. /// 
MONSTERS = {
    # lvl 1
    "SyntaxError": {
        "max_hp": (15, 22),
        "attack": (10, 12),
        "defense": (2, 4),
        "dexterity": (0, 1),
        "xp_reward": (150, 2000),
    },
    # lvl 1-2
    "TypeError": {
        "max_hp": (10, 19),
        "attack": (5, 9),
        "defense": (5, 6),
        "dexterity": (2, 4),
        "xp_reward": (10, 2000),
    },
    # lvl 2
    "ZeroDivisionError": {
        "max_hp": (10, 19),
        "attack": (5, 9),
        "defense": (5, 6),
        "dexterity": (2, 4),
        "xp_reward": (10, 20),
    },
    # Final Boss
    "Infinite Loop": {
        "max_hp": (16, 25),
        "attack": (8, 13),
        "defense": (4, 9),
        "dexterity": (4, 6),
        "xp_reward": (20, 35),
    },
}


# same class for all monster types
class Monster:
    def __init__(self, name, max_hp, attack, defense, dexterity, xp_reward):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
        self._attack = attack
        self._defense = defense
        self._dexterity = dexterity
        self._xp_reward = xp_reward

    # take damage equal or less than current hp
    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("negative damage")
        if amount > self._hp:
            amount = self._hp
        self._hp -= amount
        return amount

    def __str__(self):
        return (f"Monster type: {self._name}\n"
                f"HP: {self._hp}/{self._max_hp}\n"
                f"Attack: {self._attack} | Defense: {self._defense}\n"
        )

    @property
    def hp(self):
        return self._hp

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def name(self):
        return self._name
    
    @property
    def attack(self):
        return self._attack

    @property
    def defense(self):
        return self._defense

    @property
    def dexterity(self):
        return self._dexterity

    # calculate value and returns
    @property 
    def is_alive(self):
        return self._hp > 0

    # gives value to others 
    @property
    def xp_reward(self):
        return self._xp_reward

# monster generator
def generate_monster(monster_type):
    if monster_type not in MONSTERS:
        raise ValueError("monster not in a template dictionary")
    
    template = MONSTERS[monster_type]

    hp_range = template["max_hp"]
    hp = random.randint(hp_range[0], hp_range[1])

    attack_range = template["attack"]
    attack = random.randint(attack_range[0], attack_range[1])

    defense_range = template["defense"]
    defense = random.randint(defense_range[0], defense_range[1])

    dexterity_range = template["dexterity"]
    dexterity = random.randint(dexterity_range[0], dexterity_range[1])

    xp_reward_range = template["xp_reward"]
    xp_reward = random.randint(xp_reward_range[0], xp_reward_range[1])
    # create new monster object from class 
    new_monster = Monster(monster_type, hp, attack, defense, dexterity, xp_reward)
    return new_monster


# testing random things
if __name__ == "__main__":

    r_key = random.choice(list(MONSTERS))
    print(r_key)

    mons = MONSTERS["SyntaxError"]["attack"]
    print(mons)
    
    # numb = 1
    # random_m = MONSTERS[numb]
    
    # template = MONSTERS["SyntaxError"]
    # hp_range = template["max_hp"]
    # print(template)
    # print(hp_range)
    # print(hp_range[0], "|||", hp_range[1])

    # syntax_error1 = generate_monster("SyntaxError")


    # print(syntax_error1)
