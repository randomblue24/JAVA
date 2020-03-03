import platform

print(platform.python_version())

class Character():

    def __init__(self, name, age, upbringing):
        self.name=name
        #self.age=age
        if not isinstance(age, int):
            raise TypeError("bar must be set to an integer")
        self.upbringing=upbringing

    def skills(self,health, strength, attack, defense, magic):
        self.health=health
        self.strength=strength
        self.attack=attack
        self.defense=defense
        self.magic=magic

    def died(self):
        print(self.name.title() + " is dead!")
    
    def life(self):
        print(self.name.title() + " has come back to life!")
        



