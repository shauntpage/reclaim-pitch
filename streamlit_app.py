import streamlit as st

# --- CONFIG ---
st.set_page_config(page_title="Reclaim", page_icon="⚡", layout="centered")

# --- DIRECTOR MODE (The Safety Net) ---
# On mobile, click the '>' arrow in top-left to switch screens
st.sidebar.title("🎬 Demo Controls")
demo_phase = st.sidebar.radio(
    "Jump to Screen:",
    ["1. Home (Zoom UI)", "2. The Scan", "3. The Ledger (Money)"]
)

# --- CSS (Zoom Dark Mode) ---
st.markdown("""
    <style>
    .stApp {background-color: #1a1a1a; font-family: sans-serif;}
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 1rem; padding-bottom: 5rem;}
    
    /* ZOOM HEADER */
    .zoom-header {display: flex; justify-content: space-between; align-items: center; color: white; margin-bottom: 20px;}
    .profile {width: 35px; height: 35px; background: #555; border-radius: 10px; text-align:center; line-height:35px; font-size:12px;}
    
    /* ICONS GRID */
    .grid {display: flex; justify-content: space-between; margin-bottom: 20px;}
    .icon-col {text-align: center; width: 22%;}
    .icon-box {height: 60px; width: 60px; border-radius: 18px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin: 0 auto 5px auto; color: white;}
    .orange {background: #ff742e;}
    .blue {background: #0e72ec;}
    .label {font-size: 11px; color: #aaa;}

    /* BANNER */
    .banner {background: linear-gradient(90deg, #0e72ec, #2D8CF0); border-radius: 12px; padding: 15px; color: white; margin-bottom: 20px;}
    
    /* BOTTOM NAV */
    .nav {position: fixed; bottom: 0; left: 0; width: 100%; background: #1a1a1a; border-top: 1px solid #333; display: flex; justify-content: space-around; padding: 15px 0;}
    .nav-item {color: #888; font-size: 20px;}
    .active {color: white;}
    
    /* ANIMATIONS */
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(242, 109, 33, 0.7); }
        70% { box-shadow: 0 0 0 20px rgba(242, 109, 33, 0); }
        100% { box-shadow: 0 0 0 0 rgba(242, 109, 33, 0); }
    }
    .scanner {border: 2px solid #ff742e; height: 300px; border-radius: 20px; animation: pulse 2s infinite; display:flex; align-items:center; justify-content:center;}
    
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
            <div>🔍 &nbsp; ➕</div>
        </div>
    """, unsafe_allow_html=True)

    # Grid (Visual Only)
    st.markdown("""
        <div class="grid">
            <div class="icon-col"><div class="icon-box orange">📷</div><div class="label">Scan</div></div>
            <div class="icon-col"><div class="icon-box blue">✚</div><div class="label">Add</div></div>
            <div class="icon-col"><div class="icon-box blue">⚡</div><div class="label">FigJam</div></div>
            <div class="icon-col"><div class="icon-box blue">📤</div><div class="label">Share</div></div>
        </div>
        <div class="banner">
            <div style="font-weight:bold; margin-bottom:5px;">⚠️ Critical Alert</div>
            <div style="font-size:13px; margin-bottom:10px; opacity:0.9;">Water Heater sensor detected anomaly.</div>
            <div style="background:rgba(0,0,0,0.2); display:inline-block; padding:5px 15px; border-radius:15px; font-size:12px; font-weight:bold;">VIEW DIAGNOSTIC</div>
        </div>
        <div style="text-align:center; color:#555; margin-top:40px; font-size:14px;">No other events today</div>
    """, unsafe_allow_html=True)

    # Fake Bottom Nav
    st.markdown("""
        <div class="nav">
            <div class="nav-item active">🏠</div>
            <div class="nav-item">📋</div>
            <div class="nav-item">💰</div>
            <div class="nav-item">👥</div>
        </div>
    """, unsafe_allow_html=True)

# --- SCENE 2: SCANNER ---
elif demo_phase == "2. The Scan":
    st.markdown("""
        <div class="zoom-header">
            <span style="color:#0e72ec;">Cancel</span>
            <span style="font-weight:600;">Scanner</span>
            <span>⚡</span>
        </div>
        <div class="scanner">
            <h2 style="color:#ff742e; font-family:monospace;">SCANNING...</h2>
        </div>
        <div style="margin-top:20px; text-align:center; color:white;">
            <p>Identifying Asset...</p>
            <h3 style="color:#4CD964;">Rheem Platinum</h3>
        </div>
        <div style="text-align:center; margin-top:50px;">
             <div style="width:60px; height:60px; border-radius:50%; border:4px solid white; margin:auto;"></div>
        </div>
    """, unsafe_allow_html=True)

# --- SCENE 3: LEDGER ---
elif demo_phase == "3. The Ledger (Money)":
    st.markdown("""
        <div class="zoom-header">
            <div class="profile">SP</div>
            <span style="font-weight:600;">Assets & Money</span>
            <span>🔍</span>
        </div>
    """, unsafe_allow_html=True)
    
    # This was the part that broke - now fixed:
    items = [
        ("Kitchen Fridge", "healthy", "Healthy"),
        ("Water Heater", "crit", "Critical (14y)"),
        ("HVAC System", "healthy", "Healthy"),
        ("Tesla Charger", "healthy", "Healthy")
    ]
    
    for name, status, label in items:
        color = "#FF3B30" if status == "crit" else "#4CD964"
        st.markdown(f"""
            <div style="background:#222; padding:15px; border-radius:12px; margin-bottom:10px; display:flex; align-items:center; color:white;">
                <div style="width:10px; height:10px; background:{color}; border-radius:50%; margin-right:15px;"></div>
                <div style="flex-grow:1;">
                    <div style="font-weight:600;">{name}</div>
                    <div style="font-size:12px; color:#aaa;">{label}</div>
                </div>
                <div style="color:#555;">></div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="nav">
            <div class="nav-item">🏠</div>
            <div class="nav-item">📋</div>
            <div class="nav-item active">💰</div>
            <div class="nav-item">👥</div>
        </div>
    """, unsafe_allow_html=True)