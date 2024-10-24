import random
class character(object):
    def __init__(self, name = "anonymous", hitPoints = 10, hitChance = 50, maxDamage = 5, armor = 2):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
        
    
    @property
    def hitPoints(self):
        return self.__hitPoints   
    @hitPoints.setter
    def hitPoints(self, value):
        self.__hitPoints = self.testInt(value, -100000, 100000, 10)
        
        
    @property
    def hitChance(self):
        return self.__hitChance
    @hitChance.setter
    def hitChance(self, value):
        self.__hitChance = self.testInt(value, 0, 100, 50)
        

    @property
    def maxDamage(self):
        return self.__maxDamage
    @maxDamage.setter
    def maxDamage(self, value):
        self.__maxDamage = self.testInt(value, 0, 100000, 5)
    
    @property
    def armor(self):
        return self.__armor
    @armor.setter
    def armor(self, value):
        self.__armor = self.testInt(value, 0, 100000, 2)
    
    def printStats(self):
        print(f"{self.name}")
        print("==================")
        print(f"Hit Points: {self.hitPoints}")
        print(f"Hit Chance: {self.hitChance}")
        print(f"Max Damage: {self.maxDamage}")
        print(f"armor: {self.armor}")
        print()
        
    def testInt(self, value, min = 0, max = 100, default = 0):
        out = default
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")

        return out
    
    def hit(self, opponent):
        rand = random.randint(1, 100)
        
        if rand <= self.hitChance:
            damage = random.randint(1, self.maxDamage)
            netDamage = damage - opponent.armor
            if netDamage < 0:  
                netDamage = 0
            opponent.hitPoints = opponent.hitPoints - netDamage
            print(f"{self.name} hits {opponent.name}...\n   for {damage} points of damage")
            print(f"   {opponent.name}'s armor absorbs {opponent.armor} points")
            
            
        
        
    
def fight(c1,c2):
    keepGoing = True
        
    while keepGoing:
        if input("\npress <ENTER> for a round:") != "":
            keepGoing = False
        c1.hit(c2)
        if c2.hitPoints <= 0:
            print(f"{c2.name} has been defeated")
            keepGoing = False 
        
        c2.hit(c1)  
        if c1.hitPoints <= 0:
            print(f"{c1.name} has been defeated!")
            keepGoing = False
        print(f"{c1.name}: {c1.hitPoints} HP")
        print(f"{c2.name}: {c2.hitPoints} HP")
            

                         
        
def main():
    c1 = character("All Powerfull Being", 1000, 100, 100, 100)
    c2 = character("lucas", 1, 1, 1, 1)
    
    c1.printStats()    
    c2.printStats()
    
    fight(c1,c2)
    
    
    
   
    
    
    
if __name__ == "__main__":
    main()



    
    
    
    
    