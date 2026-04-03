from pathlib import Path
import streamlit as st

# --- 1. SET PAGE CONFIG ---
st.set_page_config(page_title="Projects | Ajeet Krishnasamy", page_icon="🚀", layout="wide")

# --- 2. PATH SETTINGS & CSS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"

# --- VISUAL SETUP ---
# Dracula Theme Colours
BACKGROUND = "#282a36"
CURRENT_LINE = "#44475a"
SELECTION = "#44475a"
FOREGROUND = "#f8f8f2"
COMMENT = "#6272a4"
CYAN = "#8be9fd"
GREEN = "#50fa7b"
ORANGE = "#ffb86c"
PINK = "#ff79c6"
PURPLE = "#bd93f9"
RED = "#ff5544"
YELLOW = "#f1fa8c"

# Load external css file
def local_css(file_path):
    if file_path.exists():
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css(css_file)

# --- 4. TOP NAVIGATION BREADCRUMB ---
st.markdown(f"""
    <div style="font-family: 'Meslo LG L', monospace; font-size: 12px; color: {COMMENT}; margin-bottom: 20px;">
        ~ / portfolio / <span style="color: {PINK};">projects.py</span>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"<h1 style='color: {PURPLE}; margin-top: 0;'>Engineering Projects</h1>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# PROJECT 1: AIRFOIL-TO-CFD TOOL
# ==========================================
with st.container():
    st.markdown(f"""
        <div style="background-color: #21222c; border-left: 4px solid {CYAN}; padding: 20px; border-radius: 0 8px 8px 0; margin-bottom: 15px;">
            <div style="color: {CYAN}; font-weight: bold; font-size: 18px;">>_ Automated Airfoil-to-CFD Tool</div>
            <div style="margin-top: 8px;">
                <a href="https://github.com/ajeet-krish/Airfoil-CFD-Automation" style="color: {PURPLE}; text-decoration: none; font-size: 14px;">[ View Source Code on GitHub ]</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Overview", "Media & Workflow", "Simulation Results"])

    with tab1:
        st.write("""
            Developed an automated pipeline in **Python** to synchronize coordinates from `.dat` airfoil files into 
            **OpenFOAM**-ready 3D geometries. This tool standardizes directory structures and automates 
            the `blockMesh` and `snappyHexMesh` generation, reducing setup time for iterative aerodynamic studies by ~80%.
        """)
        st.markdown(f"**Key Features:**")
        st.write("- Automated AoA (Angle of Attack) sweeping.")
        st.write("- Standardized $k-\omega$ SST turbulence modeling setup.")

    with tab2:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.image("assets/mesh_preview.png", caption="Automated SnappyHexMesh refinement layers")
        with col_txt:
            st.markdown(f"<span style='color: {CYAN};'># Geometry & Meshing</span>", unsafe_allow_html=True)
            st.write("""
                The tool utilizes a custom coordinate-transformation script to map 2D profiles into 3D space. 
                The mesh is refined at the leading and trailing edges to accurately capture the stagnation point 
                and wake turbulence.
            """)

        st.divider()
        st.image("assets/gui_demo.png", caption="CLI/GUI Interface for parameter input")

    with tab3:
        st.markdown(f"<span style='color: {GREEN};'># Performance Metrics</span>", unsafe_allow_html=True)
        st.write("Validation of lift ($C_l$) and drag ($C_d$) coefficients against experimental NACA data.")

        # Placeholder for your interactive Plotly or Streamlit charts
        # example: st.line_chart(df, x="AoA", y=["Cl", "Cd"])
        st.info("Interactive Plotly charts showing Polar Curves (Cl vs Cd) will be rendered here.")

        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Max L/D Ratio", "24.2", "+2.1")
        col_m2.metric("Stall Angle", "16°", "NACA 0012")
        col_m3.metric("Converged Iterations", "~1200")

st.divider()

# ==========================================
# PROJECT 2: HYDRAULIC TURBINE
# ==========================================
with st.container():
    # Styled Terminal Header
    st.markdown(f"""
        <div style="background-color: #21222c; border-left: 4px solid {GREEN}; padding: 20px; border-radius: 0 8px 8px 0; margin-bottom: 15px;">
            <div style="color: {GREEN}; font-weight: bold; font-size: 18px;">>_ Hydraulic Turbine Performance Analysis</div>
            <div style="color: {COMMENT}; font-size: 13px; margin-top: 8px;">Experimental Fluid Dynamics | April 2026</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(
        r"Experimental evaluation of operational limits. Monitored mechanical torque ($T$) and rotational speed ($N$) to calculate overall efficiency.")

    # Placeholder block for future data visualization
    st.code("""
# TODO: Import pd.DataFrame and render st.line_chart()
# X-axis: Rotational Speed (N)
# Y-axis: Efficiency (%)
    """, language="python")