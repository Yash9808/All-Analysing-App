import streamlit as st

# Custom Page Configuration
st.set_page_config(page_title="Chartwell Data Analysis", page_icon="📊", layout="wide")

# Use the raw GitHub image URL for the background
background_image_url = "https://raw.githubusercontent.com/Yash9808/All-Analysing-App/main/pic1.JPG"

# Custom CSS to set the background image correctly and make buttons black
st.markdown(f"""
    <style>
        .stApp {{
            background: url("{background_image_url}") no-repeat center center fixed;
            background-size: cover;
        }}
        .title {{
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            color: white;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.7);
        }}
        .subtitle {{
            font-size: 1.5em;
            text-align: center;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
            margin-bottom: 20px;
        }}
        .button {{
            display: block;
            padding: 15px;
            margin: 10px auto;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            background-color: black;  /* 🖤 BLACK BUTTON */
            color: white;
            border-radius: 12px;
            text-decoration: none;
            width: 80%;
            transition: 0.3s;
        }}
        .button:hover {{
            background-color: #333;  /* Dark Gray on Hover */
        }}
        .footer {{
            text-align: center;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
            margin-top: 30px;
        }}
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<p class="title">📊 ALL APPS for Analysing Data - Chartwell Hospital</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Click below to open one of the apps:</p>', unsafe_allow_html=True)

# Create Columns for Buttons (Two per Row)
col1, col2 = st.columns(2)

# First App Button (Transcribe & Analyze)
with col1:
    st.markdown('<a class="button" href="https://yp2opqdw5du4x4cevfryet.streamlit.app/">🔊 Open Transcribe & Analyse</a>', unsafe_allow_html=True)

# Second App Button (Call Analysis V4)
with col2:
    st.markdown('<a class="button" href="https://a2rpeak3gt2tflgd4skjvv.streamlit.app/">📞 Open Call Analysis V4</a>', unsafe_allow_html=True)

# Second Row of Buttons
col3, col4 = st.columns(2)

# ML Analysis Button
with col3:
    st.markdown('<a class="button" href="https://n8uxyzcvs8b6inirclre8v.streamlit.app/">🧠 ML Analysis</a>', unsafe_allow_html=True)

# MRI Image and Report Analysis Button
#with col4:
    #st.markdown('<a class="button" href="https://xiurkqcwncuxtdt28yv9db.streamlit.app/">🧲🔍MRI Image & Report Analysis</a>', unsafe_allow_html=True)

# Third Row for the New 5th and 6th Buttons (next to each other)
col5, col6 = st.columns(2)  # Create two columns for buttons 5 and 6

# 5th Button: Advance ALL MRI
#with col5:
    #st.markdown('<a class="button" href="https://jp9zpznwvcgepujrtq2dwk.streamlit.app/">🧲 Advance ALL MRI</a>', unsafe_allow_html=True)

# 6th Button: TFP login and analysis
with col6:
    st.markdown('<a class="button" href="https://mqywxe55fiwrjmcrsy7fdh.streamlit.app/">🔐 FTP Login and Analysis</a>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<p class="footer"> Chartwell Hospital App Version 1 </p>', unsafe_allow_html=True)
