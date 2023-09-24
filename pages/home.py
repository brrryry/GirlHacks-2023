import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from random import random
from threading import Timer

import streamlit as st
import time

from modules import moon, planet, graphics

elementMap = {
    "Hydrogen": 1,
    "Oxygen": 2,
    "Carbon": 3,
    "Iron": 4,
    "Nickel": 5,
    "Sulfur": 6,
    "Sodium": 7,
    "Potassium": 8
}

#helper functions
def setInterval(timer, func):
    isStop = func()
    if not isStop:
        Timer(timer, setInterval, [timer, func]).start()

#booooooo
class main:
    def __init__(self):
        if "time" not in st.session_state:
            st.session_state["time"] = time.time()

    def run(self):
        st.sidebar.image("tiny_worlds.png", use_column_width=True)
        if "planet" not in st.session_state or st.session_state["planet"] == None:
            st.markdown("ERROR: Planet does not exist yet. Please return to the home page to create your planet!")
        else:
            userPlanet = st.session_state["planet"]
            st.title(f'Planet {userPlanet.getName()}')
            graphics.draw_planet(userPlanet)

            #increment age by time
            currentTime = time.time()
            userPlanet.incrementAge(currentTime - st.session_state["time"])
            st.session_state["time"] = currentTime
            
            elementOptions = st.selectbox("Select Element to Feed Planet: ", 
                ("Hydrogen", "Oxygen", "Carbon", "Iron", "Nickel", "Sulfur", "Sodium", "Potassium"),
                index=None)
            
            if st.button("Feed This Element!", type="secondary"):
                if "planet" not in st.session_state or st.session_state["planet"] == None:
                    st.error("Planet no longer exists.")
                elif elementOptions == None:
                    st.warning("You didn't choose an element! Pick and try again.")
                else:
                    userPlanet.feed(elementMap[elementOptions])
                    st.toast(f'You fed your planet {elementOptions}!')
                    if(userPlanet.isHabitable()):
                        st.toast(f'Congratulations! You now have life!')                
            
            if(st.button("Spawn Asteroid", type="primary")):
                if "planet" not in st.session_state or st.session_state["planet"] == None:
                    st.error("Planet no longer exists.")
                else: userPlanet.spawnAsteroid(random() * userPlanet.getMass() * 1.05)

            if(st.button("Refresh", type="primary")):
                pass

if __name__ == "__main__":
    page = main()
    page.run()