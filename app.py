from pathlib import Path
import streamlit as st
from PIL import Image
import base64

# --- DRACULA THEME COLORS ---
BG_COLOR = "#282a36"
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

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'data:application/octet-stream;base64,{bin_str}'

    # This is the HTML that mimics your skill tag style
    custom_css = f"""
        <a href="{href}" download="{Path(bin_file).name}" style="
            background-color: {CURRENT_LINE}; 
            color: {PURPLE}; 
            padding: 8px 15px; 
            text-decoration: none;
            border-radius: 5px; 
            border: 1px solid {PURPLE};
            display: inline-block;
            font-family: 'Meslo LG L', monospace;
            font-size: 14px;
            font-weight: bold;
            transition: 0.3s;
        " onmouseover="this.style.backgroundColor='#6272a4'; this.style.color='#ff79c6';" 
           onmouseout="this.style.backgroundColor='{CURRENT_LINE}'; this.style.color='{PURPLE}';">
            📄 Download Resume (PDF)
        </a>
    """
    return custom_css

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "AjeetKrishnasamyResumeEng.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"

# --- GENERAL SETTINGS ---

PAGE_TITLE = "Digital CV | Ajeet Krishnasamy"
PAGE_ICON = ":wave:"
NAME = "Ajeet Krishnasamy"
DESCRIPTION = """
Biomedical Mechanical Engineering Graduate
"""
EMAIL = "ajeetkrish@icloud.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ajeetkrishnasamy/",
    "GitHub": "https://github.com/ajeet-krish",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")
# --- LOAD CSS, PDF & PROFILE PIC ---
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# Use a placeholder if image is missing to prevent crash during development
try:
    profile_pic = Image.open(profile_pic)
except FileNotFoundError:
    profile_pic = None

# --- TOP NAVIGATION BREADCRUMB ---
st.markdown(f"""
    <div style="font-family: 'Meslo LG L', monospace; font-size: 12px; color: {COMMENT}; margin-bottom: 20px;">
        ~ / portfolio / <span style="color: {PURPLE};">ajeet_krishnasamy.py</span>
    </div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="medium")
with col1:
    if profile_pic:
        st.image(profile_pic, width=230)

with col2:
    # 1. Name and Title Section
    st.markdown(f"""
        <div style="font-family: 'Meslo LG L', 'JetBrains Mono', monospace;">
            <h1 style="color: {PURPLE}; margin-bottom: 0px; font-size: 32px;">{NAME}</h1>
            <p style="color: {FOREGROUND}; margin-top: 5px; font-size: 16px">
                Biomedical Mechanical Engineering Graduate
            </p>
            <p style="color: {FOREGROUND}; margin-top: 5px; font-size: 16px">
               Aerodynamics & CFD | Python
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 2. Metadata (Comment Style)
    st.markdown(f"""
        <div style="margin-top: 10px; margin-bottom: 20px; font-family: 'Meslo LG L', monospace; font-size: 13px; color: {COMMENT};">
            📍 Toronto, ON | 🌎 CAN & US Citizen | ✈️ Open to Relocation
        </div>
    """, unsafe_allow_html=True)

    # 3. Download Button
    # Assuming get_binary_file_downloader_html is defined in your script
    resume_button_html = get_binary_file_downloader_html(resume_file, 'Resume')
    st.markdown(resume_button_html, unsafe_allow_html=True)

    # 4. Standardized Social Links (CLI Style)
    # We style these like tags/arguments to match your skills section
    st.markdown(f"""
        <div style="margin-top: 20px; font-family: 'Meslo LG L', monospace; font-size: 14px;">
            <a href="mailto:{EMAIL}" style="color: {CYAN}; text-decoration: none;">{EMAIL}</a>
            <span style="color: {COMMENT};"> | </span>
            <a href="{SOCIAL_MEDIA['LinkedIn']}" style="color: {CYAN}; text-decoration: none;">LinkedIn</a>
            <span style="color: {COMMENT};"> | </span>
            <a href="{SOCIAL_MEDIA['GitHub']}" style="color: {CYAN}; text-decoration: none;">GitHub</a>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# --- WORK HISTORY ---
st.write("\n")
st.markdown(f"### <span style='color: {PURPLE};'># Experience</span>", unsafe_allow_html=True)

def work_block(title, date, location, details):
    st.markdown(f"""
        <div style="
            background-color: #21222c; 
            border-left: 4px solid {PURPLE}; 
            padding: 20px; 
            margin-bottom: 25px; 
            font-family: 'Meslo LG L', monospace;
            border-radius: 0 8px 8px 0;
        ">
            <div style="color: {CYAN}; font-weight: bold; font-size: 16px;">{title}</div>
            <div style="color: {COMMENT}; font-size: 12px; margin-bottom: 10px;"> {date} | {location}</div>
            <div style="color: {FOREGROUND}; font-size: 13px; line-height: 1.6;">
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
        f'<span style="background-color: {CURRENT_LINE}; color: {cat_color}; padding: 2px 8px; margin: 2px; border-radius: 4px; border: 1px solid {cat_color}; font-size: 11px; white-space: nowrap;">{item}</span>'
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