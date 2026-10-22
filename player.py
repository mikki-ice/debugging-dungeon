import ui

class Player:
    def __init__(self, name):
        self._name = name
        self._max_hp = 50
        self._hp = self._max_hp
        self._level = 1
        self._xp = 0
        self._attack = 10
        self._defense = 5
        self._dexterity = 2
        self._hp_potions = 2
        self._hp_potions_max = 2
        self._hp_potion_regen = 0
        # self._xp_to_next = self.xp_to_next

    # take damage equal or less than current hp
    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("negative damage")
        if amount > self._hp:
            amount = self._hp
        self._hp -= amount
        return amount

    # calculate missing hp and heals to max_hp or less
    def heal(self, amount):
        missing_hp = self._max_hp - self._hp
        # check if negative amount
        if amount < 0:
            raise ValueError("negative heal")
        # if full hp, do nothing
        if self._hp == self._max_hp:
            return 0
        # max heal if overhealed
        elif amount > missing_hp:
            amount = missing_hp
        self._hp += amount 
        return amount

    # using potion (heals for percent of max hp)
    def use_hp_potion(self):
        if self._hp_potions > 0:
            heals_for_percent = 0.45
            hp_heal = self._max_hp * heals_for_percent
            hp_heal = round(hp_heal)
            healed = self.heal(hp_heal)
            self._hp_potions -= 1
            return healed

    # self regenerating hp potions
    def potion_regen(self):
        if self._hp_potions < self._hp_potions_max:
            self._hp_potion_regen += 1
            if self._hp_potion_regen == 4:
                self._hp_potions += 1
                self._hp_potion_regen = 0
                
    # leveling
    def level_up(self):
        self._level += 1
        self._max_hp += 20
        self._hp = self._max_hp
        self._attack += 5
        self._defense += 2
        self._dexterity += 1

    # add xp and run level_up
    def add_xp(self, amount):  
        added_levels = 0
        # checks negative value
        if amount < 0:
            raise ValueError("negative XP")
        self._xp += amount
        while self._xp >= self.xp_to_next:
            self._xp -= self.xp_to_next
            self.level_up()
            added_levels += 1
        return added_levels


    def __str__(self):
        return (f"======{ui.GREEN} DEVELOPER STATUS {ui.RESET}======\n"
                f"Name: {self._name}\n"
                f"Debugging Level: {self._level}\n"
                f"Sanity: {self._hp}/{self._max_hp}\n"
                f"Debug power: {self._attack} | Error resistance: {self._defense} | Typing speed: {self._dexterity}\n"
                f"Python Experience: {self._xp}/{self.xp_to_next}\n"
                f"Coffee available: {self._hp_potions}\n"
                f"=============================="
        )


    # guards hp so it cannot be changed in other places 
    @property
    def hp(self):
        return self._hp
    
    # guards max hp
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

    @property 
    def is_alive(self):
        return self._hp > 0

    @property
    def hp_potions(self):
        return self._hp_potions

    @property
    def xp_to_next(self):
        return self._level * 100


# testing random things
if __name__ == "__main__":
    char = Player("John")
    print(char)
    levels_added = char.add_xp(9712)
    print(char)
    print(levels_added)
