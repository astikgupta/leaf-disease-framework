# Structured Disease-Specific Mapping Dictionary
RECOMMENDATION_DB = {
    'Early Blight': {
        'Mild': {
            'Pesticide': 'Neem oil or Copper-based preventive fungicide',
            'Dosage': '5 ml per liter of water',
            'Frequency': 'Every 10-14 days',
            'Prevention': ['Avoid overhead irrigation', 'Ensure good air circulation', 'Space plants properly']
        },
        'Moderate': {
            'Pesticide': 'Mancozeb fungicide',
            'Dosage': '2 g per liter of water',
            'Frequency': 'Every 7 days',
            'Prevention': ['Remove infected lower leaves', 'Ensure good air circulation', 'Mulch around the base']
        },
        'Severe': {
            'Pesticide': 'Chlorothalonil fungicide',
            'Dosage': '2.5 g per liter of water',
            'Frequency': 'Every 5-7 days',
            'Prevention': ['Remove heavily blighted leaves', 'Burn or deeply bury infected plant debris', 'Do not compost infected material']
        }
    },
    'Late Blight': {
        'Mild': {
            'Pesticide': 'Copper Oxychloride',
            'Dosage': '2.5 g per liter of water',
            'Frequency': 'Every 7-10 days',
            'Prevention': ['Avoid overhead irrigation', 'Water at the base of the plant', 'Eliminate volunteer plants']
        },
        'Moderate': {
            'Pesticide': 'Dimethomorph or Metalaxyl-M',
            'Dosage': '1.5 g per liter of water',
            'Frequency': 'Every 7 days',
            'Prevention': ['Alternate with contact fungicides to prevent resistance', 'Improve drainage', 'Avoid excessive nitrogen fertilization']
        },
        'Severe': {
            'Pesticide': 'Cymoxanil-based systemic fungicide',
            'Dosage': 'As per manufacturer label immediately',
            'Frequency': 'Immediate application',
            'Prevention': ['Infected plants may need to be pulled up and destroyed', 'Monitor neighboring fields', 'Use resistant varieties next season']
        }
    },
    'Leaf Spot': {
        'Mild': {
            'Pesticide': 'Neem oil',
            'Dosage': '5 ml per liter of water',
            'Frequency': 'Every 14 days',
            'Prevention': ['Prune affected leaves immediately', 'Avoid wetting foliage', 'Practice crop rotation']
        },
        'Moderate': {
            'Pesticide': 'Chlorothalonil or Copper Oxychloride',
            'Dosage': '2 g per liter of water',
            'Frequency': 'Every 7-10 days',
            'Prevention': ['Improve air circulation', 'Sanitize tools between cuts', 'Control weeds']
        },
        'Severe': {
            'Pesticide': 'Systemic fungicides (e.g. Tebuconazole, Difenoconazole)',
            'Dosage': '1 ml per liter of water',
            'Frequency': 'Every 7 days',
            'Prevention': ['Increase plant spacing', 'Apply fungicides preventatively next season', 'Ensure balanced soil nutrition']
        }
    },
    'Powdery Mildew': {
        'Mild': {
            'Pesticide': 'Potassium bicarbonate or Sulfur dust',
            'Dosage': '1 tablespoon per gallon water',
            'Frequency': 'Every 7-14 days',
            'Prevention': ['Increase sunlight exposure', 'Avoid crowding plants', 'Water early in the day']
        },
        'Moderate': {
            'Pesticide': 'Myclobutanil or Propiconazole',
            'Dosage': '1 ml per liter of water',
            'Frequency': 'Every 14 days',
            'Prevention': ['Treat the entire canopy', 'Prune to improve airflow', 'Avoid excess nitrogen']
        },
        'Severe': {
            'Pesticide': 'Azoxystrobin',
            'Dosage': 'As per manufacturer label',
            'Frequency': 'Every 7-10 days',
            'Prevention': ['Heavy pruning of infected branches required', 'Destroy fallen leaves', 'Consider resistant cultivars']
        }
    },
    'Healthy Leaf': {
        'Mild': {
            'Pesticide': 'None',
            'Dosage': 'N/A',
            'Frequency': 'N/A',
            'Prevention': ['Continue standard agronomic practices', 'Monitor regularly', 'Maintain balanced nutrition']
        },
        'Moderate': {
            'Pesticide': 'None',
            'Dosage': 'N/A',
            'Frequency': 'N/A',
            'Prevention': ['Continue standard agronomic practices', 'Monitor regularly', 'Maintain balanced nutrition']
        },
        'Severe': {
            'Pesticide': 'None',
            'Dosage': 'N/A',
            'Frequency': 'N/A',
            'Prevention': ['Continue standard agronomic practices', 'Monitor regularly', 'Maintain balanced nutrition']
        },
        'None': {
            'Pesticide': 'None',
            'Dosage': 'N/A',
            'Frequency': 'N/A',
            'Prevention': ['Continue standard agronomic practices', 'Monitor regularly', 'Maintain balanced nutrition']
        }
    }
}

def get_pesticide_recommendation(disease_name, severity_category):
    """
    Returns a structured dictionary of pesticide recommendation based on both the
    detected disease and the calculated severity category.
    """
    
    # Handle healthy classifications or fallback
    if disease_name == "Healthy Leaf" or severity_category == "None":
        return RECOMMENDATION_DB['Healthy Leaf']['None']
        
    # Look up the specific recommendation
    if disease_name in RECOMMENDATION_DB:
        if severity_category in RECOMMENDATION_DB[disease_name]:
            return RECOMMENDATION_DB[disease_name][severity_category]
            
    # Fallback if somehow a mismatch occurs
    return {
        'Pesticide': 'Unknown',
        'Dosage': 'Consult an expert',
        'Frequency': 'Consult an expert',
        'Prevention': ['General monitoring', 'Consult local agricultural extension']
    }
