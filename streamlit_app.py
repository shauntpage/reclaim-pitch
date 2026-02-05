import streamlit as st

# Configure the page to use the full width and set the title
st.set_page_config(layout="wide", page_title="Reclaim Home")

# The HTML and CSS code must be inside a text string
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f4f6f9;
            margin: 0;
            padding: 20px 20px 100px 20px; /* Padding bottom for fixed nav */
        }

        /* Header Area */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
        }
        .user-initials {
            background: #e0e0e0;
            color: #333;
            width: 35px;
            height: 35px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 14px;
        }
        .page-title {
            font-size: 18px;
            font-weight: 600;
            color: #333;
        }

        /* Icon Grid */
        .grid {
            display: flex;
            justify-content: space-between;
            margin-bottom: 25px;
            flex-wrap: wrap; 
        }
        .icon-col {
            text-align: center;
            width: 19%; 
            margin-bottom: 10px;
        }
        .icon-box {
            height: 55px;
            width: 55px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 5px auto;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        .material-icons {
            font-size: 28px;
            color: white;
        }
        .orange { background: #ff742e; }
        .blue { background: #0e72ec; }
        
        .label {
            font-size: 10px;
            color: #666;
            margin-top: 5px;
            font-weight: 500;
        }

        /* Alert Banner */
        .banner {
            background: linear-gradient(90deg, #d32f2f, #f44336);
            border-radius: 12px;
            padding: 15px;
            color: white;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            box-shadow: 0 4px 12px rgba(211, 47, 47, 0.3);
        }
        .banner-icon {
            margin-right: 15px;
        }
        .banner-text h4 {
            margin: 0 0 5px 0;
            font-size: 16px;
            font-weight: 600;
        }
        .banner-text p {
            margin: 0;
            font-size: 12px;
            opacity: 0.9;
        }
        .banner-action {
            margin-left: auto;
            background: rgba(255,255,255,0.2);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 10px;
            white-space: nowrap;
            font-weight: bold;
            cursor: pointer;
        }

        /* Pulse Scanner Animation */
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(242, 109, 33, 0.7); }
            70% { box-shadow: 0 0 0 20px rgba(242, 109, 33, 0); }
            100% { box-shadow: 0 0 0 0 rgba(242, 109, 33, 0); }
        }
        .scanner-container {
            margin-top: 30px;
            position: relative;
            display: flex;
            justify-content: center;
        }
        .scanner {
            border: 2px solid #ff742e;
            height: 220px;
            width: 100%;
            border-radius: 20px;
            animation: pulse 2s infinite;
            display: flex;
            align-items: center;
            justify-content: center;
            background: white;
            flex-direction: column;
            color: #ff742e;
        }
        .scanner i {
            font-size: 60px;
            color: #ff742e;
            opacity: 0.8;
        }

        /* Info Text */
        .info-text {
            text-align: center;
            color: #aaa;
            font-size: 13px;
            margin: 20px 0;
        }

        /* Bottom Navigation */
        .nav {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #1a1a1a; 
            border-top: 1px solid #333;
            display: flex;
            justify-content: space-around;
            padding: 12px 0 20px 0; /* Extra padding for iOS home bar */
            z-index: 999;
        }
        .nav-item {
            color: #888;
            text-align: center;
            cursor: pointer;
            width: 25%;
        }
        .nav-item .material-icons {
            font-size: 24px;
            color: #888;
            margin-bottom: 4px;
        }
        .nav-item.active .material-icons {
            color: white;
        }
        .nav-label {
            font-size: 10px;
            color: #888;
            display: block;
        }
        .nav-item.active .nav-label {
            color: white;
        }
    </style>

    <div class="header">
        <div class="user-initials">SP</div>
        <div class="page-title">Home</div>
        <i class="material-icons" style="color: #ccc;">settings</i>
    </div>

    <div class="grid">
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
            <span style="font-size: 12px; margin-top: