from characters.barbar import Weapon

# Initialisation des armes pour le personnage Barbarian
barbarian_weapons = {
    "Knife": Weapon("Knife", 10),
    "Axe": Weapon("Axe", 15),
    "Club": Weapon("Club", 12),
    "Sword": Weapon("Sword", 18)
}

# Initialisation des armes pour le personnage Wizard
wizard_weapons = {
    "Staff": Weapon("Staff", 20),
    "Wand": Weapon("Wand", 15),
    "Orb": Weapon("Orb", 25),
    "Scroll": Weapon("Scroll", 15)
}

# Initialisation des armes pour les monstres en fonction de la difficulté
monster_weapons = {
    "easy": [Weapon("Claws", 15), Weapon("Fangs", 10), Weapon("Spiked Tail", 20)],
    "medium": [Weapon("Spike Club", 30), Weapon("Boulder Throw", 25), Weapon("Barbed Tentacles", 35)],
    "hard": [Weapon("Giant Axe", 50), Weapon("Flaming Breath", 40), Weapon("Venomous Stinger", 45)]
}
