import streamlit as st

# ----- Page Setup -----
st.set_page_config(
    page_title="Snapchat Demo",
    page_icon="👻",
    layout="centered",
)

# ----- Custom CSS for Snapchat-like Design -----
st.markdown("""
    <style>
        .snap-title {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #FFFC00;  /* Snapchat yellow */
            text-shadow: 2px 2px 4px #00000050;
        }
        .snap-subtitle {
            font-size: 22px;
            text-align: center;
            margin-top: -10px;
            color: white;
        }
        .center-btn {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }
