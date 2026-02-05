import streamlit as st

# 1. Setup
st.set_page_config(page_title="Reclaim Home", layout="wide")

# 2. Routing Logic (This must come BEFORE the HTML to catch the clicks)
# We check the URL to see which page to show. Default is 'home'.
page = st.query_params.get("page", "home")

# 3. Styling & The Icon Grid
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
    .icon-col { display: flex; flex-direction: column; align-items: center; text-decoration: none; color: inherit; }
    .icon-box {
        width: 50px; height: 50px; border-radius: 12px;
        display: flex; align-items: center; justify-content: center;
        color: white; margin-bottom: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .blue { background-color: #007bff; }
    .orange { background-color: #ff742e; }
    .label { font-size: 10px; color: #333; font-weight: 600; }

    .banner {
        background-color: #ffebee; border-left: 5px solid #d32f2f;
        padding: 15px; border-radius: 8px; margin: 0 10px 20px 10px;
        display: flex; align-items: center;
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

# 4. Page Content Selection
if page == "home":
    st.markdown("""
    <div class="banner">
        <div style="color: #d32f2f; font-weight: bold; font-size: 14px;">
            ⚠️ Critical Alert: Water Heater anomaly detected
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.info("Everything else looks good, Shaun.")

elif page == "scan":
    if st.button("⬅️ Back to Home"):
        st.query_params.clear()
        st.rerun()
    st.subheader("Scan Appliance")
    st.camera_input("Capture Barcode")

elif page == "reclaim":
    if st.button("⬅️ Back to Home"):
        st.query_params.clear()
        st.rerun()
    st.subheader("Reclaim Hub")
    st.metric("Tax Credits Available", "$1,200")
    st.write("Based on your HVAC model, you are eligible for federal rebates.")

elif page == "add":
    if st.button("⬅️ Back to Home"):
        st.query_params.clear()
        st.rerun()
    st.subheader("Add Asset")
    st.text_input("Enter Model Name")
    st.button("Save")

elif page == "search":
    if st.button("⬅️ Back to Home"):
        st.query_params.clear()
        st.rerun()
    st.text_input("Search your home...")

elif page == "share":
    if st.button("⬅️ Back to Home"):
        st.query_params.clear()
        st.rerun()
    st.write("Generating contractor access link...")

# 5. Bottom Navigation Bar (Visual Only)
st.markdown("""
<div style="position: fixed; bottom: 0; left: 0; width: 100%; background: white; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #eee; z-index: