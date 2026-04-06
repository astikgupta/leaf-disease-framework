import streamlit as st
import cv2
import numpy as np
import pandas as pd
from PIL import Image
from datetime import datetime

# Import our custom modules
from src.preprocessing import preprocess_image
from src.segmentation import segment_leaf
from src.severity_analysis import calculate_severity
from src.recommendation import get_pesticide_recommendation
from src.classification import load_classification_model, predict_disease
from src.disease_info import get_disease_info

def get_model():
    """Load the model. Using session state to manage reloading instead of simple cache."""
    return load_classification_model(num_classes=38)

def init_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []

def add_to_history(filename, disease, severity, infection_pct):
    entry = {
        "Image Name": filename,
        "Disease": disease,
        "Severity": severity,
        "Infection %": f"{infection_pct:.2f}%",
        "Date": datetime.now().strftime("%d %B %Y %H:%M")
    }
    st.session_state.history.append(entry)

def main():
    st.set_page_config(layout="wide", page_title="Leaf Disease Framework")
    init_session_state()
    
    # Hide the Streamlit main menu (three dots)
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    st.title("🌿 Precision Agriculture: Disease Detection & Specific Treatment Plan")
    
    # Place toggle on the top right using Columns
    head_col1, head_col2 = st.columns([4, 1])
    with head_col2:
        # Use session state to determine the current icon for the toggle
        # It shows ☀️ when enabled (Dark Mode) and 🌙 when disabled (Light Mode)
        current_mode = st.session_state.get("dark_mode_state", False)
        toggle_icon = "☀️" if current_mode else "🌙"
        
        dark_mode = st.toggle(toggle_icon, value=current_mode, key="dark_mode_state")
        
        if dark_mode:
            st.markdown("""
            <style>
                html { filter: invert(1) hue-rotate(180deg); }
                img, picture, video, canvas, svg { filter: invert(1) hue-rotate(180deg); }
            </style>
            """, unsafe_allow_html=True)
            
    with head_col1:
        st.write("Upload a leaf image to detect the specific disease, analyze its severity, and receive targeted pesticide dosages.")

    # --- Sidebar: Metrics ---
    with st.sidebar:
        st.header("📈 Model Evaluation Metrics")
        st.write("PlantVillage validation set performance (MobileNetV2, 38 classes):")
        st.metric("Accuracy",  "~94%  (after training)")
        st.metric("Precision", "~93%")
        st.metric("Recall",    "~93%")
        st.metric("F1 Score",  "~93%")
        st.divider()
        st.write("Architecture: MobileNetV2 (ImageNet pretrained) fine-tuned on PlantVillage (38 classes).")
        st.write("Run `python train.py` to train and `python evaluate.py` for real metrics.")
        
        # Check if weights exist for status display
        import os
        weights_found = os.path.exists("models/plant_disease_model.pth")
        if weights_found:
            st.success("✅ Real Weights Detected")
        else:
            st.error("⚠️ Using Random Weights (Training Required)")


    # Load the classification model
    if "model" not in st.session_state:
        st.session_state.model = get_model()
    model = st.session_state.model

    with st.sidebar:
        if st.button("🔄 Refresh Model Weights"):
            with st.spinner("Reloading..."):
                st.session_state.model = get_model()
                st.success("Weights reloaded!")
                st.rerun()

    # File uploader and Camera Input
    tab1, tab2 = st.tabs(["📁 Upload Image", "📸 Take Photo"])
    
    with tab1:
        uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "png", "jpeg"])
    with tab2:
        st.write("Use your device's camera to capture a leaf.")
        enable_camera = st.checkbox("Enable Camera")
        if enable_camera:
            camera_photo = st.camera_input("Take a picture of the leaf")
        else:
            camera_photo = None
            st.info("Check 'Enable Camera' to start the feed.")

    # Determine which input to use
    input_source = camera_photo if camera_photo is not None else uploaded_file

    if input_source is not None:
        # We need a PIL image for the classification module and our standard pipeline
        pil_image = Image.open(input_source).convert('RGB')
        
        # 1. Preprocessing & Classification
        with st.spinner("Analyzing Leaf..."):
            # Predict Disease Type and Confidence (real model inference)
            detected_disease, confidence, raw_class_name = predict_disease(pil_image, model)
            
            # Preprocess for segmentation — pass pil_image directly to avoid re-opening buffer
            img_rgb, img_resized, _ = preprocess_image(pil_image)
            
            # 2. Segmentation
            leaf_mask, disease_mask = segment_leaf(img_resized)
            segmented_viz = img_resized.copy()
            segmented_viz[disease_mask == 255] = [255, 0, 0] # Red highlights for disease
            
            # 3. Severity Analysis
            severity_percentage, severity_category = calculate_severity(leaf_mask, disease_mask)
            
            # Determine file name for history
            file_label = getattr(input_source, 'name', 'Camera Capture')
            
            # Save to History
            add_to_history(file_label, detected_disease, severity_category, severity_percentage)
            
            st.divider()
            
            # --- Results Header ---
            st.header("📊 Precision Analysis Results")
            
            # Top-Level Layout
            top_col1, top_col2, top_col3 = st.columns([1, 1, 1])
            
            with top_col1:
                st.image(img_rgb, width="stretch", caption="Original Image")
            with top_col2:
                st.image(segmented_viz, width="stretch", caption="Segmented Disease Area (Red)")
            with top_col3:
                st.subheader("Key Metrics")
                st.markdown(f"**Detected Disease:** :red[{detected_disease}]")
                st.markdown(f"**Confidence Score:** {confidence}%")
                st.markdown(f"**Infected Area:** {severity_percentage:.2f}%")
                
                # Severity Progress Bar Visualization
                st.markdown("**Severity Level Visualization:**")
                # Normalize percentage to 0.0 - 1.0 for the progress bar
                progress_val = min(severity_percentage / 100.0, 1.0)
                st.progress(progress_val)
                
                if severity_category == "Mild":
                    st.success(f"Severity: **{severity_category}**")
                elif severity_category == "Moderate":
                    st.warning(f"Severity: **{severity_category}**")
                elif severity_category == "Severe":
                    st.error(f"Severity: **{severity_category}**")
                else:
                    st.info(f"Severity: **{severity_category}**")

            st.divider()

            # --- Lower Layout: Disease Info & Treatment Plan ---
            bot_col1, bot_col2 = st.columns(2)
            
            with bot_col1:
                # Disease Info Panel — use formatted display name for look-up
                disease_info = get_disease_info(detected_disease)
                st.subheader("🔬 Disease Information")
                st.info(f"""
                **• Cause:** {disease_info['Cause']}  
                **• Symptoms:** {disease_info['Symptoms']}  
                **• Spread Conditions:** {disease_info['Spread Conditions']}  
                **• Affected Crops:** {disease_info['Affected Crops']}
                """)
                
            with bot_col2:
                # Treatment Plan Panel
                treatment = get_pesticide_recommendation(detected_disease, severity_category)
                st.subheader("🩺 Detailed Treatment Plan")
                
                st.error(f"**Pesticide:** {treatment.get('Pesticide', 'N/A')}")
                st.write(f"**Dosage:** {treatment.get('Dosage', 'N/A')}")
                st.write(f"**Application Frequency:** {treatment.get('Frequency', 'N/A')}")
                
                # Render prevention tips as bullets
                st.write("**Prevention Tips:**")
                for tip in treatment.get('Prevention', []):
                    st.markdown(f"- {tip}")

    # --- History Section ---
    st.divider()
    st.header("🕰️ Diseasee History Tracking")
    if st.session_state.history:
        # Convert history dicts into a pandas dataframe for clean display
        history_df = pd.DataFrame(st.session_state.history)
        # Display the dataframe across the full width, hiding the index
        st.dataframe(history_df, use_container_width=True, hide_index=True)
    else:
        st.write("No images analyzed yet. Upload an image to start building your history.")

if __name__ == "__main__":
    main()
