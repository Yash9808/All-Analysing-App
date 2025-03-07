import streamlit as st

# Custom Page Configuration
st.set_page_config(page_title="Chartwell Data Analysis", page_icon="📊", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .title {
            font-size: 2.2em;
            font-weight: bold;
            text-align: center;
            color: #4A90E2;
        }
        .subtitle {
            font-size: 1.3em;
            text-align: center;
            color: #333;
            margin-bottom: 20px;
        }
        .button {
            width: 100%;
            display: inline-block;
            padding: 15px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            background-color: #4A90E2;
            color: white;
            border-radius: 10px;
            text-decoration: none;
            transition: 0.3s;
        }
        .button:hover {
            background-color: #357ABD;
        }
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
st.markdown('<p style="text-align: center;"> 🧠 Chartwell Hospital | Powered by Streamlit</p>', unsafe_allow_html=True)
