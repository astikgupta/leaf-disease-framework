# Disease Information Dictionary

DISEASE_INFO = {
    'Early Blight': {
        'Cause': 'Alternaria solani (Fungus)',
        'Symptoms': 'Dark, concentric rings or lesions on older leaves, stem cankers, and fruit rot.',
        'Spread Conditions': 'High humidity, warm temperatures, and prolonged periods of leaf wetness.',
        'Affected Crops': 'Tomato, Potato, Eggplant, Pepper'
    },
    'Late Blight': {
        'Cause': 'Phytophthora infestans (Oomycete)',
        'Symptoms': 'Dark, water-soaked lesions on leaves and stems; whitish mold under leaves in humid conditions.',
        'Spread Conditions': 'High humidity (above 90%) and cool-to-moderate temperatures (60-70°F).',
        'Affected Crops': 'Tomato, Potato'
    },
    'Leaf Spot': {
        'Cause': 'Various fungi (e.g., Septoria, Cercospora) or bacteria (e.g., Xanthomonas)',
        'Symptoms': 'Small, circular brown or black spots with lighter centers; heavily infected leaves may turn yellow and drop prematurely.',
        'Spread Conditions': 'Frequent rainfall, overhead irrigation, and warm temperatures.',
        'Affected Crops': 'Many vegetables (e.g., Tomato, Strawberry, Spinaches) and ornamentals'
    },
    'Powdery Mildew': {
        'Cause': 'Various fungal species (e.g., Erysiphaceae family)',
        'Symptoms': 'White, powdery fungal patches on the upper and lower surfaces of leaves, stems, and sometimes fruit.',
        'Spread Conditions': 'Warm, dry weather with high relative humidity, especially in crowded plantings.',
        'Affected Crops': 'Squash, Cucumber, Melon, Grape, Rose'
    },
    'Healthy Leaf': {
        'Cause': 'N/A',
        'Symptoms': 'Uniform green color, no visible spots, necrotic tissue, or fungal growth.',
        'Spread Conditions': 'Optimal environmental conditions provided.',
        'Affected Crops': 'All crops'
    }
}

def get_disease_info(disease_name):
    """
    Returns the educational information for a given disease.
    """
    return DISEASE_INFO.get(disease_name, {
        'Cause': 'Unknown',
        'Symptoms': 'Unknown',
        'Spread Conditions': 'Unknown',
        'Affected Crops': 'Unknown'
    })
