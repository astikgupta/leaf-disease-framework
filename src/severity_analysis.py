import numpy as np

def calculate_severity(leaf_mask, disease_mask):
    """
    Calculates the severity of the disease based on the ratio of diseased area to total leaf area.
    
    Args:
        leaf_mask (np.array): A binary mask where 255 indicates the leaf area, 0 otherwise.
        disease_mask (np.array): A binary mask where 255 indicates the diseased area, 0 otherwise.
        
    Returns:
        severity_percentage (float): The percentage of the leaf area that is diseased.
        severity_category (str): The category of severity ('Mild', 'Moderate', 'Severe').
    """
    
    leaf_area = np.count_nonzero(leaf_mask)
    disease_area = np.count_nonzero(disease_mask)
    
    if leaf_area == 0:
        return 0.0, "None"
        
    severity_percentage = (disease_area / leaf_area) * 100
    
    if severity_percentage <= 25:
        severity_category = "Mild"
    elif severity_percentage <= 60:
        severity_category = "Moderate"
    else:
        severity_category = "Severe"
        
    return float(severity_percentage), severity_category
