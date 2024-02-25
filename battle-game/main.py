from arena.arena import Arena
from characters.barbar import Barbar
from characters.wizard import Wizard
from gears.weapon import Weapon
from gears.armor import Armor
from gears.spell import Fireball
from colorama import Fore, Style

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

def choose_barbarian():
    print("\n" + Fore.BLUE + "-"*25 + " Choose Your Weapon " + "-"*25 + Style.RESET_ALL)
    print(f"{Fore.BLUE}{'Index':<10}{'Name':<20}{'Damage':<10}{Style.RESET_ALL}")
    for i, weapon in enumerate(list_of_barbar_weapon, 1):
        print(f"{Fore.GREEN}{i:<10}{weapon.name:<20}{weapon.damage:<10}{Style.RESET_ALL}")

    while True:
        try:
            weapon_choice = int(input("Enter your weapon choice: "))
            if 1 <= weapon_choice <= len(list_of_barbar_weapon):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and", len(list_of_barbar_weapon))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    selected_weapon = list_of_barbar_weapon[weapon_choice - 1]

    print("\n" + Fore.BLUE + "-"*25 + " Choose Your Armor " + "-"*25 + Style.RESET_ALL)
    print(f"{Fore.BLUE}{'Index':<10}{'Name':<20}{'Damage':<10}{Style.RESET_ALL}")
    for i, armor in enumerate(list_of_barbar_armor, 1):
        print(f"\033[92m{i:<10}{armor.name:<20}{armor.defense:<10}\033[0m")
    while True:
        try:
            armor_choice = int(input("Enter your armor choice: "))
            if 1 <= armor_choice <= len(list_of_barbar_armor):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and", len(list_of_barbar_armor))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    selected_armor = list_of_barbar_armor[armor_choice - 1]
    name = input("Enter your character's name: ")
    return Barbar(100, name, selected_weapon, selected_armor)

def choose_wizard():
    print("\n" + Fore.MAGENTA + "-"*25 + " Choose Your Weapon " + "-"*25 + Style.RESET_ALL)
    print(f"{Fore.MAGENTA}{'Index':<10}{'Name':<20}{'Damage':<10}{Style.RESET_ALL}")
    for i, weapon in enumerate(list_of_wizard_weapon, 1):
        print(f"{Fore.GREEN}{i:<10}{weapon.name:<20}{weapon.damage:<10}{Style.RESET_ALL}")
    while True:
        try:
            weapon_choice = int(input("Enter your weapon choice: "))
            if 1 <= weapon_choice <= len(list_of_wizard_weapon):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and", len(list_of_wizard_weapon))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    selected_weapon = list_of_wizard_weapon[weapon_choice - 1]

    print("\n" + Fore.MAGENTA + "-"*25 + " Choose Your Armor " + "-"*25 + Style.RESET_ALL)
    print(f"{Fore.MAGENTA}{'Index':<10}{'Name':<20}{'Damage':<10}{Style.RESET_ALL}")
    for i, armor in enumerate(list_of_wizard_armor, 1):
        print(f"\033[92m{i:<10}{armor.name:<20}{armor.defense:<10}\033[0m")
    while True:
        try:
            armor_choice = int(input("Enter your armor choice: "))
            if 1 <= armor_choice <= len(list_of_wizard_armor):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and", len(list_of_wizard_armor))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    selected_armor = list_of_wizard_armor[armor_choice - 1]

    name = input("Enter your character's name: ")
    return Wizard(100, name, selected_weapon, selected_armor, list_of_spells, 10)

player1 = choose_character()
player2 = choose_character()
arena = Arena(player1, player2)
arena.fight()