from random import random
import time
import streamlit as st

class Planet:
    def __init__(self, name, color, size, mass, distance = 5):
        self.name = name
        self.color = color
        self.size = size
        self.mass = mass
        self.distance = distance #distance from the sun
        self.age = 0
        self.elements = [0 for i in range(20)] #list containing quantity of elements [hydrogen, carbon, oxygen, sodium, sulfur, potassium, nickel, iron]
        self.astroids = []
        self.moons = []
        self.rings = []

    #getters and setters
    def setAge(self, age): self.age = age
    def setName(self, name): self.name = name
    def setDistance(self, distance): self.distance = distance
    def getDistance(self): return self.distance
    def getAge(self): return self.age
    def getElements(self): return self.elements
    def getAstroids(self): return self.astroids
    def getMoons(self): return self.moons
    def getRings(self): return self.rings
    def getName(self): return self.name
    def getSize(self): return self.size
    def getColor(self): return self.color

    def age():
        age = 0
        while True:
            age += 100
            print(age)
            time.sleep(1)
 
    def die():
        """
        Planet go bye bye
        """
        dieAge = 100000000 #big number
        bigAstroid = 10000 #also big
        if self.age >= dieAge:
            #die
            #die
            pass
        else:
            pass
    
    def feed(self, element):
        """
        Planet nom nom some element
        Earth (life): Hydrogen, Oxygen, Carbon
        Mars: iron, nickle, sulfur
        Mercury: sodium, sulfur, potassium
        """
        self.elements[element] += 1
        
    def spawnAsteroid(self, mass):
        """ creates moon or destroys planet """
        astroids += [mass]
        if mass > self.getMass(): #some arbitrary number, will change later
            self.die()
            st.info("The asteroid destroyed your planet!", icon="😢")
        elif (random() * 10 > 7): #20% for asteroid
            self.spawnMoon(moon.Moon(random() * 7 + 1, random() * 360, sum(self.astroids), 10000, 0x000000))
        elif(random() * 10 > 9): #5% for rings
            self.spawnRing 
            st.info("The asteroid created rings!", icon="🪐")
            

    def spawnMoon(self, moon):
        self.moons += [moon]

    def spawnRing(self, ring):
        self.ring += [ring]
        
    def isHabitable(self):
        return (self.elements[0] > 0 and self.elements[1] > 0) and self.elements[2] > 0

    