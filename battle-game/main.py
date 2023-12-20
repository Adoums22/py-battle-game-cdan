from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor

#Instanciation 
knife = Weapon('Couteau')
gun = Weapon ('Deagle', 50)
mini_shield = Armor('Mini Shield', 25)
gros_shield = Armor('Gros Shield', 50)
adel = Character(100, 'Adel', gun, mini_shield)
Kevin = Character(100, 'Kevin', knife, gros_shield)
print(adel.armor.defense)
print(Kevin.armor.defense)
# Test Méthode
adel.attack(Kevin)
print("Results: ")
print(adel.name, adel.hp, "HP")  # Affiche les points de vie d'Adel
print(adel.name, adel.armor.get_defense(), "Armor")  # Affiche la défense d'armure d'Adel
print(Kevin.name, Kevin.hp, "HP")  # Affiche les points de vie de Kevin
print(Kevin.name, Kevin.armor.get_defense(), "Armor")  # Affiche la défense d'armure de Kevin

input("------------------")
Kevin.attack(adel)
print("Results: ")
print(adel.name, adel.hp, "HP")
print(adel.name, adel.armor.defense, "HP")
print(Kevin.name, Kevin.hp, "HP")
print(Kevin.name, Kevin.armor.defense, "HP")
input("------------------")
