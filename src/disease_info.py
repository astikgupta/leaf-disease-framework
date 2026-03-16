"""
disease_info.py  —  Disease information for all 38 PlantVillage classes.
Keys are the formatted display names returned by classification.format_class_name().
"""

DISEASE_INFO = {
    # ────────── APPLE ──────────
    "Apple — Apple Scab": {
        "Cause": "Fungus (Venturia inaequalis)",
        "Symptoms": "Olive-green to black scabby lesions on leaves and fruit",
        "Spread Conditions": "Cool, moist spring weather; rain splash",
        "Affected Crops": "Apple",
    },
    "Apple — Black Rot": {
        "Cause": "Fungus (Botryosphaeria obtusa)",
        "Symptoms": "Circular brown leaf spots; rotting fruit with black concentric rings",
        "Spread Conditions": "Warm humid weather; wind-dispersed spores",
        "Affected Crops": "Apple",
    },
    "Apple — Cedar Apple Rust": {
        "Cause": "Fungus (Gymnosporangium juniperi-virginianae) — requires cedar host",
        "Symptoms": "Yellow-orange spots on upper leaf surface; tube-like lesions underneath",
        "Spread Conditions": "Spring rains; requires both apple and cedar/juniper hosts nearby",
        "Affected Crops": "Apple",
    },
    "Apple (Healthy)": {
        "Cause": "N/A",
        "Symptoms": "No disease symptoms observed",
        "Spread Conditions": "N/A",
        "Affected Crops": "Apple",
    },

    # ────────── BLUEBERRY ──────────
    "Blueberry (Healthy)": {
        "Cause": "N/A",
        "Symptoms": "No disease symptoms observed",
        "Spread Conditions": "N/A",
        "Affected Crops": "Blueberry",
    },

    # ────────── CHERRY ──────────
    "Cherry (Including Sour) — Powdery Mildew": {
        "Cause": "Fungus (Podosphaera clandestina)",
        "Symptoms": "White powdery coating on leaves; leaf curling and distortion",
        "Spread Conditions": "Warm dry days, cool humid nights; wind-dispersed spores",
        "Affected Crops": "Cherry",
    },
    "Cherry (Including Sour) (Healthy)": {
        "Cause": "N/A",
        "Symptoms": "No disease symptoms observed",
        "Spread Conditions": "N/A",
        "Affected Crops": "Cherry",
    },

    # ────────── CORN ──────────
    "Corn (Maize) — Cercospora Leaf Spot Gray Leaf Spot": {
        "Cause": "Fungus (Cercospora zeae-maydis)",
        "Symptoms": "Rectangular grey-tan lesions parallel to leaf veins",
        "Spread Conditions": "High humidity, >12 hrs leaf wetness, warm temperatures",
        "Affected Crops": "Corn (Maize)",
    },
    "Corn (Maize) — Common Rust ": {
        "Cause": "Fungus (Puccinia sorghi)",
        "Symptoms": "Small reddish-brown pustules scattered on both leaf surfaces",
        "Spread Conditions": "Cool temperatures (60–77°F), high humidity; wind-dispersed spores",
        "Affected Crops": "Corn (Maize)",
    },
    "Corn (Maize) — Northern Leaf Blight": {
        "Cause": "Fungus (Exserohilum turcicum)",
        "Symptoms": "Long cigar-shaped grey-green lesions on leaves",
        "Spread Conditions": "Moderate temperatures, extended leaf wetness; wind and rain splash",
        "Affected Crops": "Corn (Maize)",
    },
    "Corn (Maize) (Healthy)": {
        "Cause": "N/A",
        "Symptoms": "No disease symptoms observed",
        "Spread Conditions": "N/A",
        "Affected Crops": "Corn (Maize)",
    },

    # ────────── GRAPE ──────────
    "Grape — Black Rot": {
        "Cause": "Fungus (Guignardia bidwellii)",
        "Symptoms": "Tan-brown circular leaf spots with dark border; shrivelled mummified berries",
        "Spread Conditions": "Warm rainy weather during bloom; rain dispersed spores",
        "Affected Crops": "Grape",
    },
    "Grape — Esca (Black Measles)": {
        "Cause": "Complex of wood-rotting fungi (Phaeomoniella, Phaeoacremonium, etc.)",
        "Symptoms": "Tiger-stripe pattern on leaves; black spots on berries; internal wood decay",
        "Spread Conditions": "Infection through pruning wounds; stressed vines",
        "Affected Crops": "Grape",
    },
    "Grape — Leaf Blight (Isariopsis Leaf Spot)": {
        "Cause": "Fungus (Pseudocercospora vitis)",
        "Symptoms": "Dark brown angular spots on upper leaf surface; defoliation",
        "Spread Conditions": "Warm humid conditions; rain splash",
        "Affected Crops": "Grape",
    },
    "Grape (Healthy)": {
        "Cause": "N/A",
        "Symptoms": "No disease symptoms observed",
        "Spread Conditions": "N/A",
        "Affected Crops": "Grape",
    },

    # ────────── ORANGE ──────────
    "Orange — Haunglongbing (Citrus Greening)": {
        "Cause": "Bacterium (Candidatus Liberibacter asiaticus), spread by Asian citrus psyllid",
        "Symptoms": "Yellowing of shoots; blotchy mottled leaves; small lopsided bitter fruit",
        "Spread Conditions": "Spread by insect vector (psyllid); incurable bacterial disease",
        "Affected Crops": "Orange, Citrus",
    },

    # ────────── PEACH ──────────
    "Peach — Bacterial Spot": {
        "Cause": "Bacterium (Xanthomonas arboricola pv. pruni)",
        "Symptoms": "Small water-soaked spots turning brown/purple on leaves; cracking fruit",
        "Spread Conditions": "Warm, rainy, windy weather; rain splash and wind dispersal",
        "Affected Crops": "Peach, Nectarine, Plum",
    },
    "Peach (Healthy)": {
        "Cause": "N/A",
        "Symptoms": "No disease symptoms observed",
        "Spread Conditions": "N/A",
        "Affected Crops": "Peach",
    },

    # ────────── PEPPER ──────────
    "Pepper — Bacterial Spot": {
        "Cause": "Bacterium (Xanthomonas campestris pv. vesicatoria)",
        "Symptoms": "Small water-soaked spots turning brown with yellow halos on leaves",
        "Spread Conditions": "Warm temperatures (75–86°F), rain splash, high humidity",
        "Affected Crops": "Pepper (Bell, Chili)",
    },
    "Pepper (Healthy)": {
        "Cause": "N/A",
        "Symptoms": "No disease symptoms observed",
        "Spread Conditions": "N/A",
        "Affected Crops": "Pepper",
    },

    # ────────── POTATO ──────────
    "Potato — Early Blight": {
        "Cause": "Fungus (Alternaria solani)",
        "Symptoms": "Dark brown target-like spots with concentric rings on lower leaves",
        "Spread Conditions": "Warm temperatures (75–84°F), wet conditions; spores spread by wind and rain",
        "Affected Crops": "Potato, Tomato",
    },
    "Potato — Late Blight": {
        "Cause": "Oomycete (Phytophthora infestans)",
        "Symptoms": "Water-soaked lesions turning brown-black rapidly; white mould beneath leaf",
        "Spread Conditions": "Cool and wet weather; rapidly spreads in humid conditions",
        "Affected Crops": "Potato, Tomato",
    },
    "Potato (Healthy)": {
        "Cause": "N/A",
        "Symptoms": "No disease symptoms observed",
        "Spread Conditions": "N/A",
        "Affected Crops": "Potato",
    },

    # ────────── RASPBERRY / SOYBEAN / SQUASH / STRAWBERRY ──────────
    "Raspberry (Healthy)": {
        "Cause": "N/A",
        "Symptoms": "No disease symptoms observed",
        "Spread Conditions": "N/A",
        "Affected Crops": "Raspberry",
    },
    "Soybean (Healthy)": {
        "Cause": "N/A",
        "Symptoms": "No disease symptoms observed",
        "Spread Conditions": "N/A",
        "Affected Crops": "Soybean",
    },
    "Squash — Powdery Mildew": {
        "Cause": "Fungus (Podosphaera xanthii / Erysiphe cichoracearum)",
        "Symptoms": "White powdery patches on leaves; yellowing and wilting",
        "Spread Conditions": "Warm dry days, cool nights; wind-dispersed spores",
        "Affected Crops": "Squash, Cucumber, Pumpkin",
    },
    "Strawberry — Leaf Scorch": {
        "Cause": "Fungus (Diplocarpon earlianum)",
        "Symptoms": "Irregular purple-red spots; centres turn grey, leaf dies and scorches",
        "Spread Conditions": "Wet conditions, overhead irrigation, warm spring weather",
        "Affected Crops": "Strawberry",
    },
    "Strawberry (Healthy)": {
        "Cause": "N/A",
        "Symptoms": "No disease symptoms observed",
        "Spread Conditions": "N/A",
        "Affected Crops": "Strawberry",
    },

    # ────────── TOMATO ──────────
    "Tomato — Bacterial Spot": {
        "Cause": "Bacterium (Xanthomonas spp.)",
        "Symptoms": "Small dark spots on leaves and fruit with water-soaked margins",
        "Spread Conditions": "Warm, wet weather; rain splash, contaminated tools",
        "Affected Crops": "Tomato, Pepper",
    },
    "Tomato — Early Blight": {
        "Cause": "Fungus (Alternaria solani)",
        "Symptoms": "Dark concentric ring spots on older/lower leaves; premature defoliation",
        "Spread Conditions": "Warm temperatures, prolonged leaf wetness; wind and rain",
        "Affected Crops": "Tomato, Potato",
    },
    "Tomato — Late Blight": {
        "Cause": "Oomycete (Phytophthora infestans)",
        "Symptoms": "Large water-soaked greasy spots turning brown-black; white mould in humidity",
        "Spread Conditions": "Cool, wet, foggy weather; very rapid spread",
        "Affected Crops": "Tomato, Potato",
    },
    "Tomato — Leaf Mold": {
        "Cause": "Fungus (Passalora fulva)",
        "Symptoms": "Yellow patches on upper leaf; olive-green to grey mould on underside",
        "Spread Conditions": "High humidity (>85%), poor air circulation; greenhouse crops",
        "Affected Crops": "Tomato",
    },
    "Tomato — Septoria Leaf Spot": {
        "Cause": "Fungus (Septoria lycopersici)",
        "Symptoms": "Circular dark-bordered spots with lighter centres and dark pycnidia",
        "Spread Conditions": "Warm wet weather; rain splash, infected plant debris",
        "Affected Crops": "Tomato",
    },
    "Tomato — Spider Mites Two-Spotted Spider Mite": {
        "Cause": "Pest mite (Tetranychus urticae)",
        "Symptoms": "Fine stippling/silvering on leaves; webbing on undersides; bronze appearance",
        "Spread Conditions": "Hot, dry conditions; spreads by wind, workers, infested plants",
        "Affected Crops": "Tomato, Pepper, Cucumber",
    },
    "Tomato — Target Spot": {
        "Cause": "Fungus (Corynespora cassiicola)",
        "Symptoms": "Brown lesions with concentric rings (target pattern); defoliation",
        "Spread Conditions": "Warm humid conditions; rain splash",
        "Affected Crops": "Tomato",
    },
    "Tomato — Tomato Yellow Leaf Curl Virus": {
        "Cause": "Begomovirus (TYLCV), spread by whitefly (Bemisia tabaci)",
        "Symptoms": "Upward curling yellowed leaves; stunted growth; low yield",
        "Spread Conditions": "Warm seasons; spread by whitefly vector",
        "Affected Crops": "Tomato",
    },
    "Tomato — Tomato Mosaic Virus": {
        "Cause": "Tobamovirus (ToMV)",
        "Symptoms": "Mosaic pattern of light and dark green; leaf distortion; stunting",
        "Spread Conditions": "Seed-borne; mechanical spread by workers and tools",
        "Affected Crops": "Tomato, Pepper",
    },
    "Tomato (Healthy)": {
        "Cause": "N/A",
        "Symptoms": "No disease symptoms observed",
        "Spread Conditions": "N/A",
        "Affected Crops": "Tomato",
    },
}

_DEFAULT_INFO = {
    "Cause": "Under investigation",
    "Symptoms": "Consult a local agronomist for detailed assessment",
    "Spread Conditions": "Variable — depends on pathogen type",
    "Affected Crops": "Multiple crops may be affected",
}


def get_disease_info(disease_name: str) -> dict:
    """
    Returns disease info dict for a given formatted disease name.
    Performs a case-insensitive partial match if exact key not found.
    """
    # Exact match
    if disease_name in DISEASE_INFO:
        return DISEASE_INFO[disease_name]

    # Partial / case-insensitive match
    lower = disease_name.lower()
    for key, val in DISEASE_INFO.items():
        if key.lower() == lower:
            return val

    return _DEFAULT_INFO
