import streamlit as st
import pandas as pd

st.set_page_config(page_title="About Me | Ajeet", page_icon="🏃")
st.title("Beyond Engineering")

st.write(
    "Outside of mechanical design and CFD, I focus on tracking performance metrics in physical training and sports.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("⚽ Soccer Analytics")
    st.write("I actively track match intensity and volume.")
    # Example metrics
    st.metric(label="Matches Played (This Season)", value="14")
    st.metric(label="Average Distance Covered", value="8.5 km")

with col2:
    st.subheader("🏋️ Strength & Conditioning")
    st.write("Monitoring 1RM progression and total weekly volume.")

    # Example data table for lifts
    data = pd.DataFrame({
        "Lift": ["Squat", "Bench", "Deadlift"],
        "Current 1RM (kg)": [140, 100, 160],
        "Goal (kg)": [160, 110, 180]
    })
    st.dataframe(data, hide_index=True)

st.divider()
st.subheader("Currently Reading / Studying")
st.markdown("""
* Advanced OpenFOAM meshing strategies
* Ghostty terminal configuration & environment optimization
""")