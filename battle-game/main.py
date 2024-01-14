from arena.arena import Arena
from characters.barbar import Barbar
from characters.wizard import Wizard
from gears.weapon import Weapon
from gears.armor import Armor
from gears.spell import Fireball

#Instanciation 
list_of_spells = [Fireball()]
knife = Weapon('Couteau')
gun = Weapon ('Deagle', 50)
mini_shield = Armor('Mini Shield', 25)
gros_shield = Armor('Gros Shield', 50)
adel = Wizard(100, 'Adel', gun, mini_shield, list_of_spells, 10)
Kevin = Barbar(100, 'Kevin', knife, gros_shield)
arena = Arena(Kevin, adel)

print(adel.get_armor())
arena.fight()
