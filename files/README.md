# AI Image Studio - Streamlit UI

A modern, colorful UI for your AI image generation/processing app built with Streamlit.

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   streamlit run streamlit_ui.py
   ```

3. **Open in browser:**
   The app will automatically open at `http://localhost:8501`

## 🎨 Features

- **Modern Design**: Gradient backgrounds, smooth animations, and colorful UI elements
- **Three Modes**: 
  - Image Generation with custom prompts
  - Image Processing with various operations
  - Batch Processing for multiple images
- **Responsive Layout**: Works great on different screen sizes
- **Interactive Sidebar**: All settings and parameters in one place
- **Tabbed Interface**: Organized Create, Gallery, and History sections
- **Custom Styling**: CSS-based modern design with gradients and hover effects

## 🔧 Customization Guide

### 1. **Integrate Your AI Model**

Replace the placeholder comments with your actual AI code:

**For Image Generation** (around line 270):
```python
if generate_btn:
    with st.spinner("🎨 Creating your masterpiece..."):
        # YOUR CODE HERE
        generated_image = your_image_generation_function(prompt, style, resolution)
        
        st.success("✅ Image generated successfully!")
        st.image(generated_image, use_column_width=True)
```

**For Image Processing** (around line 305):
```python
if process_btn:
    with st.spinner(f"⚙️ Applying {operation}..."):
        # YOUR CODE HERE
        processed_image = your_image_processing_function(image, operation, strength)
        
        st.image(processed_image, use_column_width=True)
```

### 2. **Change Color Scheme**

Edit the CSS gradients in the `st.markdown()` section:

```python
# Main gradient (currently purple)
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

# Change to blue-green:
background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);

# Change to orange-red:
background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);

# Change to blue:
background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
```

### 3. **Add Your Logo**

Replace the emoji in the header:
```python
st.markdown('<h1 class="header-text">🎨 AI Image Studio</h1>', unsafe_allow_html=True)

# With an image:
st.image("your_logo.png", width=200)
st.markdown('<h1 class="header-text">AI Image Studio</h1>', unsafe_allow_html=True)
```

### 4. **Customize Operations**

Add your own image processing operations:
```python
operation = st.selectbox(
    "Operation",
    [
        "Enhance", 
        "Background Removal", 
        "Style Transfer", 
        "Upscale", 
        "Color Correction",
        # Add your operations:
        "Custom Filter 1",
        "Custom Filter 2"
    ]
)
```

### 5. **Add More Parameters**

Extend the sidebar with your specific parameters:
```python
with st.sidebar:
    # Add custom sliders
    temperature = st.slider("Temperature", 0.0, 2.0, 1.0)
    
    # Add custom number inputs
    num_images = st.number_input("Number of Images", 1, 10, 1)
    
    # Add custom checkboxes
    use_advanced = st.checkbox("Use Advanced Mode")
```

## 📦 Deployment

### Deploy to Streamlit Cloud (Free):

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy!

### Deploy to other platforms:

- **Heroku**: Use the Heroku buildpack for Python
- **AWS/GCP/Azure**: Use their app hosting services
- **Docker**: Create a Dockerfile with Streamlit

## 🎯 File Structure

```
your-project/
├── streamlit_ui.py      # Main UI file
├── requirements.txt     # Python dependencies
├── your_model.py        # Your AI model code
└── README.md           # This file
```

## 💡 Tips

1. **Performance**: For heavy processing, use `@st.cache_data` decorator
2. **Session State**: Use `st.session_state` to preserve data across reruns
3. **File Size**: Set max upload size in `.streamlit/config.toml`:
   ```toml
   [server]
   maxUploadSize = 200
   ```

## 🔗 Useful Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Components](https://streamlit.io/components)
- [Streamlit Gallery](https://streamlit.io/gallery)

## 📝 Next Steps

1. Integrate your AI model functions
2. Test with sample images
3. Customize colors and branding
4. Add image gallery storage (database/cloud)
5. Implement user authentication if needed
6. Deploy to production

---

**Need help?** Check the comments in `streamlit_ui.py` for guidance on where to add your code!
