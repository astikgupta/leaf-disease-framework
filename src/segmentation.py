import cv2
import numpy as np

def segment_leaf(image_rgb):
    """
    Segments a leaf image to find the leaf area and the infected area.
    Because we don't have a pretrained U-Net for PlantVillage, we use 
    HSV color thresholding as a robust baseline for leaf disease segmentation.
    
    Returns:
        leaf_mask (np.array): Mask of the entire leaf (healthy + infected).
        disease_mask (np.array): Mask of only the infected/diseased areas.
    """
    
    # Convert to HSV color space for better color segmentation
    hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
    
    # 1. Segment the Entire Leaf (Healthy + Diseased) vs Background
    # Most PlantVillage backgrounds are light gray/white/black.
    # We look for green, yellow, brown, and dark spots (typical of leaves and disease).
    
    # Lower bound: Hue 20 (brown/yellowish), Sat 30, Val 30
    # Upper bound: Hue 90 (green), Sat 255, Val 255
    lower_leaf = np.array([20, 25, 25])
    upper_leaf = np.array([100, 255, 255])
    
    leaf_mask = cv2.inRange(hsv, lower_leaf, upper_leaf)
    
    # Clean up the mask using morphological operations
    kernel_large = np.ones((7,7), np.uint8)
    leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_CLOSE, kernel_large)
    leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    
    # Keep only the largest connected component (assuming the leaf is the largest object)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(leaf_mask, connectivity=8)
    if num_labels > 1:
        # Index 0 is background, so we find the max area from index 1 onwards
        largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
        leaf_mask = np.zeros_like(leaf_mask)
        leaf_mask[labels == largest_label] = 255
        
    # 2. Segment the Diseased Area
    # Diseased areas are typically yellow, brown, or black spots on the green leaf.
    # Therefore, we can find healthy green areas, and subtract them from the total leaf.
    
    # Define "healthy green" range
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])
    
    healthy_mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # The diseased area is the part of the leaf that is NOT healthy green
    disease_mask = cv2.bitwise_and(leaf_mask, cv2.bitwise_not(healthy_mask))
    
    # Optional: Clean up tiny noise in the disease mask
    kernel_small = np.ones((3,3), np.uint8)
    disease_mask = cv2.morphologyEx(disease_mask, cv2.MORPH_OPEN, kernel_small)
    
    return leaf_mask, disease_mask
