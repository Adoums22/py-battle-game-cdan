from characters.character import Character  
from gears.armor import Armor
from gears.weapon import Weapon
class Monster(Character):
    def __init__(self, hp: int, name: str, weapon: Weapon, armor: Armor, strength: int, difficulty: str):
        super().__init__(hp, name, weapon, armor)
        self.strength = strength
        self.difficulty = difficulty
        
    def set_strength(self):
        return self.strength

    def get_strength(self, value):
        self.strength = value

    def set_difficulty(self, value):
        self.difficulty = value 

    def get_difficulty(self):
        return self.difficulty   
    
    def set_hp(self, new_hp: int):
        self.hp = new_hp

    def get_hp(self):
        return self.hp

    def attack(self, other: Character):
        # Calculer les dégâts basés sur les dégâts de l'arme multipliés par la force du monstre
        damage_dealt = self.weapon.damage * self.strength

        # Appeler la méthode attack de la classe parente pour infliger les dégâts ajustés
        super().attack(other, damage_dealt)