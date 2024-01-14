
class Spell:
    def __init__(self, name:str, damage:int = 0, mana:int = 0) :
        self.name = name
        self.damage = damage
        self.mana = mana

    def get_name(self) : 
        return self.name
    
    def get_damage(self) :
        return self.damage
    
    def get_mana(self) : 
        return self.mana
    
    def set_name(self, new_name) :
        self.name = new_name
    
    def set_damage(self, new_damage) :
        self.damage = new_damage

    def set_mana(self, new_mana) :
        self.mana = new_mana

class Fireball(Spell):
    def __init__(self):
        super().__init__(name="Fireball", damage=20, mana=5)