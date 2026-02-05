import streamlit as st
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="AI Image Studio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern, colorful design
st.markdown("""
    <style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Custom container styling */
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Header styling */
    .header-text {
        background: linear-gradient(120deg, #667eea, #764ba2, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .subheader-text {
        color: #6b7280;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        border-radius: 50px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Sidebar styling */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .css-1d391kg .sidebar-content, [data-testid="stSidebar"] .sidebar-content {
        color: white;
    }
    
    /* Input field styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e5e7eb;
        padding: 0.75rem;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Card styling */
    .image-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .image-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* Metric styling */
    .stMetric {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
    }
    
    /* File uploader styling */
    .stFileUploader > div {
        border: 2px dashed #667eea;
        border-radius: 15px;
        padding: 2rem;
        background: #f9fafb;
        transition: all 0.3s ease;
    }
    
    .stFileUploader > div:hover {
        border-color: #764ba2;
        background: #f3f4f6;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #f3f4f6;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Success/Info boxes */
    .stSuccess, .stInfo {
        border-radius: 10px;
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="header-text">🎨 AI Image Studio</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader-text">Transform your ideas into stunning visuals</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    
    # Mode selection
    mode = st.radio(
        "Select Mode",
        ["Generate Image", "Process Image", "Batch Processing"],
        help="Choose your workflow"
    )
    
    st.markdown("---")
    
    # Common settings
    st.markdown("### 🎛️ Parameters")
    
    if mode == "Generate Image":
        style = st.selectbox(
            "Art Style",
            ["Realistic", "Abstract", "Cartoon", "Oil Painting", "Watercolor", "Digital Art"]
        )
        
        quality = st.select_slider(
            "Quality",
            options=["Draft", "Standard", "High", "Ultra"],
            value="High"
        )
        
        resolution = st.selectbox(
            "Resolution",
            ["512x512", "768x768", "1024x1024", "1024x1792"]
        )
        
    elif mode == "Process Image":
        operation = st.selectbox(
            "Operation",
            ["Enhance", "Background Removal", "Style Transfer", "Upscale", "Color Correction"]
        )
        
        strength = st.slider("Effect Strength", 0.0, 1.0, 0.7)
    
    st.markdown("---")
    
    # Advanced settings in expander
    with st.expander("🔧 Advanced Options"):
        seed = st.number_input("Random Seed", value=42, help="For reproducible results")
        steps = st.slider("Processing Steps", 10, 100, 50)
    
    st.markdown("---")
    st.markdown("### 📊 Usage")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Images", "24", "+3")
    with col2:
        st.metric("Credits", "76", "-4")

# Main content area
tab1, tab2, tab3 = st.tabs(["🎨 Create", "🖼️ Gallery", "📝 History"])

with tab1:
    if mode == "Generate Image":
        # Text input for prompt
        col1, col2 = st.columns([2, 1])
        
        with col1:
            prompt = st.text_area(
                "Enter your prompt",
                placeholder="Describe the image you want to generate...\nExample: A serene mountain landscape at sunset with vibrant colors",
                height=120
            )
        
        with col2:
            negative_prompt = st.text_area(
                "Negative prompt (optional)",
                placeholder="What to avoid...\nExample: blurry, low quality",
                height=120
            )
        
        # Generate button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            generate_btn = st.button("✨ Generate Image", use_container_width=True)
        
        if generate_btn:
            with st.spinner("🎨 Creating your masterpiece..."):
                # Placeholder for your image generation logic
                st.success("✅ Image generated successfully!")
                
                # Display results in a nice layout
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown('<div class="image-card">', unsafe_allow_html=True)
                    st.markdown("#### Generated Image")
                    # Replace this with your actual generated image
                    st.info("Your generated image will appear here")
                    # st.image(generated_image, use_column_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col2:
                    st.markdown('<div class="image-card">', unsafe_allow_html=True)
                    st.markdown("#### Image Details")
                    st.write(f"**Prompt:** {prompt}")
                    st.write(f"**Style:** {style}")
                    st.write(f"**Resolution:** {resolution}")
                    st.write(f"**Quality:** {quality}")
                    
                    # Download buttons
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.button("💾 Save", use_container_width=True)
                    with col_b:
                        st.button("🔄 Regenerate", use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
    
    elif mode == "Process Image":
        # File uploader
        uploaded_file = st.file_uploader(
            "Upload an image",
            type=["jpg", "jpeg", "png", "webp"],
            help="Drag and drop or click to upload"
        )
        
        if uploaded_file:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<div class="image-card">', unsafe_allow_html=True)
                st.markdown("#### Original Image")
                image = Image.open(uploaded_file)
                st.image(image, use_column_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="image-card">', unsafe_allow_html=True)
                st.markdown("#### Processed Image")
                
                process_btn = st.button("🚀 Process Image", use_container_width=True)
                
                if process_btn:
                    with st.spinner(f"⚙️ Applying {operation}..."):
                        # Placeholder for your image processing logic
                        st.success(f"✅ {operation} applied successfully!")
                        st.info("Processed image will appear here")
                        # st.image(processed_image, use_column_width=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
    
    else:  # Batch Processing
        st.markdown("### 📦 Batch Upload")
        uploaded_files = st.file_uploader(
            "Upload multiple images",
            type=["jpg", "jpeg", "png", "webp"],
            accept_multiple_files=True
        )
        
        if uploaded_files:
            st.write(f"📊 **{len(uploaded_files)} images uploaded**")
            
            col1, col2 = st.columns([1, 3])
            with col1:
                process_all = st.button("⚡ Process All", use_container_width=True)
            
            if process_all:
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for idx, file in enumerate(uploaded_files):
                    progress = (idx + 1) / len(uploaded_files)
                    progress_bar.progress(progress)
                    status_text.text(f"Processing {idx + 1}/{len(uploaded_files)}: {file.name}")
                
                st.success(f"✅ All {len(uploaded_files)} images processed!")
            
            # Display thumbnails
            cols = st.columns(4)
            for idx, file in enumerate(uploaded_files):
                with cols[idx % 4]:
                    st.image(Image.open(file), caption=file.name, use_column_width=True)

with tab2:
    st.markdown("### 🖼️ Your Gallery")
    
    # Sample gallery (replace with your actual images)
    col1, col2, col3 = st.columns(3)
    
    for i, col in enumerate([col1, col2, col3]):
        with col:
            st.markdown('<div class="image-card">', unsafe_allow_html=True)
            st.info(f"Gallery Image {i+1}")
            st.caption("Generated 2 hours ago")
            st.button("🔍 View", key=f"view_{i}", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown("### 📝 Recent Activity")
    
    # Activity timeline
    activities = [
        {"time": "2 hours ago", "action": "Generated", "prompt": "Mountain landscape at sunset"},
        {"time": "5 hours ago", "action": "Processed", "prompt": "Enhanced portrait image"},
        {"time": "1 day ago", "action": "Generated", "prompt": "Abstract geometric pattern"},
    ]
    
    for activity in activities:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{activity['action']}:** {activity['prompt']}")
                st.caption(f"🕒 {activity['time']}")
            with col2:
                st.button("↩️ Reuse", key=activity['time'], use_container_width=True)
        st.markdown("---")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Need help?** Check out our [Documentation](#)")
with col2:
    st.markdown("**Have feedback?** [Contact us](#)")
with col3:
    st.markdown("**Version:** 1.0.0")
