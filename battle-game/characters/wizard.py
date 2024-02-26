from colorama import Fore, Style
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
        print(f"{Style.BRIGHT}Available spells:{Style.RESET_ALL}")  # Titre en gras
        for i, spell in enumerate(self.spells, 1):
            print(f"{i}. {Fore.CYAN}{spell.name}{Style.RESET_ALL} (Damage: {Fore.YELLOW}{spell.damage}{Style.RESET_ALL}, Mana: {Fore.YELLOW}{spell.mana}{Style.RESET_ALL}")  # Cyan pour le nom du sort, jaune pour les dégâts et la mana

    def cast_spell(self, other:Self):
        while True:
            self.list_spells()
            print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL}'s current mana: {Fore.YELLOW}{self.mana}{Style.RESET_ALL}")  # Cyan pour le nom du personnage, jaune pour la mana
            choice = input("Choose a spell by entering its number (or type 'back' to go back): ")  # Retour en gras

            if choice.lower() == 'back':
                return  # Retournez à la boucle principale pour choisir entre arme et sort
            try:
                spell_index = int(choice) - 1
                if 0 <= spell_index < len(self.spells):
                    selected_spell = self.spells[spell_index]
                    if self.mana >= selected_spell.mana:
                        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} casts {Fore.CYAN}{selected_spell.name}{Style.RESET_ALL} at {Fore.RED}{other.name}{Style.RESET_ALL}")  # Cyan pour le nom du personnage et du sort, rouge pour le nom de l'autre personnage
                        self.mana -= selected_spell.mana
                        other.set_hp(other.get_hp() - selected_spell.damage)
                        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL}'s remaining mana: {Fore.YELLOW}{self.mana}{Style.RESET_ALL}\n")  # Cyan pour le nom du personnage, jaune pour la mana
                        return  # Sortez de la boucle si le sort est lancé avec succès
                    else:
                        print(f"{Fore.RED}Not enough mana to cast the spell! Choose another spell.{Style.RESET_ALL}")  # Rouge pour le message d'erreur
                else:
                    print(f"{Fore.RED}Invalid spell choice.{Style.RESET_ALL}")  # Rouge pour le message d'erreur
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a valid number.{Style.RESET_ALL}")  # Rouge pour le message d'erreur

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