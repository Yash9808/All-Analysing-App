import streamlit as st

# Custom Page Configuration
st.set_page_config(page_title="Chartwell Data Analysis", page_icon="📊", layout="wide")

# Background GIF URL (Using the RAW GitHub Link)
background_gif_url = "https://raw.githubusercontent.com/Yash9808/All-Analysing-App/main/pic1.JPG"

# Custom CSS for setting the GIF as a background
st.markdown(f"""
    <style>
        body {{
            background: url('{background_gif_url}') no-repeat center center fixed;
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
            width: 100%;
            display: inline-block;
            padding: 15px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            background-color: rgba(0, 102, 204, 0.8);
            color: white;
            border-radius: 12px;
            text-decoration: none;
            transition: 0.3s;
        }}
        .button:hover {{
            background-color: rgba(0, 82, 164, 0.9);
        }}
        .footer {{
            text-align: center;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
        }}
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<p class="title">📊 ALL APPS for Analysing Data - Chartwell Hospital</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Click below to open one of the apps:</p>', unsafe_allow_html=True)

# Create Columns for Better Layout
col1, col2 = st.columns(2)

# First App Button
with col1:
    st.markdown('<a class="button" href="https://yp2opqdw5du4x4cevfryet.streamlit.app/">🔊 Open Transcribe & Analyse</a>', unsafe_allow_html=True)

# Second App Button
with col2:
    st.markdown('<a class="button" href="https://a2rpeak3gt2tflgd4skjvv.streamlit.app/">📞 Open Call Analysis V4</a>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<p class="footer">Made with ❤️ for Chartwell Hospital | Powered by Streamlit</p>', unsafe_allow_html=True)
