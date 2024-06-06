from Fortuna import random_int, random_value


class Monster:
    monster_names = (
        "Goblin",
        "Troll",
        "Ogre",
        "Giant",
        "Vampire",
        "Dragon",
    )

    def __init__(self):
        self.name = random_value(self.monster_names)
        self.level = random_int(1, 10)

    def __repr__(self):
        """ Repr is required for printing Monsters within a list """
        return f"Monster({self.name}, {self.level})"
