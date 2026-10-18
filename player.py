class Player:
    def __init__(self, name):
        self._name = name
        self._max_hp = 100
        self._hp = 100
        self._level = 1
        self._xp = 0
        self._attack = 10
        self._defense = 5
        self._dexterity = 5

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

    # take damage equal or less than current hp
    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("negative damage")
        if amount > self._hp:
            amount = self._hp
        self._hp -= amount
        return amount

    # RIP
    def death(self):
        if self._hp <= 0:
            return True
        return False

    # calculate missing hp and heals to max_hp or less
    def heal(self, amount):
        missing_hp = self._max_hp - self._hp
        if amount < 0:
            raise ValueError("negative heal")
        # if full hp, do nothing
        if self._hp == self._max_hp:
            return 0
        elif amount > missing_hp:
            amount = missing_hp
        self._hp += amount
        return amount

    def __str__(self):
        return (f"Name: {self._name}\n"
                f"Level: {self._level}\n"
                f"HP: {self._hp}/{self._max_hp}\n"
                f"Attack: {self._attack} | Defense: {self._defense} | Dexterity: {self._dexterity}\n"
                f"XP: {self._xp}"
        )