import torch
import torchvision.models as models
import torch.nn as nn
from PIL import Image
import torchvision.transforms as transforms
import json
import os

# Default path for weights
def get_weights_path():
    # Try multiple common locations to be robust for Streamlit/Local/Training runs
    paths = [
        os.path.join(os.getcwd(), "models", "plant_disease_model.pth"),
        os.path.join(os.path.dirname(__file__), "..", "models", "plant_disease_model.pth")
    ]
    for p in paths:
        if os.path.exists(p):
            return os.path.abspath(p)
    return os.path.abspath(paths[0]) # Return default if none exist

def get_class_names_path():
    paths = [
        os.path.join(os.getcwd(), "models", "class_names.json"),
        os.path.join(os.path.dirname(__file__), "..", "models", "class_names.json")
    ]
    for p in paths:
        if os.path.exists(p):
            return os.path.abspath(p)
    return os.path.abspath(paths[0])

_DEFAULT_WEIGHTS_PATH = get_weights_path()
_DEFAULT_CLASS_NAMES_PATH = get_class_names_path()

def _load_class_names(class_names_path=None):
    """Load class names from JSON; fall back to a basic list if not found."""
    path = class_names_path or _DEFAULT_CLASS_NAMES_PATH
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Return the 38 PlantVillage class names as fallback
        return [
            "Apple___Apple_scab", "Apple___Black_rot",
            "Apple___Cedar_apple_rust", "Apple___healthy",
            "Blueberry___healthy", "Cherry_(including_sour)___Powdery_mildew",
            "Cherry_(including_sour)___healthy",
            "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
            "Corn_(maize)___Common_rust_", "Corn_(maize)___Northern_Leaf_Blight",
            "Corn_(maize)___healthy", "Grape___Black_rot",
            "Grape___Esca_(Black_Measles)", "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
            "Grape___healthy", "Orange___Haunglongbing_(Citrus_greening)",
            "Peach___Bacterial_spot", "Peach___healthy",
            "Pepper,_bell___Bacterial_spot", "Pepper,_bell___healthy",
            "Potato___Early_blight", "Potato___Late_blight", "Potato___healthy",
            "Raspberry___healthy", "Soybean___healthy",
            "Squash___Powdery_mildew", "Strawberry___Leaf_scorch",
            "Strawberry___healthy", "Tomato___Bacterial_spot",
            "Tomato___Early_blight", "Tomato___Late_blight",
            "Tomato___Leaf_Mold", "Tomato___Septoria_leaf_spot",
            "Tomato___Spider_mites Two-spotted_spider_mite",
            "Tomato___Target_Spot",
            "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
            "Tomato___Tomato_mosaic_virus", "Tomato___healthy",
        ]


def format_class_name(raw_name: str) -> str:
    """Convert 'Tomato___Early_blight' → 'Tomato - Early Blight'."""
    parts = raw_name.split("___")
    plant = parts[0].replace("_", " ").replace(",", "").strip().title()
    disease = parts[1].replace("_", " ").strip().title() if len(parts) > 1 else ""
    if disease.lower() in ("healthy", ""):
        return f"{plant} (Healthy)"
    return f"{plant} — {disease}"


def load_classification_model(num_classes=38, weights_path=None):
    """
    Creates / loads a MobileNetV2 model for PlantVillage classification.
    If weights_path is None and the default path exists, it is used automatically.
    """
    model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
    model.classifier[1] = nn.Linear(model.last_channel, num_classes)

    # Auto-detect default weights
    effective_path = weights_path or _DEFAULT_WEIGHTS_PATH
    if os.path.exists(effective_path):
        try:
            model.load_state_dict(
                torch.load(effective_path, map_location=torch.device("cpu"))
            )
            print(f"✅ Loaded trained weights from {effective_path}")
        except Exception as e:
            print(f"⚠️  Could not load weights: {e}")
    else:
        print("⚠️  No trained weights found. Using ImageNet initialisation (predictions will be inaccurate).")
        print(f"   Expected path: {effective_path}")
        print("   Run 'python train.py' first to train the model.")

    model.eval()
    return model


def predict_disease(image_pil: Image.Image, model,
                    class_names_path=None):
    """
    Runs real inference using the trained PlantVillage model.

    Returns:
        tuple: (display_name: str, confidence_percentage: float)
               e.g. ("Tomato — Early Blight", 94.3)
    """
    class_names = _load_class_names(class_names_path)

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])

    input_tensor = transform(image_pil).unsqueeze(0)  # [1, 3, 224, 224]

    with torch.no_grad():
        outputs       = model(input_tensor)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)[0]
        confidence, predicted_idx = torch.max(probabilities, 0)

    raw_class_name  = class_names[predicted_idx.item()]
    display_name    = format_class_name(raw_class_name)
    confidence_pct  = round(confidence.item() * 100.0, 1)

    return display_name, confidence_pct, raw_class_name
