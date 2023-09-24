import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

import streamlit as st
from modules import moon, planet, graphics

#booooooo
class main:
    def __init__(self):
        if "time" not in st.session_state:
            st.session_state["time"] = time.time()

    def run(self):
        st.title("Your Planet")
        st.sidebar.image("tiny_worlds.png", use_column_width=True)
        planetName = st.text_input("Planet Name", type='default')
        planetSize = st.slider("Planet Size (km * 10^4)", min_value=1, max_value=10)
        planetMass = st.slider("Planet Mass (kg * 10^24)", min_value=1, max_value=5000)
        planetColor = st.color_picker('Pick A Color', '#f6fcdc')

        if st.button("Submit!", type="primary"): 
            if len(planetName) < 5:
                st.warning('Name should be at least 5 characters long!', icon='⚠')
            else:
                userPlanet = planet.Planet(planetName, planetColor, planetSize / 30, planetMass)
                st.session_state["planet"] = userPlanet
                st.success(f'Planet \"{planetName}\" successfully created!')
                self.astroids = []

if __name__ == "__main__":
    page = main()
    page.run()
