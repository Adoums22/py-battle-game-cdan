from characters.character import Character  
from gears.armor import Armor
from gears.weapon import Weapon
from typing import Self
class Barbar(Character):
    def __init__(self, hp: int, name: str, weapon: Weapon, armor: Armor):
        super().__init__(hp, name, weapon, armor)

    def attack(self, other: Character):
        damage_dealt = self.weapon.damage

        # Attaque une fois en utilisant la méthode de la classe parente
        super().attack(other, damage_dealt)
         # Attaque une deuxieme fois en utilisant la méthode de la classe parente
        super().attack(other, damage_dealt)