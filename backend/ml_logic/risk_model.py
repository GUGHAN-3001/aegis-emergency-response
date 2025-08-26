from pydantic import BaseModel

class RiskInput(BaseModel):
    latitude: float
    longitude: float

HIGH_RISK_ZONES = [
    {"name": "Velachery", "lat_range": (12.97, 12.99), "lon_range": (80.21, 80.23)},
    {"name": "T. Nagar", "lat_range": (13.03, 13.05), "lon_range": (80.22, 80.24)},
    {"name": "Adyar", "lat_range": (13.00, 13.02), "lon_range": (80.25, 80.27)},
]

MEDIUM_RISK_ZONES = [
    {"name": "Mylapore", "lat_range": (13.02, 13.04), "lon_range": (80.26, 80.28)},
    {"name": "Guindy", "lat_range": (13.00, 13.02), "lon_range": (80.21, 80.23)},
]

def get_risk_prediction(risk_input: RiskInput) -> dict:
    lat, lon = risk_input.latitude, risk_input.longitude
    for zone in HIGH_RISK_ZONES:
        if (zone["lat_range"][0] <= lat <= zone["lat_range"][1]) and \
           (zone["lon_range"][0] <= lon <= zone["lon_range"][1]):
            return {"risk_level": "High", "confidence": 0.92, "reason": f"In high-risk zone: {zone['name']}."}
    for zone in MEDIUM_RISK_ZONES:
        if (zone["lat_range"][0] <= lat <= zone["lat_range"][1]) and \
           (zone["lon_range"][0] <= lon <= zone["lon_range"][1]):
            return {"risk_level": "Medium", "confidence": 0.85, "reason": f"In medium-risk zone: {zone['name']}."}
    return {"risk_level": "Low", "confidence": 0.95, "reason": "Not in a known high/medium risk zone."}