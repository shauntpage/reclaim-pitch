import streamlit as st

# This MUST be the first line using 'st'
st.set_page_config(page_title="Reclaim Home", layout="wide")

# Now your markdown will work
st.markdown("""
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
...
# Updated HTML Grid with active links for all icons
st.markdown("""
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

# --- Python Navigation Logic ---
current_page = st.query_params.get("page", "home")

if current_page == "scan":
    if st.button("⬅️ Back"):
        st.query_params.clear()
        st.rerun()
    st.camera_input("Scan Appliance Label")

elif current_page == "add":
    if st.button("⬅️ Back"):
        st.query_params.clear()
        st.rerun()
    st.subheader("Add Asset Manually")
    st.text_input("Brand / Model")
    st.date_input("Purchase Date")

elif current_page == "reclaim":
    if st.button("⬅️ Back"):
        st.query_params.clear()
        st.rerun()
    st.subheader("Reclaim Center")
    st.info("Searching for tax credits, rebates, and warranty claims for your home...")

elif current_page == "share":
    if st.button("⬅️ Back"):
        st.query_params.clear()
        st.rerun()
    st.subheader("Share Access")
    st.write("Invite a family member or service professional to view your assets.")

else:
    # Default Dashboard View (The Banner and Status)
    st.markdown('<div class="banner"><b>Critical Alert:</b> Water Heater sensor detected anomaly.</div>', unsafe_allow_html=True)
    st.info("No other events today.")