import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Travel Map | Ajeet Krishnasamy", page_icon="🌍")
st.title("Travel Map")
st.write("An interactive map of places I've visited.")

# Center map (Example: Ottawa)
m = folium.Map(location=[45.4215, -75.6972], zoom_start=3)

# Add a marker (Example location)
folium.Marker(
    [45.4215, -75.6972],
    popup="Ottawa, ON",
    tooltip="Click for info"
).add_to(m)

# Add more markers as needed
# folium.Marker([lat, lon], popup="Location Name").add_to(m)

st_folium(m, width=700, height=500)