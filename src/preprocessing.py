import cv2
import numpy as np
from PIL import Image

def preprocess_image(image_path_or_file, target_size=(256, 256)):
    """
    Loads an image, resizes it to target_size, and normalizes it.
    Can accept a file path or a file-like object (e.g., from Streamlit upload).
    """
    
    # 1. Load image
    if isinstance(image_path_or_file, str):
        img_bgr = cv2.imread(image_path_or_file)
        if img_bgr is None:
            raise ValueError(f"Could not load image at {image_path_or_file}")
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    elif isinstance(image_path_or_file, Image.Image):
        # Handle already opened PIL Image (prevents cursor reset issues)
        img_rgb = np.array(image_path_or_file.convert('RGB'))
    else:
        # Assume it's a file-like object (buffer)
        img_pil = Image.open(image_path_or_file).convert('RGB')
        img_rgb = np.array(img_pil)

    # 2. Resize
    img_resized = cv2.resize(img_rgb, target_size)
    
    # 3. Normalize for PyTorch model (if used)
    # Convert to float32 and scale to [0, 1]
    img_normalized = img_resized.astype(np.float32) / 255.0
    
    # Usually for PyTorch we need shape (C, H, W) and standard ImageNet normalization
    # but we'll return the standard normalized array here, and let the segmentation
    # module handle specific PyTorch tensor conversion if needed.
    
    return img_rgb, img_resized, img_normalized
