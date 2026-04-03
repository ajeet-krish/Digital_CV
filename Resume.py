from pathlib import Path
import streamlit as st
from PIL import Image
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Digital CV | Ajeet Krishnasamy", page_icon=":wave:", layout="wide")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "AjeetKrishnasamyResumeEng.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"

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

# Resume Download Button Function
def get_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'data:application/octet-stream;base64,{bin_str}'
    return f'<a href="{href}" download="{Path(bin_file).name}" class="download-btn">{file_label}</a>'

# Use a placeholder if image is missing to prevent crash during development
try:
    profile_pic = Image.open(profile_pic)
except Exception:
    profile_pic = None

# --- GENERAL SETTINGS ---
NAME = "Ajeet Krishnasamy"
EMAIL = "ajeetkrish@icloud.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ajeetkrishnasamy/",
    "GitHub": "https://github.com/ajeet-krish",
}

# --- TOP NAVIGATION BREADCRUMB ---
st.markdown(f"""
    <div style="font-family: 'Meslo LG L', monospace; font-size: 12px; color: {COMMENT}; margin-bottom: 20px;">
        ~ / portfolio / <span style="color: {PINK};">ajeet_krishnasamy.py</span>
    </div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="large")
with col1:
    if profile_pic:
        st.image(profile_pic, width=400)

with col2:
    # --- NAME & INTRO ---
    st.markdown(f"""
        <h1 style="color: {PURPLE}; font-size: 36px; text-align: center; margin-top: 0; margin-bottom: 0px;">
            {NAME}
        </h1>
        <div style="line-height: 1.6; font-size: 16px; margin-bottom: 10px;">
            I am a <span style="color: {ORANGE};">Biomedical Mechanical Engineering</span> graduate 
            specializing in <span style="color: {CYAN};">aerodynamics</span> and 
            <span style="color: {CYAN};">CFD</span> for the aerospace and automotive sectors. 
            I leverage <span style="color: {CYAN};">Python</span> and 
            <span style="color: {CYAN};">MATLAB</span> to automate high-fidelity simulations in 
            <span style="color: {CYAN};">OpenFOAM</span>, bridging the gap between conceptual 
            <span style="color: {ORANGE};">CAD</span> design and physical validation. 
            This portfolio showcases my work in fluid dynamics, structural modeling, 
            and data analysis.
        </div>
    """, unsafe_allow_html=True)

    # Metadata
    st.markdown(f"""
        <div style="
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            gap: 15px;
            font-family: 'Meslo LG L', monospace; 
            font-size: 16px;
            margin-top: 10px;
        ">
            <div>
                <span style="color: {ORANGE};">Toronto, ON</span>
                <span style="color: {COMMENT};">|</span>
                <span style="color: {ORANGE};">CAN & US Citizen</span>
                <span style="color: {COMMENT};">|</span>
                <span style="color: {ORANGE};">Open to Relocation</span> 
            </div>
        </div>
    """, unsafe_allow_html=True)


resume_button_html = get_file_downloader_html(resume_file, 'Resume.pdf')

# Flex Row
st.markdown(f"""
    <div style="
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 15px;
        font-family: 'Meslo LG L', monospace; 
        font-size: 16px;
        margin-top: 10px;
    ">
        {resume_button_html}
        <span style="color: {COMMENT};">|</span>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <span style="color: {COMMENT};">|</span>
        <a href="{SOCIAL_MEDIA['LinkedIn']}">LinkedIn</a>
        <span style="color: {COMMENT};">|</span>
        <a href="{SOCIAL_MEDIA['GitHub']}">GitHub</a>
    </div>
""", unsafe_allow_html=True)

st.divider()

# --- WORK HISTORY ---
st.markdown(f"### <span style='color: {PURPLE};'># Experience</span>", unsafe_allow_html=True)

def work_block(title, date, location, details):
    st.markdown(f"""
        <div style="
            background-color: #21222c; 
            border-left: 4px solid {PURPLE}; 
            padding: 20px; 
            margin-bottom: 15px; 
            font-family: 'Meslo LG L', monospace;
            border-radius: 0 8px 8px 0;
        ">
            <div style="color: {CYAN}; font-weight: bold; font-size: 16px;">{title}</div>
            <div style="color: {COMMENT}; font-size: 13px; margin-bottom: 10px;"> {date} | {location}</div>
            <div style="color: {FOREGROUND}; font-size: 14px; line-height: 1.6;">
                {details}
            </div>
        </div>
    """, unsafe_allow_html=True)

# Job 1
work_block(
    "Systems Engineer (Intern) | CenTrak",
    "10/2020 - 09/2021",
    "Newtown, PA, United States",
    "• Developed statistical models (R, Excel) to assess medical device reliability.<br>"
    ". Automated performance reporting for Connect Pulse™ to minimize system downtime.<br>"
    "• Analyzed battery and device datasets to predict and prevent hardware failures.<br>"
    "• Structured and cleaned large-scale RTLS data to accelerate troubleshooting."
)

# Job 2
work_block(
    "Systems Engineer (Intern) | CenTrak",
    "05/2019 - 09/2019",
    "Newtown, PA, United States",
    "• Applied regression and classification models to optimize RTLS location accuracy.<br>"
    "• Executed on-site testing protocols to validate hardware field performance.<br>"
    "• Synthesized technical data into actionable recommendations for system upgrades."
)

# --- SKILLS SECTION ---
st.write("\n")
st.markdown(f"### <span style='color: {ORANGE};'># Skills</span>", unsafe_allow_html=True)

skill_categories = {
    "CAD": {"items": ["SolidWorks", "FreeCAD", "Fusion 360"], "color": CYAN},
    "CFD": {"items": ["Ansys CFX", "OpenFOAM"], "color": GREEN},
    "Data Analysis": {"items": ["Python", "MATLAB"], "color": ORANGE},
    "Manufacturing": {"items": ["CNC Machining", "3D Printing", "Lathe & Mill", "MIG Welding"], "color": PINK}
}

# Building the internal HTML
skills_inner_html = ""
for category, data in skill_categories.items():
    cat_color = data["color"]
    items = data["items"]

    # Category Key in its specific color
    skills_inner_html += f'&nbsp;&nbsp;&nbsp;&nbsp;"<span>{category}</span>": ['

    # Tags using the category-specific color for the border and text
    tags = "".join([
        f'<span style="background-color: {CURRENT_LINE}; color: {cat_color}; padding: 2px 8px; margin: 2px; border-radius: 4px; border: 1px solid {cat_color}; font-size: 13px; white-space: nowrap;">{item}</span>'
        for item in items
    ])

    skills_inner_html += f'{tags}],<br>'

# Block Style
st.markdown(f"""
    <div style="
        background-color: #21222c; 
        border-left: 4px solid {ORANGE}; 
        padding: 20px; 
        margin-bottom: 25px; 
        font-family: 'Meslo LG L', monospace;
        border-radius: 0 8px 8px 0;
    ">
        <div style="color: {CYAN}; font-weight: bold; font-size: 16px; margin-bottom: 10px; ">Hardware & Software Proficiencies</div>
        <div style="color: {FOREGROUND}; font-size: 14px; line-height: 1.6;">
            <span style="color: {PURPLE};">return</span> {{<br>
            {skills_inner_html}
            }}
        </div>
    </div>
""", unsafe_allow_html=True)

# --- EDUCATION SECTION ---
st.write("\n")
st.markdown(f"### <span style='color: {PINK};'># Education</span>", unsafe_allow_html=True)

# Block Style
st.markdown(f"""
    <div style="
        background-color: #21222c; 
        border-left: 4px solid {PINK}; 
        padding: 20px; 
        margin-bottom: 25px; 
        font-family: 'Meslo LG L', monospace;
        border-radius: 0 8px 8px 0;
    ">
        <div style="color: {CYAN}; font-weight: bold; font-size: 16px;">University of Ottawa</div>
        <div style="color: {COMMENT}; font-size: 12px; margin-bottom: 10px;">Ottawa, ON, Canada | May 2026</div>
        <div style="color: {FOREGROUND}; font-size: 14px; line-height: 1.6;">
            <span style="color: {PURPLE};">return</span> {{<br>
            &nbsp;&nbsp;&nbsp;&nbsp;"degree": "Bachelor of Applied Science (BASc)",<br>
            &nbsp;&nbsp;&nbsp;&nbsp;"major": "Biomedical Mechanical Engineering"<br>
            }}
        </div>
    </div>
""", unsafe_allow_html=True)