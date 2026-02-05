import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Reclaim Home", layout="wide")

# 2. Design (CSS) - Fixed for iPhone notch and mobile view
st.markdown("""
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<style>
    /* Hide Streamlit default UI for a clean app feel */
    #MainMenu, .stDeployButton, footer, header {visibility: hidden;}
    .block-container { padding: 0 !important; max-width: 100%; }
    .stApp { background-color: #f4f6f8; }
    
    /* Top Action Grid */
    .grid-container {
        display: grid; 
        grid-template-columns: repeat(5, 1fr);
        gap: 10px; 
        margin: 65px 10px 20px 10px; 
        text-align: center;
    }
    .icon-col { display: flex; flex-direction: column; align-items: center; text-decoration: none; }
    
    .icon-box {
        width: 50px; height: 50px; border-radius: 12px;
        display: flex; align-items: center; justify-content: center;
        color: white; margin-bottom: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .blue { background-color: #007bff; }
    .orange { background-color: #ff742e; }
    .label { font-size: 10px; color: #333; font-weight: 600; text-decoration: none; }

    /* Alert Banner */
    .banner {
        background-color: #ffebee; border-left: 5px solid #d32f2f;
        padding: 15px; border-radius: 8px; margin: 0 10px 20px 10px;
        display: flex; align-items: center; cursor: pointer;
    }
    .banner-text { font-size: 13px; color: #d32f2f; font-weight: bold; }

    /* Bottom Nav Bar */
    .nav {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: white; display: flex; justify-content: space-around;
        padding: 15px 0; border-top: 1px solid #eee; z-index: 999;
    }
</style>

<div class="grid-container">
    <a href="/?page=search" target="_self" class="icon-col">
        <div class="icon-box blue"><i class="material-icons">search</i></div>
        <div class="label">Search</div>
    </a>
    
    <a href="/?page=scan" target="_self" class="icon-col">
        <div class="icon-box orange"><i class="material-icons">qr_code_scanner</i></div>
        <div class="label">New Scan</div>
    </a>

    <a href="/?page=add" target="_self" class="icon-col">
        <div class="icon-box blue"><i class="material-icons">add_box</i></div>
        <div class="label">Add Asset</div>
    </a>

    <a href="/?page=reclaim" target="_self" class="icon-col">
        <div class="icon-box blue"><i class="material-icons">bolt</i></div>
        <div class="label">Reclaim</div>
    </a>

    <a href="/?page=share" target="_self" class="icon-col">
        <div class="icon-box blue"><i class="material-icons">ios_share</i></div>
        <div class="label">Share</div>
    </a>
</div>
""", unsafe_allow_html=True)

# 3. Navigation & Page Content Logic
# This reads the URL to see which 'page' was clicked in the HTML above
current_page = st.query_params.get("page", "home")

# A quick helper to reset to home
def back_to_home():
    st.query_params.clear()
    st.rerun()

# --- THE ROUTER ---

if current_page == "search":
    st.button("⬅️ Home", on_click=back_to_home)
    st.subheader("Inventory Search")
    st.text_input("Find asset, manual, or history...", placeholder="e.g. Jeep Cherokee")

elif current_page == "scan":
    st.button("⬅️ Home", on_click=back_to_home)
    st.subheader("AI Barcode Scanner")
    img = st.camera_input("Position model label in frame")
    if img:
        st.success("Barcode Identified: Bosch SHPM65Z55N")

elif current_page == "add":
    st.button("⬅️ Home", on_click=back_to_home)
    st.subheader("Manual Asset Entry")
    with st.form("entry"):
        st.text_input("Manufacturer & Model")
        st.date_input("Purchase/Install Date")
        st.form_submit_button("Save to Inventory")

elif current_page == "reclaim":
    st.button("⬅️ Home", on_click=back_to_home)
    st.subheader("Reclaim Portal")
    st.metric("Potential Unclaimed Rebates", "$215.00")
    st.metric("Active Warranties", "4 Assets")
    st.info("AI Analysis: You are eligible for a $50 rebate on your last Water Heater service.")

elif current_page == "share":
    st.button("⬅️ Home", on_click=back_to_home)
    st.subheader("Share Access")
    st.write("Grant temporary access to a service professional.")
    st.button("Generate QR Code for Contractor")

elif current_page == "diagnostic":
    st.button("⬅️ Home", on_click=back_to_home)
    st.error("### ⚠️ Diagnostic Alert: Water Heater")
    st.write("**Model:** Rheem Performance Platinum")
    st.write("**Issue:** Lower heating element failure detected.")
    st.button("🛒 Buy Replacement Part ($28.99)")
    st.button("🛠️ View DIY Repair Video")

else:
    # --- DEFAULT HOME PAGE ---
    st.markdown("""
    <a href="/?page=diagnostic" target="_self" style="text-decoration:none;">
        <div class="banner">
            <div class="banner-text">⚠️ Critical Alert: Water Heater sensor anomaly</div>
        </div>
    </a>
    """, unsafe_allow_html=True)
    st.write("")
    st.info("All other systems (Solar, HVAC, Dishwasher) are online.")

# 4. Global Navigation (The Static Bottom Bar)
st.markdown("""
<div class="nav">
    <div style="text-align:center; color:#007bff"><i class="material-icons">home</i><div style="font-size:10px">Home</div></div>
    <div style="text-align:center; color:#999"><i class="material-icons">assignment</i><div style="font-size:10px">Assets</div></div>
    <div style="text-align:center; color:#999"><i class="material-icons">account_balance_wallet</i><div style="font-size:10px">Ledger</div></div>
    <div style="text-align:center; color:#999"><i class="material-icons">group</i><div style="font-size:10px">Team</div></div>
</div>
""", unsafe_allow_html=True)