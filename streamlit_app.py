import streamlit as st
import time

# 1. Page Config
st.set_page_config(page_title="Reclaim Home", layout="wide")

# 2. CSS Styling (The Design)
st.markdown("""
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<style>
    /* Hide Streamlit default UI */
    #MainMenu, .stDeployButton, footer, header {visibility: hidden;}
    .block-container { padding: 0 !important; max-width: 100%; }
    .stApp { background-color: #f4f6f8; }
    
    /* Grid Layout for Top Icons */
    .grid-container {
        display: grid; 
        grid-template-columns: repeat(5, 1fr);
        gap: 10px; 
        margin: 65px 10px 20px 10px; /* Pushes content below the iPhone notch */
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
        display: flex; align-items: center;
    }
    .banner-text { font-size: 14px; color: #d32f2f; font-weight: bold; }

    /* Bottom Nav */
    .nav {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: white; display: flex; justify-content: space-around;
        padding: 15px 0; border-top: 1px solid #eee; z-index: 999;
    }
</style>

<div class="grid-container">
    <div class="icon-col">
        <div class="icon-box blue"><i class="material-icons">search</i></div>
        <div class="label">Search</div>
    </div>
    
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

# 3. Navigation & App Logic
current_page = st.query_params.get("page", "home")

if current_page == "scan":
    if st.button("⬅️ Back to Dashboard"):
        st.query_params.clear()
        st.rerun()
    
    st.subheader("Appliance Scanner")
    img_file = st.camera_input("Scan Barcode or Model Number")
    
    if img_file:
        with st.status("Analyzing...", expanded=True) as status:
            time.sleep(1)
            st.write("Extracting details...")
            time.sleep(1)
            status.update(label="Match Found!", state="complete")
        st.success("Identified: Bosch Series 800 Dishwasher")

elif current_page == "add":
    if st.button("⬅️ Back"):
        st.query_params.clear()
        st.rerun()
    st.subheader("Add Asset Manually")
    st.text_input("Brand / Model Name")

elif current_page == "reclaim":
    if st.button("⬅️ Back"):
        st.query_params.clear()
        st.rerun()
    st.subheader("Reclaim Values")
    st.metric("Potential Rebates", "$150.00")
    st.metric("Warranty Savings", "$450.00")

else:
    # Home Page Default View
    st.markdown("""
    <div class="banner">
        <div class="banner-text">⚠️ Critical Alert: Water Heater sensor anomaly</div>
    </div>
    """, unsafe_allow_html=True)
    st.info("No other maintenance tasks today.")

# 4. Bottom Nav Bar
st.markdown("""
<div class="nav">
    <div style="text-align:center; color:#007bff"><i class="material-icons">home</i><div style="font-size:10px">Home</div></div>
    <div style="text-align:center; color:#999"><i class="material-icons">assignment</i><div style="font-size:10px">Assets</div></div>
    <div style="text-align:center; color:#999"><i class="material-icons">account_balance_wallet</i><div style="font-size:10px">Ledger</div></div>
    <div style="text-align:center; color:#999"><i class="material-icons">group</i><div style="font-size:10px">Team</div></div>
</div>
""", unsafe_allow_html=True)