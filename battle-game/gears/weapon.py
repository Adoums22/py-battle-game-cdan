
class Weapon:
    def __init__(self, name:str, damage:int = 10) :
        self.name = name
        self.damage = damage

    def get_name(self) : 
        return self.name
    
    def set_name(self, new_name) :
        self.name = new_name
    
    def get_damage(self) :
        return self.damage

    def set_damage(self, new_damage) :
        self.damage = new_damage
