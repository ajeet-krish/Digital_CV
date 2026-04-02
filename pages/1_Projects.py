import streamlit as st

st.set_page_config(page_title="Projects | Ajeet Krishnasamy", page_icon="🚀", layout="wide")
st.title("Engineering Projects")

# Project 1 Container
with st.container():
    st.subheader("🏆 Automated Airfoil-to-CFD Tool")
    st.write("[View Source Code on GitHub](https://github.com/ajeet-krish/Airfoil-CFD-Automation)")

    tab1, tab2, tab3 = st.tabs(["Overview", "Methodology", "Code Snippet"])

    with tab1:
        st.write("An automated pipeline to synchronize geometry and generate 3D wings for computational analysis.")
        # st.image("assets/cfd_render.png", caption="Pressure contour of airfoil")

    with tab2:
        st.markdown("### Simulation Parameters")
        st.write(
            "Utilized the $k-\omega$ SST turbulence model to accurately capture boundary layer separation. The continuity equation solved is:")
        st.latex(r"\nabla \cdot (\rho \mathbf{u}) = 0")

    with tab3:
        st.code("""
# Example geometry generation logic
def generate_mesh(airfoil_dat, angle_of_attack):
    # Synchronizes points and scales for blockMesh dict
    pass
        """, language="python")

st.divider()

# Project 2 Container
with st.container():
    st.subheader("🏆 Hydraulic Turbine Performance Analysis")
    st.write(
        "Experimental evaluation of operational limits. Monitored mechanical torque ($T$) and rotational speed ($N$) to calculate overall efficiency.")
    # Add a st.line_chart() here later to show efficiency curves