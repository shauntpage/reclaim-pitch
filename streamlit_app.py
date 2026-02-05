import streamlit as st

# --- CONFIG ---
st.set_page_config(page_title="Reclaim", page_icon="⚡", layout="centered")

# --- DIRECTOR MODE (The Safety Net) ---
st.sidebar.title("🎬 Demo Controls")
demo_phase = st.sidebar.radio(
    "Jump to Screen:",
    ["1. Home (Zoom UI)", "2. The Scan", "3. The Ledger (Money)"]
)

# --- CSS (The Design Layer) ---
# This block makes it look like a native app. 
# DO NOT DELETE 'unsafe_allow_html=True' at the end!
st.markdown("""
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
    .stApp {background-color: #1a1a1a; font-family: sans-serif;}
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 1rem; padding-bottom: 5rem;}
    
    /* ZOOM HEADER */
    .zoom-header {display: flex; justify-content: space-between; align-items: center; color: white; margin-bottom: 20px;}
    .profile {width: 35px; height: 35px; background: #555; border-radius: 10px; text-align:center; line-height:35px; font-size:12px; color:white;}
    
    /* ICONS GRID */
    .grid {display: flex; justify-content: space-between; margin-bottom: 20px;}
    .icon-col {text-align: center; width: 22%;}
    .icon-box {height: 60px; width: 60px; border-radius: 18px; display: flex; align-items: center; justify-content: center; margin: 0 auto 5px auto;}
    .material-icons {font-size: 30px; color: white;} 
    
    .orange {background: #ff742e;}
    .blue {background: #0e72ec;}
    .label {font-size: 11px; color: #aaa; margin-top: 5px;}

    /* BANNER */
    .banner {background: linear-gradient(90deg, #0e72ec, #2D8CF0); border-radius: 12px; padding: 15px; color: white; margin-bottom: 20px;}
    
    /* BOTTOM NAV */
    .nav {position: fixed; bottom: 0; left: 0; width: 100%; background: #1a1a1a; border-top: 1px solid #333; display: flex; justify-content: space-around; padding: 15px 0; z-index: 999;}
    .nav-item {color: #888; text-align: center; cursor: pointer;}
    .nav-item .material-icons {font-size: 28px; color: #888;}
    .nav-item.active .material-icons {color: white;}
    .nav-label {font-size: 10px; color: #888; display: block;}
    .active .nav-label {color: white;}
    
    /* ANIMATIONS */
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(242, 109, 33, 0.7); }
        70% { box-shadow: 0 0 0 20px rgba(242, 109, 33, 0); }
        100% { box-shadow: 0 0 0 0 rgba(242, 109, 33, 0); }
    }
    .scanner {border: 2px solid #ff742e; height: 300px; border-radius: 20px; animation: pulse 2s infinite; display:flex; align-items:center; justify-content:center; margin-top: 20px;}
    
    </style>
""", unsafe_allow_html=True)

# --- SCENE 1: HOME ---
if demo_phase == "1. Home (Zoom UI)":
    # Header
    st.markdown("""
        <div class="zoom-header">
            <div style="display:flex; gap:10px; align-items:center;">
                <div class="profile">SP</div>
                <span style="font-weight:600; font-size:18px;">Home</span>
            </div>
            <div><span class="material-icons" style="font-size:24px;">search</span></div>
        </div>
    """, unsafe_allow_html=True)

    # Grid (Professional Icons)
    st.markdown("""
        <div class="grid">
            <div class="icon-col">
                <div class="icon-box orange"><span class="material-icons">qr_code_scanner</span></div>
                <div class="label">New Scan</div>
            </div>
            <div class="icon-col">
                <div class="icon-box blue"><span class="material-icons">add_box</span></div>
                <div class="label">Add Asset</div>
            </div>
            <div class="icon-col">
                <div class="icon-box blue"><span class="material-icons">bolt</span></div>
                <div class="label">Reclaim</div>
            </div>
            <div class="icon-col">
                <div class="icon-box blue"><span class="material-icons">ios_share</span></div>
                <div class="label">Share</div>
            </div>
        </div>
        
        <div class="banner">
            <div style="font-weight:bold; margin-bottom:5px; display:flex; align-items:center; gap:10px;">
                <span class="material-icons" style="font-size:20px;">warning</span> Critical Alert
            </div>
            <div style="font-size:13px; margin-bottom:10px; opacity:0.9;">Water Heater sensor detected anomaly.</div>
            <div style="background:rgba(0,0,0,0.2); display:inline-block; padding:5px 15px; border-radius:15px; font-size:12px; font-weight:bold;">VIEW DIAGNOSTIC</div>
        </div>
        <div style="text-align:center; color:#555; margin-top:40px; font-size:14px;">No other events today</div>
    """, unsafe_allow_html=True)

    # Bottom Nav (Professional)
    st.markdown("""
        <div class="nav