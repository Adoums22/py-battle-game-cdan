from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor

#Instanciation 
knife = Weapon('Couteau')
gun = Weapon ('Deagle', 50)
mini_shield = Armor('Mini Shield', 25)
adel = Character(100, 'Adel', gun, mini_shield)
Kevin = Character(100, 'Kevin', knife, mini_shield)

#Test Methode
adel.attack(Kevin)
print(Kevin.get_armor())
print(Kevin.get_hp())