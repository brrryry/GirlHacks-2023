import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from random import random

import streamlit as st

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

#booooooo
class main:
    def __init__(self):
        pass

    def run(self):

        if "planet" not in st.session_state:
            st.markdown("ERROR: Planet does not exist yet. Please return to the home page to create your planet!")
        else:
            userPlanet = st.session_state["planet"]
            st.title(f'Planet {userPlanet.getName()}')
            graphics.draw_planet(userPlanet)

            
            
            elementOptions = st.selectbox("Select Element to Feed Planet: ", 
                ("Hydrogen", "Oxygen", "Carbon", "Iron", "Nickel", "Sulfur", "Sodium", "Potassium"),
                index=None)
            
            if st.button("Feed This Element!", type="secondary"):
                if elementOptions == None:
                    st.warning("You didn't choose an element! Pick and try again.")
                else:
                    userPlanet.feed(elementMap[elementOptions])
                    st.toast(f'You fed your planet {elementOptions}!')
                    if(userPlanet.isHabitable()):
                        st.toast(f'Congratulations! You now have life!')
                
                
                
            
            if(st.button("Spawn Asteroid", type="primary")):
                userPlanet.spawnAsteroid()

            if(st.button("Status", type="primary")):
                pass
            
            

if __name__ == "__main__":
    page = main()
    page.run()
