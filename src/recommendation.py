"""
recommendation.py  —  Treatment recommendations for all 38 PlantVillage classes.
Keys are the formatted display names returned by classification.format_class_name().
"""


def _healthy_entry():
    return {
        "Mild":     {"Pesticide": "No treatment needed", "Dosage": "—", "Frequency": "—",
                     "Prevention": ["Maintain balanced fertilisation", "Monitor regularly for early signs of disease"]},
        "Moderate": {"Pesticide": "No treatment needed", "Dosage": "—", "Frequency": "—",
                     "Prevention": ["Continue regular monitoring"]},
        "Severe":   {"Pesticide": "No treatment needed", "Dosage": "—", "Frequency": "—",
                     "Prevention": ["Continue regular monitoring"]},
    }


RECOMMENDATIONS = {
    # ─── APPLE ───
    "Apple — Apple Scab": {
        "Mild":     {"Pesticide": "Captan 50 WP",       "Dosage": "2.5 g/L water",  "Frequency": "Every 10 days",
                     "Prevention": ["Remove fallen leaves", "Prune for air circulation", "Use resistant varieties"]},
        "Moderate": {"Pesticide": "Myclobutanil",       "Dosage": "1.5 mL/L water", "Frequency": "Every 7–10 days",
                     "Prevention": ["Rake and destroy fallen leaves", "Apply protective sprays at green tip"]},
        "Severe":   {"Pesticide": "Mancozeb + Systemic fungicide", "Dosage": "3 g/L water", "Frequency": "Every 5–7 days",
                     "Prevention": ["Remove severely infected tissue", "Replant with scab-resistant varieties if repeated"]},
    },
    "Apple — Black Rot": {
        "Mild":     {"Pesticide": "Captan 80 WDG",      "Dosage": "2 g/L water",    "Frequency": "Every 14 days",
                     "Prevention": ["Remove mummified fruit", "Prune dead wood"]},
        "Moderate": {"Pesticide": "Thiophanate-methyl", "Dosage": "1 g/L water",    "Frequency": "Every 10 days",
                     "Prevention": ["Disinfect pruning tools", "Remove infected bark cankers"]},
        "Severe":   {"Pesticide": "Mancozeb + Copper",  "Dosage": "3 g/L water",    "Frequency": "Every 7 days",
                     "Prevention": ["Destroy heavily infected branches", "Improve drainage"]},
    },
    "Apple — Cedar Apple Rust": {
        "Mild":     {"Pesticide": "Myclobutanil",       "Dosage": "1 mL/L water",   "Frequency": "Every 10 days from pink stage",
                     "Prevention": ["Remove nearby juniper/cedar trees if possible", "Plant resistant varieties"]},
        "Moderate": {"Pesticide": "Trifloxystrobin",    "Dosage": "0.5 mL/L water", "Frequency": "Every 7–10 days",
                     "Prevention": ["Apply during infection periods (wet spring weather)"]},
        "Severe":   {"Pesticide": "Myclobutanil + Mancozeb", "Dosage": "2 g/L water", "Frequency": "Every 7 days",
                     "Prevention": ["Eliminate cedar/juniper host plants within 500m if feasible"]},
    },
    "Apple (Healthy)":       _healthy_entry(),
    "Blueberry (Healthy)":   _healthy_entry(),
    "Raspberry (Healthy)":   _healthy_entry(),
    "Soybean (Healthy)":     _healthy_entry(),
    "Strawberry (Healthy)":  _healthy_entry(),
    "Cherry (Including Sour) — Powdery Mildew": {
        "Mild":     {"Pesticide": "Wettable sulphur",  "Dosage": "2 g/L water",  "Frequency": "Every 14 days",
                     "Prevention": ["Avoid overhead irrigation", "Prune for air circulation"]},
        "Moderate": {"Pesticide": "Myclobutanil",      "Dosage": "1 mL/L water", "Frequency": "Every 10 days",
                     "Prevention": ["Remove infected shoots promptly"]},
        "Severe":   {"Pesticide": "Tebuconazole",      "Dosage": "1 mL/L water", "Frequency": "Every 7 days",
                     "Prevention": ["Do not compost infected material"]},
    },
    "Cherry (Including Sour) (Healthy)": _healthy_entry(),
    "Corn (Maize) — Cercospora Leaf Spot Gray Leaf Spot": {
        "Mild":     {"Pesticide": "Azoxystrobin",       "Dosage": "1 mL/L water",   "Frequency": "At first sign; repeat after 14 days",
                     "Prevention": ["Rotate with non-host crops", "Use resistant hybrids", "Reduce residue"]},
        "Moderate": {"Pesticide": "Propiconazole",      "Dosage": "1 mL/L water",   "Frequency": "Every 10–14 days",
                     "Prevention": ["Minimum tillage to reduce inoculum", "Proper spacing for airflow"]},
        "Severe":   {"Pesticide": "Azoxystrobin + Propiconazole","Dosage": "1.5 mL/L water","Frequency": "Every 7–10 days",
                     "Prevention": ["Rotate crops for 2+ years", "Destroy infected residue"]},
    },
    "Corn (Maize) — Common Rust ": {
        "Mild":     {"Pesticide": "Mancozeb 75 WP",     "Dosage": "2.5 g/L water",  "Frequency": "At first sign; every 14 days",
                     "Prevention": ["Plant resistant hybrids", "Early planting"]},
        "Moderate": {"Pesticide": "Propiconazole",      "Dosage": "1 mL/L water",   "Frequency": "Every 10 days",
                     "Prevention": ["Scout regularly from V6 stage"]},
        "Severe":   {"Pesticide": "Tebuconazole + Trifloxystrobin","Dosage": "1.5 mL/L water","Frequency": "Every 7 days",
                     "Prevention": ["Use certified rust-resistant varieties next season"]},
    },
    "Corn (Maize) — Northern Leaf Blight": {
        "Mild":     {"Pesticide": "Azoxystrobin 23 SC", "Dosage": "1 mL/L water",   "Frequency": "Every 14 days",
                     "Prevention": ["Use resistant hybrids", "Crop rotation"]},
        "Moderate": {"Pesticide": "Propiconazole",      "Dosage": "1 mL/L water",   "Frequency": "Every 10 days",
                     "Prevention": ["Bury or remove crop residue after harvest"]},
        "Severe":   {"Pesticide": "Mancozeb + Carbendazim","Dosage": "2 g/L water", "Frequency": "Every 7 days",
                     "Prevention": ["Replant resistant hybrid next season"]},
    },
    "Corn (Maize) (Healthy)": _healthy_entry(),
    "Grape — Black Rot": {
        "Mild":     {"Pesticide": "Mancozeb 75 WP",     "Dosage": "2.5 g/L water",  "Frequency": "Every 10–14 days",
                     "Prevention": ["Remove mummified berries", "Prune infected canes"]},
        "Moderate": {"Pesticide": "Myclobutanil",       "Dosage": "1.5 mL/L water", "Frequency": "Every 7–10 days",
                     "Prevention": ["Keep vine canopy open", "Remove infected fruit clusters"]},
        "Severe":   {"Pesticide": "Tebuconazole + Captan","Dosage": "2 g/L water",  "Frequency": "Every 7 days",
                     "Prevention": ["Destroy all infected material; do not compost"]},
    },
    "Grape — Esca (Black Measles)": {
        "Mild":     {"Pesticide": "Topsin-M wound sealant paste", "Dosage": "Apply to all cut surfaces","Frequency": "Every pruning season",
                     "Prevention": ["Paint pruning wounds with sealant", "Avoid large cuts"]},
        "Moderate": {"Pesticide": "Topsin-M wound sealant paste", "Dosage": "Apply to all cut surfaces","Frequency": "Every pruning season",
                     "Prevention": ["Remove infected wood", "Sterilise pruning tools between vines"]},
        "Severe":   {"Pesticide": "Uprooting may be necessary", "Dosage": "—","Frequency": "—",
                     "Prevention": ["Replace with certified disease-free planting material"]},
    },
    "Grape — Leaf Blight (Isariopsis Leaf Spot)": {
        "Mild":     {"Pesticide": "Copper-based fungicide","Dosage": "2.5 g/L water","Frequency": "Every 14 days",
                     "Prevention": ["Improve canopy ventilation", "Avoid overhead watering"]},
        "Moderate": {"Pesticide": "Mancozeb 75 WP",       "Dosage": "2 g/L water",  "Frequency": "Every 10 days",
                     "Prevention": ["Remove fallen infected leaves"]},
        "Severe":   {"Pesticide": "Propiconazole",         "Dosage": "1 mL/L water", "Frequency": "Every 7 days",
                     "Prevention": ["Reduce canopy density; improve airflow"]},
    },
    "Grape (Healthy)": _healthy_entry(),
    "Orange — Haunglongbing (Citrus Greening)": {
        "Mild":     {"Pesticide": "Imidacloprid (for psyllid vector control)","Dosage": "0.5 mL/L water","Frequency": "Every 3 months",
                     "Prevention": ["Control Asian citrus psyllid", "Use certified disease-free budwood"]},
        "Moderate": {"Pesticide": "Thiamethoxam + Oxytetracycline injection","Dosage": "Per label for trunk injection","Frequency": "Twice yearly",
                     "Prevention": ["Remove and destroy symptomatic trees to prevent spread"]},
        "Severe":   {"Pesticide": "Tree removal recommended","Dosage": "—","Frequency": "—",
                     "Prevention": ["HLB is incurable — remove infected trees", "Replant with HLB-tolerant varieties"]},
    },
    "Peach — Bacterial Spot": {
        "Mild":     {"Pesticide": "Copper hydroxide (Kocide)","Dosage": "3 g/L water","Frequency": "Every 10 days",
                     "Prevention": ["Apply copper sprays at leaf drop", "Plant windbreaks"]},
        "Moderate": {"Pesticide": "Oxytetracycline",         "Dosage": "1 g/L water", "Frequency": "Every 7 days",
                     "Prevention": ["Avoid overhead irrigation", "Space plants for air circulation"]},
        "Severe":   {"Pesticide": "Copper + Mancozeb",       "Dosage": "2 g/L water", "Frequency": "Every 5–7 days",
                     "Prevention": ["Remove severely damaged leaves and shoots"]},
    },
    "Peach (Healthy)": _healthy_entry(),
    "Pepper — Bacterial Spot": {
        "Mild":     {"Pesticide": "Copper oxychloride 50 WP","Dosage": "2.5 g/L water","Frequency": "Every 10 days",
                     "Prevention": ["Use certified disease-free seed", "Avoid working in wet fields"]},
        "Moderate": {"Pesticide": "Copper hydroxide",        "Dosage": "2 g/L water",  "Frequency": "Every 7 days",
                     "Prevention": ["Crop rotation; avoid planting pepper after tomato"]},
        "Severe":   {"Pesticide": "Copper + Mancozeb",       "Dosage": "3 g/L water",  "Frequency": "Every 5 days",
                     "Prevention": ["Remove and destroy all infected plant material"]},
    },
    "Pepper (Healthy)": _healthy_entry(),
    "Potato — Early Blight": {
        "Mild":     {"Pesticide": "Mancozeb 75 WP",         "Dosage": "2 g/L water",  "Frequency": "Every 7–10 days",
                     "Prevention": ["Remove lower infected leaves", "Ensure adequate K nutrition"]},
        "Moderate": {"Pesticide": "Chlorothalonil 75 WP",   "Dosage": "2 g/L water",  "Frequency": "Every 7 days",
                     "Prevention": ["Use certified seed tubers", "Rotate with non-solanaceous crops"]},
        "Severe":   {"Pesticide": "Azoxystrobin + Mancozeb","Dosage": "2 g/L water",  "Frequency": "Every 5–7 days",
                     "Prevention": ["Destroy crop debris after harvest"]},
    },
    "Potato — Late Blight": {
        "Mild":     {"Pesticide": "Metalaxyl-M + Mancozeb (Ridomil Gold)","Dosage": "2.5 g/L water","Frequency": "Every 7 days",
                     "Prevention": ["Use certified blight-free seed", "Hill up soil around stems"]},
        "Moderate": {"Pesticide": "Cymoxanil + Mancozeb (Curzate M)","Dosage": "2 g/L water","Frequency": "Every 5–7 days",
                     "Prevention": ["Destroy volunteer potatoes", "Monitor weather for blight conditions"]},
        "Severe":   {"Pesticide": "Fluopicolide + Propamocarb (Infinito)","Dosage": "1.5 mL/L water","Frequency": "Every 5 days",
                     "Prevention": ["Defoliate and destroy haulm before harvest", "Store tubers dry and cool"]},
    },
    "Potato (Healthy)": _healthy_entry(),
    "Squash — Powdery Mildew": {
        "Mild":     {"Pesticide": "Wettable sulphur 80 WP", "Dosage": "2 g/L water", "Frequency": "Every 7–10 days",
                     "Prevention": ["Avoid excess nitrogen", "Improve spacing for airflow"]},
        "Moderate": {"Pesticide": "Myclobutanil 10 WP",     "Dosage": "1 g/L water", "Frequency": "Every 7 days",
                     "Prevention": ["Remove infected leaves", "Apply potassium bicarbonate as alternative"]},
        "Severe":   {"Pesticide": "Tebuconazole + Sulphur", "Dosage": "1.5 g/L water","Frequency": "Every 5–7 days",
                     "Prevention": ["Eliminate high-humidity conditions in greenhouse"]},
    },
    "Strawberry — Leaf Scorch": {
        "Mild":     {"Pesticide": "Captan 80 WDG",           "Dosage": "2 g/L water", "Frequency": "Every 10–14 days",
                     "Prevention": ["Remove older infected leaves", "Avoid overhead irrigation"]},
        "Moderate": {"Pesticide": "Myclobutanil",            "Dosage": "1 mL/L water","Frequency": "Every 10 days",
                     "Prevention": ["Use drip irrigation", "Mulch to reduce rain splash"]},
        "Severe":   {"Pesticide": "Tebuconazole + Captan",   "Dosage": "2 g/L water", "Frequency": "Every 7 days",
                     "Prevention": ["Remove heavily infected plants"]},
    },
    "Tomato — Bacterial Spot": {
        "Mild":     {"Pesticide": "Copper oxychloride 50 WP","Dosage": "2.5 g/L water","Frequency": "Every 10 days",
                     "Prevention": ["Use disease-free seed", "Avoid working in wet conditions"]},
        "Moderate": {"Pesticide": "Copper hydroxide",        "Dosage": "2 g/L water",  "Frequency": "Every 7 days",
                     "Prevention": ["Rotate crops; avoid solanaceous crops in same plot"]},
        "Severe":   {"Pesticide": "Copper + Mancozeb",       "Dosage": "3 g/L water",  "Frequency": "Every 5 days",
                     "Prevention": ["Destroy all infected plants; sanitise tools"]},
    },
    "Tomato — Early Blight": {
        "Mild":     {"Pesticide": "Mancozeb 75 WP",          "Dosage": "2 g/L water",  "Frequency": "Every 7 days",
                     "Prevention": ["Remove lower infected leaves", "Mulch around plants"]},
        "Moderate": {"Pesticide": "Chlorothalonil + Copper", "Dosage": "2 g/L water",  "Frequency": "Every 7 days",
                     "Prevention": ["Stake plants to improve airflow", "Rotate crops annually"]},
        "Severe":   {"Pesticide": "Azoxystrobin + Mancozeb", "Dosage": "2.5 g/L water","Frequency": "Every 5–7 days",
                     "Prevention": ["Destroy crop residues; deep plough after harvest"]},
    },
    "Tomato — Late Blight": {
        "Mild":     {"Pesticide": "Metalaxyl-M 4% + Mancozeb 64% (Ridomil Gold)","Dosage": "2.5 g/L water","Frequency": "Every 7 days",
                     "Prevention": ["Avoid overhead irrigation", "Plant resistant varieties"]},
        "Moderate": {"Pesticide": "Cymoxanil 8% + Mancozeb 64%","Dosage": "2 g/L water","Frequency": "Every 5–7 days",
                     "Prevention": ["Remove lower leaves; avoid wetting foliage"]},
        "Severe":   {"Pesticide": "Fluopicolide + Propamocarb","Dosage": "1.5 mL/L water","Frequency": "Every 5 days",
                     "Prevention": ["Remove and destroy all infected material", "Do not compost — burn or bury deep"]},
    },
    "Tomato — Leaf Mold": {
        "Mild":     {"Pesticide": "Chlorothalonil 75 WP",    "Dosage": "2 g/L water",  "Frequency": "Every 10 days",
                     "Prevention": ["Reduce greenhouse humidity below 85%", "Improve ventilation"]},
        "Moderate": {"Pesticide": "Mancozeb + Copper",       "Dosage": "2.5 g/L water","Frequency": "Every 7 days",
                     "Prevention": ["Remove infected leaves", "Avoid wetting leaves"]},
        "Severe":   {"Pesticide": "Tebuconazole",            "Dosage": "1 mL/L water", "Frequency": "Every 5–7 days",
                     "Prevention": ["Sanitise greenhouse surfaces; reduce humidity"]},
    },
    "Tomato — Septoria Leaf Spot": {
        "Mild":     {"Pesticide": "Mancozeb 75 WP",          "Dosage": "2 g/L water",  "Frequency": "Every 7–10 days",
                     "Prevention": ["Remove oldest lower leaves", "Avoid rain splash with mulch"]},
        "Moderate": {"Pesticide": "Chlorothalonil",          "Dosage": "2.5 g/L water","Frequency": "Every 7 days",
                     "Prevention": ["Stake and prune to improve air circulation"]},
        "Severe":   {"Pesticide": "Azoxystrobin + Chlorothalonil","Dosage": "2 g/L water","Frequency": "Every 5–7 days",
                     "Prevention": ["Rotate with non-solanaceous crops for 2 years"]},
    },
    "Tomato — Spider Mites Two-Spotted Spider Mite": {
        "Mild":     {"Pesticide": "Neem oil / Insecticidal soap","Dosage": "5 mL/L water","Frequency": "Every 5–7 days",
                     "Prevention": ["Increase humidity", "Introduce predatory mites"]},
        "Moderate": {"Pesticide": "Abamectin 1.9 EC",           "Dosage": "0.5 mL/L water","Frequency": "Every 5 days",
                     "Prevention": ["Remove heavily infested leaves", "Avoid dusty conditions"]},
        "Severe":   {"Pesticide": "Spiromesifen / Hexythiazox",  "Dosage": "1 mL/L water","Frequency": "Every 3–5 days — rotate mode of action",
                     "Prevention": ["Do not use pyrethroid insecticides (causes mite flare-up)"]},
    },
    "Tomato — Target Spot": {
        "Mild":     {"Pesticide": "Chlorothalonil 75 WP",    "Dosage": "2 g/L water",  "Frequency": "Every 10 days",
                     "Prevention": ["Prune low leaves", "Avoid overhead irrigation"]},
        "Moderate": {"Pesticide": "Azoxystrobin",            "Dosage": "1 mL/L water", "Frequency": "Every 7 days",
                     "Prevention": ["Remove and destroy infected leaves"]},
        "Severe":   {"Pesticide": "Tebuconazole + Mancozeb", "Dosage": "2 g/L water",  "Frequency": "Every 5–7 days",
                     "Prevention": ["Destroy residue after harvest; rotate crops"]},
    },
    "Tomato — Tomato Yellow Leaf Curl Virus": {
        "Mild":     {"Pesticide": "Imidacloprid (whitefly vector control)","Dosage": "0.5 mL/L water","Frequency": "Every 7 days",
                     "Prevention": ["Use reflective silver mulch", "Install yellow sticky traps"]},
        "Moderate": {"Pesticide": "Thiamethoxam 25 WG",      "Dosage": "0.3 g/L water","Frequency": "Every 7 days",
                     "Prevention": ["Remove and destroy infected plants", "Use virus-resistant tomato varieties"]},
        "Severe":   {"Pesticide": "Remove infected plants + whitefly control","Dosage": "—","Frequency": "—",
                     "Prevention": ["TYLCV is incurable — remove infected plants immediately"]},
    },
    "Tomato — Tomato Mosaic Virus": {
        "Mild":     {"Pesticide": "No effective chemical cure","Dosage": "—","Frequency": "—",
                     "Prevention": ["Wash hands before handling plants", "Disinfect tools with 10% bleach solution"]},
        "Moderate": {"Pesticide": "Remove infected plants",  "Dosage": "—","Frequency": "—",
                     "Prevention": ["Use certified virus-free seed"]},
        "Severe":   {"Pesticide": "Destroy infected crop",   "Dosage": "—","Frequency": "—",
                     "Prevention": ["Plant resistant varieties", "Do not smoke near plants — tobacco carries ToMV"]},
    },
    "Tomato (Healthy)": _healthy_entry(),
}

