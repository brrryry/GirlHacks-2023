import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import json

from random import random
from threading import Timer
import time

import streamlit as st
import math
import pandas as pd

from modules import moon, planet, graphics

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
        if "planet" not in st.session_state or st.session_state["planet"] == None: #if planet does not exist
            st.markdown("ERROR: Planet does not exist yet. Please return to the home page to create your planet!")
        else:
            userPlanet = st.session_state["planet"]

            #increment age by time
            currentTime = time.time()
            userPlanet.incrementAge(currentTime - st.session_state["time"])
            st.session_state["time"] = currentTime

            st.title(f'Planet {userPlanet.getName()} - Statistics')
            
            st.metric("Name", userPlanet.getName())
            st.metric("Color", userPlanet.getColor())
            st.metric("Age", f'{userPlanet.getAge()} years')
            st.metric("Size", f'{"{:e}".format(int(4/3 * (userPlanet.getSize() * 1e3) ** 3 * math.pi * 100) / 100)} km^3')
            st.metric("Mass", f'{int(userPlanet.getMass() * 1e24 * 100) / 100} kg')

            elementNames = ["Hydrogen", "Carbon", "Oxygen", "Sodium", "Sulfur", "Potassium", "Nickel", "Iron"]
            elements = userPlanet.getElements()[1:]
            for i in range(len(elements)):
                st.metric(f'{elementNames[i]} Units: ', elements[i])
            
            st.metric("Asteroid Count", len(userPlanet.getAsteroids()))
            st.metric("Total Asteroid Mass", sum(userPlanet.getAsteroids()))
            st.metric("Star count", 100)

            moons = userPlanet.getMoons()
            st.metric("Moons", len(moons))

            if len(moons) > 0:
                df = pd.DataFrame(columns=["Name", "Color", "Size", "Mass", "Distance from Planet"])
                for moon in moons:
                    df.loc[len(df.index)] = [moon.getName(), 
                    moon.getColor(), 
                    f'{"{:e}".format(int(4/3 * (moon.getSize() * 1e3) ** 3 * math.pi * 100) / 100)} km^3', 
                    f'{int(moon.getMass() * 1e24 * 100) / 100} kg', 
                    f'{moon.getDistance() * 1e6} km']
                st.dataframe(df)

            
            
if __name__ == "__main__":
    page = main()
    page.run()
