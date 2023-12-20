from gears.armor import Armor
from gears.weapon import Weapon
from typing import Self

class Character:

    def __init__(self, hp:int, name:str , weapon:Weapon, armor:Armor) :
        self.hp = hp
        self.name = name
        self.weapon = weapon
        self.armor = armor

    # Getter pour hp
    def get_hp(self):
        return self._hp

    def set_hp(self, new_hp):
        self._hp = new_hp

    # Getter name
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    # Getter weapon
    def get_weapon(self):
        return self._weapon

    def set_weapon(self, new_weapon):
        self._weapon = new_weapon

    # Getter armor
    def get_armor(self):
        return self._armor

    def set_armor(self, new_armor):
        self._armor = new_armor

    def attack(self, other:Self) :
        other.armor.defense -= self.weapon.damage