from characters.character import Character  
from gears.armor import Armor
from gears.weapon import Weapon
from typing import Self
class Barbar(Character):
    def __init__(self, hp: int, name: str, weapon: Weapon, armor: Armor):
        super().__init__(hp, name, weapon, armor)

    def attack(self, other:Self):
        # Attaque une première fois en utilisant la méthode de la classe parent
        super().attack(other)

        # Attaque une deuxième fois
        super().attack(other)
