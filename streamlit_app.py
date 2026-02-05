import streamlit as st
import time

# 1. Page Config
st.set_page_config(page_title="Reclaim Home", layout="wide")

# 2. CSS Styling (iPhone Notch fix + UI Clean up)
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

    .banner {
        background-color: #ffebee; border-left: 5px solid #d32f2f;
        padding: 15px; border-radius: 8px; margin: 0 10px 20px 10px;
        display: flex; align-items: center; cursor: pointer;
    }
    .banner-text { font-size: 13px; color: #d32f2f; font-weight: bold; }

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

# 3. Navigation Logic
current_page = st.query_params.get("page", "home")

# Function to go back home
def go_home():
    st.query_params.clear()
    st.rerun()

# --- PAGE ROUTING ---

if current_page == "search":
    st.button("⬅️ Back", on_click=go_home)
    st.subheader("Search Inventory")
    st.text_input("Find an appliance, manual, or receipt...", placeholder="e.g. Dishwasher")

elif current_page == "scan":
    st.button("⬅️ Back", on_click=go_home)
    st.subheader("AI Appliance Scanner")
    img = st.camera_input("Scan Barcode")
    if img:
        st.success("Barcode Detected: Rheem XE50T12CS55U1")

elif current_page == "add":
    st.button("⬅️ Back", on_click=go_home)
    st.subheader("Manual Asset Entry")
    with st.form("add_form"):
        st.text_input("Brand/Model")
        st.date_input("Purchase Date")
        st.file_uploader("Upload Receipt/Warranty")
        st.form_submit_button("Save Asset")

elif current_page == "reclaim":
    st.button("⬅️ Back", on_click=go_home)
    st.subheader("Reclaim Portal")
    st.write("We found **3 potential savings** for your home:")
    st.metric("Energy Star Rebate", "$75.00")
    st.metric("Class Action (Dishwasher)", "$120.00")
    st.info("Click to file claim automatically.")

elif current_page == "share":
    st.button("⬅️ Back", on_click=go_home)
    st.subheader("Share Home Access")
    st.write("Generate a secure link for a service professional.")
    st.selectbox("Select Duration", ["1 Hour", "24 Hours", "Permanent"])
    st.button("Generate Secure Link")

elif current_page == "diagnostic":
    st.button("⬅️ Back", on_click=go_home)
    st.error("### ⚠️ Water Heater Alert")
    st.write("**Detected:** Inconsistent heating cycle.")
    st.write("**Part Required:** Upper Heating Element (Rheem Part #SP10869L)")
    st.button("🛒 Order Part via Amazon")
    st.button("🛠️ Watch DIY Replacement Guide")

else:
    # --- HOME PAGE VIEW ---
    st.markdown("""
    <a href="/?page=diagnostic" target="_self" style="text-decoration:none;">
        <div class="banner">
            <div class="banner-text">⚠️ Critical Alert: Water Heater anomaly</div>
        </div>
    </a>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.info("System Status: All other assets performing within normal range.")

# 4. Fixed Nav Bar (Bottom)
st.markdown("""
<div class="nav">
    <div style="text-align:center; color:#007bff"><i class="material-icons">home</i><div style="font-size:10px">Home</div></div>
    <div style="text-align:center; color:#999"><i class="material-icons">assignment</i><div style="font-size:10px">Assets</div></div>
    <div style="text-align:center; color:#999"><i class="material-icons">account_balance_wallet</i><div style="font-size:10px">Ledger</div></div>
    <div style="text-align:center; color:#999"><i class="material-icons">group</i><div style="font-size:10px">Team</div></div>
</div>
""", unsafe_allow_html=True)