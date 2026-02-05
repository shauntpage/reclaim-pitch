<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reclaim Home Dashboard</title>
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
            width: 19%; /* Adjusted slightly to fit 5 items if needed, or wrap */
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
            70% { box-shadow: 0 0 0 20px rgba(242, 109, 33