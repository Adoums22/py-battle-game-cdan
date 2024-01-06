from characters.character import Character  
from gears.spell import Spell
from gears.armor import Armor
from gears.weapon import Weapon
from typing import Self
from typing import List
class Wizard(Character):
    def __init__(self, hp: int, name: str, weapon: Weapon, armor: Armor, spells: List[Spell], mana):
        super().__init__(hp, name, weapon, armor)
        self.spells = spells
        self.mana = mana

    def list_spells(self):
        print("Available spells:")
        for i, spell in enumerate(self.spells, 1):
            print(f"{i}. {spell.name} (Damage: {spell.damage}, Mana: {spell.mana})")

    def cast_spell(self, other: 'Character'):
        self.list_spells()
        choice = input("Choose a spell by entering its number: ")

        try:
            spell_index = int(choice) - 1
            if 0 <= spell_index < len(self.spells):
                selected_spell = self.spells[spell_index]
                if self.mana >= selected_spell.mana:
                    print(f"{self.name} casts {selected_spell.name} at {other.name}")
                    self.mana -= selected_spell.mana
                    other.set_hp(other.get_hp() - selected_spell.damage)
                else:
                    print("Not enough mana to cast the spell!")
            else:
                print("Invalid spell choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def attack(self, other:Self):
        valid_choice = False
        
        while not valid_choice:
            choice = input("Do you want to attack with your weapon or cast a spell? (weapon/spell): ").lower()

            if choice == "weapon":
                super().attack(other)  # Attaque avec l'arme en utilisant la méthode de la classe parente
                valid_choice = True
            elif choice == "spell":
                self.cast_spell(other)
                valid_choice = True
            else:
                print("Invalid choice. Choose 'weapon' or 'spell'.")