_DEFAULT_REC = {
    "Mild": {
        "Pesticide": "Copper-based fungicide",
        "Dosage": "2.5 g/L water",
        "Frequency": "Every 10 days",
        "Prevention": ["Monitor regularly", "Ensure good air circulation", "Remove infected material"],
    },
    "Moderate": {
        "Pesticide": "Mancozeb 75 WP",
        "Dosage": "2.5 g/L water",
        "Frequency": "Every 7 days",
        "Prevention": ["Remove infected leaves", "Improve drainage", "Rotate crops next season"],
    },
    "Severe": {
        "Pesticide": "Contact + Systemic fungicide combo",
        "Dosage": "3 g/L water",
        "Frequency": "Every 5–7 days",
        "Prevention": ["Destroy heavily infected plants", "Sanitise tools", "Consult local agronomist"],
    },
}


def get_pesticide_recommendation(disease_name: str, severity: str) -> dict:
    """
    Returns treatment recommendation for a given disease + severity level.
    disease_name: formatted display name e.g. 'Tomato — Early Blight'
    severity: 'Mild' | 'Moderate' | 'Severe' | 'None'
    """
    severity_key = severity if severity in ("Mild", "Moderate", "Severe") else "Moderate"

    if disease_name in RECOMMENDATIONS:
        return RECOMMENDATIONS[disease_name].get(severity_key, _DEFAULT_REC[severity_key])

    lower = disease_name.lower()
    for key, val in RECOMMENDATIONS.items():
        if key.lower() == lower:
            return val.get(severity_key, _DEFAULT_REC[severity_key])

    return _DEFAULT_REC[severity_key]
