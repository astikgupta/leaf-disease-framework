# Deep Learning-Based Leaf Disease Segmentation and Intelligent Severity-Guided Pesticide Recommendation Framework

## 🌿 Project Overview
This project is an intelligent **Precision Agriculture Decision-Support Tool**. It takes an image of a plant leaf, analyzes it using Deep Learning and Computer Vision, and provides a farmer with a highly specific, actionable treatment plan to save their crops.

By determining exactly **which disease** is present and calculating **how much of the leaf is infected**, the system bridges the gap between raw AI classification and practical agricultural application.

---

## ✨ Key Features
1. **Disease Detection:** Uses a PyTorch MobileNetV2 architecture to classify the exact disease (Early Blight, Late Blight, Leaf Spot, Powdery Mildew, or Healthy Leaf).
2. **Infection Segmentation:** Uses an advanced HSV (Hue, Saturation, Value) color thresholding algorithm to cleanly isolate healthy green tissue from necrotic/diseased brown and yellow tissue.
3. **Severity Calculation:** Computes the exact percentage of the leaf that is diseased and categorizes it into Mild (0-25%), Moderate (25-60%), or Severe (>60%).
4. **Precision Recommendation Engine:** Maps the specific disease and the severity level to a custom database, outputting a highly structured treatment plan (Pesticide Name, Exact Dosage, Frequency, and Prevention Tips).
5. **Educational Information Panel:** Displays the underlying cause of the disease, symptoms, spread conditions, and commonly affected crops.
6. **Disease History Tracking:** Automatically logs all analyzed leaves into a session dataframe so farmers can track their continuous analysis.
7. **Dark Mode & Dynamic UI:** Built on Streamlit, featuring an interactive layout with progress bars, visual metrics, and an integrated dark mode toggle.

---

## 🛠️ Technology Stack
- **Frontend & UI:** Streamlit
- **Deep Learning / AI:** PyTorch (`torch`, `torchvision`)
- **Computer Vision:** OpenCV (`opencv-python`)
- **Image Processing:** NumPy, Pillow
- **Data Structuring:** Pandas

---

## 📁 System Architecture & Modules

The project is modularly structured into specific functional files inside the `src/` directory, glued together by `app.py`.

### 1. `app.py` (The Main Application)
This is the Streamlit dashboard that the user interacts with. It handles file uploads, manages the session state (for the History Tracking), renders the columns, displays the segmented images side-by-side with original images, and renders the Disease Information and Treatment Plan panels.

### 2. `src/preprocessing.py` (Data Normalization)
When an image is uploaded, it is passed here first. 
- It converts the image into a standard RGB format using `OpenCV` and `Pillow`.
- It resizes the image to a standardized resolution so the AI models don't crash due to unexpected dimensions.
- Standardizes the image tensors to match PyTorch's ImageNet statistical requirements.

### 3. `src/classification.py` (Model Inference)
This module acts as the "Brain".
- It loads a `MobileNetV2` model modified to output our 5 specific disease classes.
- It processes the pre-processed leaf through the neural network pipeline.
- *Note: In the demo version, it utilizes a deterministic simulated hash to guarantee a prediction output since a multi-gigabyte PlantVillage weight file is not loaded locally.*
- It returns the **Predicted Disease String** and a **Confidence Score (%)**.

### 4. `src/segmentation.py` (Computer Vision Extractor)
This module calculates exactly where the disease is physically located on the leaf.
- It converts the RGB image to the **HSV color space**, which is vastly superior for isolating biological colors under varying lighting conditions.
- Uses morphological operations (opening/closing) to clean up noise and isolate the largest green object (the leaf itself).
- It subtracts the "healthy green" pixels from the total leaf pixels, resulting in an exact mask of the diseased spots, which is returned to the app to be highlighted in bright red.

### 5. `src/severity_analysis.py` (Quantitative Math)
- Takes the pixel counts of the `disease_mask` and divides it by the total pixel count of the `leaf_mask`.
- Multiplies by 100 to get a quantitative percentage.
- Brackets this percentage into String categories (Mild, Moderate, Severe).

### 6. `src/disease_info.py` (The Encyclopedia)
- A simple dictionary acting as a lightweight database. It maps strings like 'Early Blight' to highly researched text blocks regarding the biological cause (e.g., *Alternaria solani*), the symptoms, and what weather conditions encourage the spread.

### 7. `src/recommendation.py` (The Decision Engine)
- The final step. It takes the output from `classification.py` (e.g., Late Blight) and `severity_analysis.py` (e.g., Moderate) and looks them up in a nested dictionary matrix.
- It returns a specific JSON-like object dictating the precise chemical (e.g., Dimethomorph), dosage (1.5 g/L), and frequency.

---

## 🚀 Installation & Setup

1. **Ensure Python 3.8+ is installed** via `python.org` on your system.
2. **Navigate to the core directory:**
   ```powershell
   cd d:\leaf-disease-framework
   ```
3. **Activate the Virtual Environment:**
   *(If not created already: `python -m venv venv`)*
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
4. **Install Dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
5. **Run the Application:**
   ```powershell
   streamlit run app.py
   ```
6. The app will launch automatically in your browser at `http://localhost:8501`.
