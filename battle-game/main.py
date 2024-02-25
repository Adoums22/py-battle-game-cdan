import random
from arena.arena import Arena
from characters.barbar import Barbar
from characters.wizard import Wizard
from characters.monster import Monster
from gears.weapon import Weapon
from gears.armor import Armor
from gears.spell import Fireball
from colorama import Fore, Style
import config.weapon_config  

#Instanciation 
list_of_spells = [Fireball()]

knife = Weapon('Knife', 10)
axe = Weapon('Axe', 15)
club = Weapon('Club', 12)
sword = Weapon('Sword', 18)
list_of_barbar_weapon = [knife, axe, club, sword]

staff = Weapon('Staff', 20)
wand = Weapon('Wand', 15)
orb = Weapon('Orb', 25)
scroll = Weapon('Scroll', 15)
list_of_wizard_weapon = [staff, wand, orb, scroll]

leather_armor = Armor('Leather Armor', 30)
hide_shield = Armor('Hide Shield', 40)
iron_plate = Armor('Iron Plate', 50)
list_of_barbar_armor = [leather_armor, hide_shield, iron_plate]

robe = Armor('Robe', 20)
cloak = Armor('Cloak', 25)
enchanted_amulet = Armor('Enchanted Amulet', 30)
list_of_wizard_armor = [robe, cloak, enchanted_amulet]


# Armures des monstres en fonction de la difficulté
monster_armors = {
    "easy": [Armor("Leather Hide", 20), Armor("Chitin Shell", 15), Armor("Thick Fur", 25)],
    "medium": [Armor("Iron Plating", 20), Armor("Reinforced Scales", 25), Armor("Obsidian Carapace", 35)],
    "hard": [Armor("Dragon Scales", 80), Armor("Mithril Armor", 70), Armor("Ethereal Mantle", 90)]
}

# Initialisation des armes pour les monstres en fonction de la difficulté
monster_weapons = {
    "easy": [Weapon("Claws", 15), Weapon("Fangs", 10), Weapon("Spiked Tail", 20)],
    "medium": [Weapon("Spike Club", 30), Weapon("Boulder Throw", 25), Weapon("Barbed Tentacles", 35)],
    "hard": [Weapon("Giant Axe", 50), Weapon("Flaming Breath", 40), Weapon("Venomous Stinger", 45)]
}

def set_difficulty():
    while True:
        difficulty = input("\033[1mChoose difficulty level:\n \033[94m1: easy\n \033[93m2: medium\n \033[91m3: hard\n\033[0m")
        if difficulty in ["1", "2", "3"]:
            return int(difficulty)  # Retourne la difficulté sélectionnée sous forme d'entier
        else:
            print("\033[91mInvalid input. Please choose 1, 2, or 3 for difficulty level.\033[0m")

def set_monster(difficulty):
    difficulty_mapping = {1: "easy", 2: "medium", 3: "hard"}
    monster_difficulty = difficulty_mapping[difficulty]
    # Création d'un monstre avec une arme et une armure aléatoires en fonction de la difficulté
    monster_weapon = random.choice(monster_weapons[monster_difficulty])
    monster_armor = random.choice(monster_armors[monster_difficulty])

    # Création du monstre avec l'arme et l'armure sélectionnées aléatoirement
    return Monster(100, "Ogre", monster_weapon, monster_armor, difficulty, difficulty)

def choose_character():
    print("Choose your character:")
    print(f"{Fore.BLUE}1. Barbarian{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}2. Wizard{Style.RESET_ALL}")
    choice = input("Enter your choice: ")
    if choice == "1":
        return choose_barbarian()
    elif choice == "2":
        return choose_wizard()
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        return choose_character()

from colorama import Fore, Style

def choose_barbarian():
    print("\n" + Fore.BLUE + "-"*25 + " Choose Your Weapon " + "-"*25 + Style.RESET_ALL)
    print(f"{Fore.BLUE}{'Index':<10}{'Name':<20}{'Damage':<10}{Style.RESET_ALL}")

    for i, weapon in enumerate(list_of_barbar_weapon, 1):
        print(f"{Fore.GREEN}{i:<10}{weapon.name:<20}{weapon.damage:<10}{Style.RESET_ALL}")

    selected_weapon = choose_item(list_of_barbar_weapon, "weapon")

    print("\n" + Fore.BLUE + "-"*25 + " Choose Your Armor " + "-"*25 + Style.RESET_ALL)
    print(f"{Fore.BLUE}{'Index':<10}{'Name':<20}{'Defense':<10}{Style.RESET_ALL}")

    for i, armor in enumerate(list_of_barbar_armor, 1):
        print(f"\033[92m{i:<10}{armor.name:<20}{armor.defense:<10}\033[0m")

    selected_armor = choose_item(list_of_barbar_armor, "armor")
    
    name = input("Enter your character's name: ")
    return Barbar(100, name, selected_weapon, selected_armor)

def choose_item(item_list, item_type):
    while True:
        try:
            choice = int(input(f"Enter your {item_type} choice: "))
            if 1 <= choice <= len(item_list):
                return item_list[choice - 1]
            else:
                print(Fore.RED + f"Invalid choice. Please enter a number between 1 and {len(item_list)}" + Fore.RESET)
        except ValueError:
            print(Fore.RED +"Invalid input. Please enter a valid number."+ Fore.RESET)

def choose_wizard():
    print("\n" + Fore.MAGENTA + "-"*25 + " Choose Your Weapon " + "-"*25 + Style.RESET_ALL)
    print(f"{Fore.MAGENTA}{'Index':<10}{'Name':<20}{'Damage':<10}{Style.RESET_ALL}")

    for i, weapon in enumerate(list_of_wizard_weapon, 1):
        print(f"\033[92m{i:<10}{weapon.name:<20}{weapon.damage:<10}\033[0m")

    selected_weapon = choose_item(list_of_wizard_weapon, "weapon")

    print("\n" + Fore.MAGENTA + "-"*25 + " Choose Your Armor " + "-"*25 + Style.RESET_ALL)
    print(f"{Fore.MAGENTA}{'Index':<10}{'Name':<20}{'Defense':<10}{Style.RESET_ALL}")

    for i, armor in enumerate(list_of_wizard_armor, 1):
        print(f"\033[92m{i:<10}{armor.name:<20}{armor.defense:<10}\033[0m")

    selected_armor = choose_item(list_of_wizard_armor, "armor")
    
    name = input("Enter your character's name: ")
    return Wizard(100, name, selected_weapon, selected_armor, list_of_spells, 10)


difficulty = set_difficulty()
monster = set_monster(difficulty)
player1 = choose_character()
arena = Arena(player1, monster)
arena.fight()