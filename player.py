class Player:
    def __init__(self, name):
        self._name = name
        self._max_hp = 50
        self._hp = self._max_hp
        self._level = 1
        self._xp = 0
        self._attack = 20
        self._defense = 5
        self._dexterity = 50
        self._hp_potions = 2
        self._hp_potions_max = 2
        self._hp_potion_regen = 0

    # take damage equal or less than current hp
    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("negative damage")
        if amount > self._hp:
            amount = self._hp
        self._hp -= amount
        return amount

    # calculate missing hp and heals to max_hp or less if hp potion available
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

    # using potion
    def use_hp_potion(self):
        if self._hp_potions > 0:
            hp_heal = self._max_hp * 0.6
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
                



    def __str__(self):
        return (f"Name: {self._name}\n"
                f"Level: {self._level}\n"
                f"HP: {self._hp}/{self._max_hp}\n"
                f"Attack: {self._attack} | Defense: {self._defense} | Dexterity: {self._dexterity}\n"
                f"XP: {self._xp}"
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