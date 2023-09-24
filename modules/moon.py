import random

firstWord = ["Big", "Goofy", "Tiny", "Stinky", "Bossy", "Dapper", "Massive", "Short", "Deadly", "Evil"]
secondWord = ["Thing", "Cow", "Father", "Fish", "Kitten", "Ball","Cupcake", "Rainbow", "Hotdog"]

def generateName():
    return f'{random.choice(firstWord)} {random.choice(secondWord)}'

class Moon:
    def __init__(self, relativeplanet, distance, angle, speed, mass, size, color):
        self.distance = distance + relativeplanet.getSize()
        self.speed = speed
        self.mass = mass
        self.size = size
        self.angle = angle
        self.color = color
        self.name = generateName()
    
    def getName(self): return self.name
    def getColor(self): return self.color
    def getDistance(self): return self.distance
    def getSpeed(self): return self.speed
    def getMass(self): return self.mass
    def getSize(self): return self.size
    def getAngle(self): return self.angle


        
    
    
