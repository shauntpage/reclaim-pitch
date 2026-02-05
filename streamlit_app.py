import streamlit as st
import time

# 1. Setup
st.set_page_config(page_title="Reclaim Home", layout="wide")

# 2. Check if the URL tells us to open the scanner
query_params = st.query_params
is_scanning = query_params.get("scan") == "true"

# 3. Design (HTML/CSS)
st.markdown("""
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<style>
    #MainMenu, .stDeployButton, footer, header {visibility: hidden;}
    .block-container { padding: 0 !important; max-width: 100%; }
    .stApp { background-color: #f4f6f8; }
    
    .grid-container {
        display: grid; grid-template-columns: repeat(5, 1fr);
        gap: 10px; margin: 50px 10px 20px 10px; text-align: center;
    }
    .icon-col { display: flex; flex-direction: column; align-items: center; text-decoration: none; }
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
        padding: 15px; border-radius: 8px; margin: 0 10px 20px 10px;
    }
</style>

<div class="grid-container">
    <div class="icon-col">
        <div class="icon-box blue"><i class="material-icons">search</i></div>
        <div class="label">Search</div>
    </div>
    
    <a href="/?scan=true" target="_self" class="icon-col">
        <div class="icon-box orange">
            <i class="material-icons">qr_code_scanner</i>
        </div>
        <div class="label">New Scan</div>
    </a>

    <div class="icon-col">
        <div class="icon-box blue"><i class="material-icons">add_box</i></div>
        <div class="label">Add Asset</div>
    </div>
    <div class="icon-col">
        <div class="icon-box blue"><i class="material-icons">bolt</i></div>
        <div class="label">Reclaim</div>
    </div>
    <div class="icon-col">
        <div class="icon-box blue"><i class="material-icons">ios_share</i></div>
        <div class="label">Share</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Logic: Show Camera ONLY if scan=true in the URL
if is_scanning:
    # A simple back button to return home
    if st.button("⬅️ Cancel Scan", use_container_width=True):
        st.query_params.clear()
        st.rerun()

    img_file = st.camera_input("Scan Appliance Label")

    if img_file:
        with st.status("AI Analyzing image...", expanded=True) as status:
            st.write("Extracting Model Number...")
            time.sleep(1)
            st.write("Searching manufacturer database...")
            time.sleep(1)
            status.update(label="Appliance Identified!", state="complete", expanded=False)
        
        st.success("**Matched: Bosch Dishwasher (Series 800)**")
        st.info("✅ Manual Downloaded | ✅ Warranty Registered")
        if st.button("Done - Back to Home"):
            st.query_params.clear()
            st.rerun()
else:
    # Standard Dashboard View
    st.markdown('<div class="banner"><b>Critical Alert:</b> Water Heater sensor detected anomaly.</div>', unsafe_allow_html=True)
    st.write("")
    st.info("No other events today. Click 'New Scan' to add an appliance.")

# 5. Fixed Nav
st.markdown("""
<div style="position: fixed; bottom: 0; left: 0; width: 100%; background: white; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #eee; z-index: 999;">
    <div style="text-align:center; color:#007bff"><i class="material-icons">home</i><div style="font-size:10px">Home</div></div>
    <div style="text-align:center; color:#999"><i class="material-icons">assignment</i><div style="font-size:10px">Assets</div></div>
    <div style="text-align:center; color:#999"><i class="material-icons">account_balance_wallet</i><div style="font-size:10px">Ledger</div></div>
    <div style="text-align:center; color:#999"><i class="material-icons">group</i><div style="font-size:10px">Team</div></div>
</div>
""", unsafe_allow_html=True)