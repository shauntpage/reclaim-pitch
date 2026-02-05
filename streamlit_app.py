import streamlit as st

# 1. Set page configuration to force a light theme and wide layout
st.set_page_config(
    page_title="Reclaim Home",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS to hide Streamlit elements and fix layout
st.markdown("""
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        /* --- HIDE STREAMLIT DEFAULT ELEMENTS --- */
        #MainMenu {visibility: hidden;} /* Hides the hamburger menu */
        .stDeployButton {visibility: hidden;} /* Hides the "Fork"/Crown button */
        footer {visibility: hidden;} /* Hides the "Made with Streamlit" footer */
        header {visibility: hidden;} /* Hides the entire top header bar */

        /* --- MAIN CONTAINER & THEME --- */
        .block-container {
            padding: 0 !important;
            max-width: 100%;
        }
        
        /* Force light background for the main area */
        .stApp {
            background-color: #f4f6f8;
        }

        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
        }

        /* --- CUSTOM COMPONENT STYLES --- */
        
        /* Grid Layout for Top Icons */
        .grid-container {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
            /* Added more margin at the top to push it down from the status bar */
            margin: 50px 10px 20px 10px;
            text-align: center;
        }

        .icon-col {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .icon-box {
            width: 50px;
            height: 50px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            margin-bottom: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            cursor: pointer;
        }

        .icon-box.blue { background-color: #007bff; }
        .icon-box.orange { background-color: #ff742e; }
        
        .label {
            font-size: 10px;
            color: #333;
            font-weight: 500;
        }

        /* Critical Alert Banner */
        .banner {
            background-color: #ffebee;
            border-left: 5px solid #d32f2f;
            padding: 15px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin: 0 10px 20px 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        .banner-icon { color: #d32f2f; margin-right: 10px; }
        
        .banner-text h4 {
            margin: 0;
            color: #d32f2f;
            font-size: 14px;
            font-weight: bold;
        }

        .banner-text p {
            margin: 2px 0 0 0;
            font-size: 12px;
            color: #555;
        }

        .banner-action {
            font-size: 11px;
            font-weight: bold;
            color: #d32f2f;
            text-transform: uppercase;
            white-space: nowrap;
            cursor: pointer;
        }

        /* Info Text */
        .info-text {
            text-align: center;
            color: #999;
            font-size: 14px;
            margin: 20px 0;
        }

        /* Scanner Circle */
        .scanner-container {
            display: flex;
            justify-content: center;
            margin: 30px 0;
        }

        .scanner {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            border: 2px dashed #ccc;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #ccc;
        }
        
        .scanner i { font-size: 40px; }

        /* Bottom Navigation */
        .nav {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: white;
            display: flex;
            justify-content: space-around;
            padding: 15px 0;
            border-top: 1px solid #eee;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
            z-index: 999;
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            color: #999;
            cursor: pointer;
        }

        .nav-item.active { color: #007bff; }
        
        .nav-item i { font-size: 24px; margin-bottom: 2px; }
        .nav-label { font-size: 10px; }
    </style>

    <div class="grid-container">
        <div class="icon-col">
            <div class="icon-box blue">
                <i class="material-icons">search</i>
            </div>
            <div class="label">Search</div>
        </div>
        <div class="icon-col">
            <div class="icon-box orange">
                <i class="material-icons">qr_code_scanner</i>
            </div>
            <div class="label">New Scan</div>
        </div>
        <div class="icon-col">
            <div class="icon-box blue">
                <i class="material-icons">add_box</i>
            </div>
            <div class="label">Add Asset</div>
        </div>
        <div class="icon-col">
            <div class="icon-box blue">
                <i class="material-icons">bolt</i>
            </div>
            <div class="label">Reclaim</div>
        </div>
         <div class="icon-col">
            <div class="icon-box blue">
                <i class="material-icons">ios_share</i>
            </div>
            <div class="label">Share</div>
        </div>
    </div>

    <div class="banner">
        <div class="banner-icon">
            <i class="material-icons">warning</i>
        </div>
        <div class="banner-text">
            <h4>Critical Alert</h4>
            <p>Water Heater sensor detected anomaly.</p>
        </div>
        <div class="banner-action">
            VIEW DIAGNOSTIC
        </div>
    </div>

    <div class="info-text">No other events today</div>

    <div class="scanner-container">
        <div class="scanner">
            <i class="material-icons">qr_code_scanner</i>
            <span style="font-size: 12px; margin-top: 10px; color: #ff742e;">Active Monitor</span>
        </div>
    </div>

    <div class="nav">
        <div class="nav-item active">
            <i class="material-icons">home</i>
            <span class="nav-label">Home</span>
        </div>
        <div class="nav-item">
            <i class="material-icons">assignment</i>
            <span class="nav-label">Assets</span>
        </div>
        <div class="nav-item">
            <i class="material-icons">account_balance_wallet</i>
            <span class="nav-label">Ledger</span>
        </div>
        <div class="nav-item">
            <i class="material-icons">group</i>
            <span class="nav-label">Team</span>
        </div>
    </div>
    """, unsafe_allow_html=True)