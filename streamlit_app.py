import streamlit as st

# 1. Setup
st.set_page_config(page_title="Reclaim Home", layout="wide")

# 2. State Management - tracks if we are currently "scanning"
if 'scanning' not in st.session_state:
    st.session_state.scanning = False

def toggle_scan():
    st.session_state.scanning = not st.session_state.scanning

# 3. The Design (HTML/CSS)
st.markdown("""
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<style>
    #MainMenu, .stDeployButton, footer, header {visibility: hidden;}
    .block-container { padding: 0 !important; max-width: 100%; }
    .stApp { background-color: #f4f6f8; }
    
    .grid-container {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 10px;
        margin: 50px 10px 20px 10px;
        text-align: center;
    }
    .icon-col { display: flex; flex-direction: column; align-items: center; }
    .icon-box {
        width: 50px; height: 50px; border-radius: 12px;
        display: flex; align-items: center; justify-content: center;
        color: white; margin-bottom: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .blue { background-color: #007bff; }
    .orange { background-color: #ff742e; }
    .label { font-size: 10px; color: #333; font-weight: 500; }

    .banner {
        background-color: #ffebee; border-left: 5px solid #d32f2f;
        padding: 15px; border-radius: 8px; display: flex;
        align-items: center; justify-content: space-between;
        margin: 0 10px 20px 10px;
    }
    .banner-text h4 { margin: 0; color: #d32f2f; font-size: 14px; }
    .banner-text p { margin: 2px 0 0 0; font-size: 12px; color: #555; }
    
    /* Bottom Nav */
    .nav {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: white; display: flex; justify-content: space-around;
        padding: 15px 0; border-top: 1px solid #eee; z-index: 999;
    }
</style>

<div class="grid-container">
    <div class="icon-col"><div class="icon-box blue"><i class="material-icons">search</i></div><div class="label">Search</div></div>
    <div class="icon-col"><div class="icon-box orange"><i class="material-icons">qr_code_scanner</i></div><div class="label">New Scan</div></div>
    <div class="icon-col"><div class="icon-box blue"><i class="material-icons">add_box</i></div><div class="label">Add Asset</div></div>
    <div class="icon-col"><div class="icon-box blue"><i class="material-icons">bolt</i></div><div class="label">Reclaim</div></div>
    <div class="icon-col"><div class="icon-box blue"><i class="material-icons">ios_share</i></div><div class="label">Share</div></div>
</div>

<div class="banner">
    <div class="banner-text">
        <h4>Critical Alert</h4>
        <p>Water Heater sensor detected anomaly.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Functional Python Bridge
# Since HTML buttons in st.markdown can't easily trigger Python, 
# we use a standard Streamlit button to "Activate" the scanner for this demo.

st.write("---")
if not st.session_state.scanning:
    if st.button("🚀 Activate Scanner", use_container_width=True):
        st.session_state.scanning = True
        st.rerun()
else:
    if st.button("❌ Close Scanner", use_container_width=True):
        st.session_state.scanning = False
        st.rerun()
    
    # This is the "Magic" - The actual camera input
    img_file = st.camera_input("Scan Appliance Label")
    
    if img_file:
        st.success("Barcode/Label detected! Processing with AI...")
        st.info("Searching for: Bosch Dishwasher SHPM65Z55N Manual...")

# 5. Bottom Navigation Design
st.markdown("""
<div class="nav">
    <div class="nav-item"><i class="material-icons" style="color:#007bff">home</i><div class="nav-label">Home</div></div>
    <div class="nav-item"><i class="material-icons" style="color:#999">assignment</i><div class="nav-label">Assets</div></div>
    <div class="nav-item"><i class="material-icons" style="color:#999">account_balance_wallet</i><div class="nav-label">Ledger</div></div>
    <div class="nav-item"><i class="material-icons" style="color:#999">group</i><div class="nav-label">Team</div></div>
</div>
""", unsafe_allow_html=True)