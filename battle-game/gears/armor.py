

class Armor:
    def __init__(self, name:str, defense:int = 0) :
        self.name = name
        self.defense = defense
        
    def get_name(self) : 
        return self.name
    
    def get_defense(self) :
        return self.defense
    
    def set_name(self, new_name) :
        self.name = new_name
    
    def set_defense(self, new_defense) :
        self.defense = new_defense