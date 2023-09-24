import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pyvista as pv
from stpyvista import stpyvista

import streamlit as st
from modules import moon, planet, graphics

#booooooo
class main:
    def __init__(self):
        pass

    def run(self):
        st.title("Your Planet")
        planetName = st.text_input("Planet Name", type='default')
        planetSize = st.slider("Planet Size (miles * 10^5)", min_value=1, max_value=10)
        planetMass = st.slider("Planet Mass (kg * 10^24)", min_value=1, max_value=5000)
        planetColor = st.color_picker('Pick A Color', '#000000')
            

        if st.button("Submit!", type="primary"):
            if len(planetName) < 5:
                st.warning('Name should be at least 5 characters long!', icon='⚠')
            else:
                userPlanet = planet.Planet(planetName, planetColor, planetSize, planetMass)
                userPlanet.spawnMoon(moon.Moon(0.25, 90, 50, 500, 0.4, 0x000000))
                st.session_state["planet"] = userPlanet
                st.success(f'Planet \"{planetName}\" successfully created!')
            
            

if __name__ == "__main__":
    page = main()
    page.run()
