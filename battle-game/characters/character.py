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
        return self.hp

    def set_hp(self, new_hp):
        self.hp = new_hp

    # Getter name
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    # Getter weapon
    def get_weapon(self):
        return self.weapon

    def set_weapon(self, new_weapon):
        self.weapon = new_weapon

    # Getter armor
    def get_armor(self):
        return self.armor.defense

    def set_armor(self, new_armor):
        self.armor = new_armor

    def attack(self, other:Self):
        damage_dealt = self.weapon.damage

        other_armor_defense = other.armor.get_defense()

        # Réduire la défense de l'armure de l'autre personnage
        if damage_dealt >= other_armor_defense:
            damage_dealt -= other_armor_defense
            other.armor.set_defense(0)
        else:
            other.armor.set_defense(other_armor_defense - damage_dealt)
            damage_dealt = 0

        # Infliger les dégâts restants aux points de vie du personnage
        other.set_hp(other.get_hp() - damage_dealt)
