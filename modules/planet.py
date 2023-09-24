import random
import time
import streamlit as st
from PIL import Image, ImageDraw

from modules import graphics, moon

class Planet:
    def __init__(self, name, color, size, mass, distance = 5):
        self.name = name
        self.color = color
        self.size = size
        self.mass = mass
        self.distance = distance #distance from the sun
        self.age = 0
        self.elements = [0 for i in range(9)] #list containing quantity of elements [None, hydrogen, carbon, oxygen, sodium, sulfur, potassium, nickel, iron]
        self.asteroids = []
        self.moons = []
        self.rings = []
        self.pattern = random.choice([ "/" , "\\" , "|" , "-",])

    #getters and setters
    def setColor(self, color): self.color = color
    def setAge(self, age): self.age = age
    def setName(self, name): self.name = name
    def setDistance(self, distance): self.distance = distance
    def getDistance(self): return self.distance
    def getAge(self): return self.age
    def getElements(self): return self.elements
    def getAsteroids(self): return self.asteroids
    def getMoons(self): return self.moons
    def getRings(self): return self.rings
    def getName(self): return self.name
    def getSize(self): return self.size
    def getColor(self): return self.color
    def getMass(self): return self.mass
    def getPattern(self): return self.pattern

    startTime = time.time()

    def incrementAge(self, delta):
        self.age += round((random.random() * 1000 + 1000) * delta)
        return
 
    def die(self):
        """
        Planet go bye bye
        """
        self.name = ""
        self.color = 0
        self.size = 0
        self.mass = 0
        self.distance = 0 
        self.age = 0
        self.elements = [0 for i in range(20)] #list containing quantity of elements [None, hydrogen, carbon, oxygen, sodium, sulfur, potassium, nickel, iron]
        self.asteroids = []
        self.moons = []
        self.rings = []
        self.pattern = None
        st.session_state["planet"] = None
        st.session_state.pop("time")
    
    def feed(self, element):
        """
        Planet nom nom some element
        Earth (life): Hydrogen, Oxygenself.die(), Carbon
        Mars: iron, nickle, sulfur
        Mercury: sodium, sulfur, potassium
        """

        self.elements[element] += 1
        
        #list containing quantity of elements [None, hydrogen, carbon, oxygen, sodium, sulfur, potassium, nickel, iron]

        if self.elements[1] > 0 and self.elements[2] > 0 and self.elements[3] > 0:
            isHabitable = True
            st.info ("Theres life on your planet now!", icon="🌱")
            self.setColor("#34A56F")
        if self.elements[4] > 0 and self.elements[3] > 0 and self.elements[4] > 0:
            isHabitable = False
            st.info ("You have a rocky planet!", icon="🪨")
            self.setColor("#80461B")
        if self.elements[6] > 0 and self.elements[7] > 0 and self.elements[8] > 0:
            isHabitable = False
            st.info ("You have an icy planet!", icon="🧊")
            self.setColor("#94e7f2")

    def spawnAsteroid(self, mass): 
        """ creates moon or destroys planet """
        self.asteroids += [mass]
        if mass > self.getMass(): #some arbitrary number, will change later
            st.info("The asteroid destroyed your planet!", icon="😢")
            self.die()
        elif (random.random() * 10 > 7): #20% for asteroid
            redVal = random.random()
            greenVal = random.random()
            blueVal = random.random()
            self.spawnMoon(moon.Moon(self, random.random() * 0.5, round(random.random() * 360), 50, sum(self.asteroids), min(random.random() + 0.25, 0.7) * self.getSize(), str(hex(int(random.random() * 0xFFFFFF)))))
            st.info('The stars have aligned. You created a moon!', icon='🌙')
            random.seed(redVal * 2)
        else:
            st.info('An asteroid hits the earth. Nothing major happens.')
            

    def spawnMoon(self, moon):
        self.moons += [moon]

    def spawnRing(self, ring):
        self.ring += [ring]
        
    def isHabitable(self):
        return (self.elements[0] > 0 and self.elements[1] > 0) and self.elements[2] > 0