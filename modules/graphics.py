import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import math
import pyvista as pv
from stpyvista import stpyvista

def draw_planet(planet):
   ''' #Create a figure and axis for the circle planet
    fig, ax = plt.subplots(figsize=(11, 11))
    ax.set_aspect('equal')
    ax.set_axis_off()

    #Draw the circle planet with the chosen color
    planet_to_draw = Circle((0.5, 0.5), planet.getSize() / 20, color=planet.getColor(), ec='black', lw=1)

    for moon in planet.getMoons():
        moon_to_draw = Circle((0.5 + moon.getDistance() * math.cos(moon.getAngle() * math.pi / 180), 0.5 + moon.getDistance() * math.sin(moon.getAngle() * math.pi / 180)), moon.getSize() / 20,  color='grey' , ec='black', lw=1)
        ax.add_patch(moon_to_draw)
        st.toast('You created a moon', icon='🌙')


    ax.add_patch(planet_to_draw)

    # Display the planet in Streamlit
    st.pyplot(fig)  '''

# Set up plotter
plotter = pv.Plotter(window_size=[300, 300])

# Create element
sphere = pv.Sphere(phi_resolution=res, theta_resolution=res)
plotter.add_mesh(sphere, name="sphere", show_edges=True)

plotter.view_isometric()
plotter.set_background("white")

# Pass the plotter (not the mesh) to stpyvista
stpyvista(plotter)




