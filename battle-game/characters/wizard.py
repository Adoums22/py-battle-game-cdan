from characters.character import Character  
from gears.spell import Spell
from gears.armor import Armor
from gears.weapon import Weapon
from typing import Self
from typing import List
from gears.spell import Fireball, ShadowBlast, DevastationOfSpirits
class Wizard(Character):
    def __init__(self, hp: int, name: str, weapon: Weapon, armor: Armor, spells: List[Spell], mana:int = 10):
        super().__init__(hp, name, weapon, armor)
        self.spells = [Fireball(), ShadowBlast(), DevastationOfSpirits()]
        self.mana = mana
        self.first_turn = True

    def list_spells(self):
        print("\033[1mAvailable spells:\033[0m")  # Titre en gras
        for i, spell in enumerate(self.spells, 1):
            print(f"{i}. \033[96m{spell.name}\033[0m (Damage: \033[93m{spell.damage}\033[0m, Mana: \033[93m{spell.mana}\033[0m)")  # Cyan pour le nom du sort, jaune pour les dégâts et la mana

    def cast_spell(self, other: 'Character'):
        while True:
            self.list_spells()
            print(f"\033[96m{self.name}\033[0m's current mana: \033[93m{self.mana}\033[0m")  # Cyan pour le nom du personnage, jaune pour la mana
            choice = input("Choose a spell by entering its number (or type '\033[1mback\033[0m' to go back): ")  # Retour en gras

            if choice.lower() == 'back':
                return  # Retournez à la boucle principale pour choisir entre arme et sort
            try:
                spell_index = int(choice) - 1
                if 0 <= spell_index < len(self.spells):
                    selected_spell = self.spells[spell_index]
                    if self.mana >= selected_spell.mana:
                        print(f"\033[96m{self.name}\033[0m casts \033[96m{selected_spell.name}\033[0m at \033[91m{other.name}\033[0m")  # Cyan pour le nom du personnage et du sort, rouge pour le nom de l'autre personnage
                        self.mana -= selected_spell.mana
                        other.set_hp(other.get_hp() - selected_spell.damage)
                        print(f"\033[96m{self.name}\033[0m's remaining mana: \033[93m{self.mana}\033[0m")  # Cyan pour le nom du personnage, jaune pour la mana
                        return  # Sortez de la boucle si le sort est lancé avec succès
                    else:
                        print("\033[91mNot enough mana to cast the spell! Choose another spell.\033[0m")  # Rouge pour le message d'erreur
                else:
                    print("\033[91mInvalid spell choice.\033[0m")  # Rouge pour le message d'erreur
            except ValueError:
                print("\033[91mInvalid input. Please enter a valid number.\033[0m")  # Rouge pour le message d'erreur

    def attack(self, other:Self):
        valid_choice = False
        
        while not valid_choice:
            # Incrémentez la mana à partir du deuxième tour
            if not self.first_turn:
                self.mana += 1
            else:
                self.first_turn = False
            choice = input("Do you want to attack with your weapon or cast a spell? (weapon/spell): ").lower()

            if choice == "weapon":
                damage_dealt = self.weapon.damage
                super().attack(other, damage_dealt)  # Attaque avec l'arme en utilisant la méthode de la classe parente
                valid_choice = True
            elif choice == "spell":
                self.cast_spell(other)
                valid_choice = True
            else:
                print("Invalid choice. Choose 'weapon' or 'spell'.")