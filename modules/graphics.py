import streamlit as st
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import math
import random

numDots = 100
dots_x = np.random.rand(numDots)
dots_y = np.random.rand(numDots)

def draw_planet(planet):
    #Create a figure and axis for the circle planet
    fig, ax = plt.subplots(figsize=(25, 25))
    ax.set_aspect('equal')
    ax.set_axis_off()
    plt.rcParams['savefig.facecolor'] = '#021024'

    #Draw the circle planet with the chosen color
    hatch_pattern = planet.getPattern()

    planet_to_draw = Circle((0.5, 0.5), planet.getSize(), color=planet.getColor(), ec='black', lw=1, hatch=hatch_pattern)

    # creates random stars
    dotSizes =  planet.getSize() * 0.01   
    

    for moon in planet.getMoons():
        moon_to_draw = Circle((0.5 + moon.getDistance() * math.cos(moon.getAngle() * math.pi / 180), 0.5 + moon.getSize() + moon.getDistance() * math.sin(moon.getAngle() * math.pi / 180)), moon.getSize(),  color="#" + ("0" * (6 - len(moon.getColor()[2:]))) + moon.getColor()[2:], ec='black', lw=1)
        ax.add_patch(moon_to_draw)

    for i in range(numDots):
            dots_x[i] += random.uniform(-0.001, 0.001) 
            dots_y[i] += random.uniform(-0.001, 0.001) 
            dot = plt.Circle((dots_x[i], dots_y[i]), dotSizes, color="#e6eff0")
            ax.add_patch(dot)

    ax.add_patch(planet_to_draw)


    # Display the planet in Streamlit
    st.pyplot(fig)  