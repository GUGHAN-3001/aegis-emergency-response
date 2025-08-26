# File: backend/services/ml_models.py (Updated)

from fastapi import APIRouter
import schemas
from ml_logic import risk_model
import random

router = APIRouter(
    prefix="/ml",
    tags=["Machine Learning Models"]
)

# ✅ Removed the authentication dependency to make it public for the dashboard
@router.get("/risk", response_model=schemas.RiskResponse)
def get_risk_assessment(lat: float, lon: float):
    risk_input = risk_model.RiskInput(latitude=lat, longitude=lon)
    return risk_model.get_risk_prediction(risk_input)

# ✅ Removed the authentication dependency to make it public for the dashboard
@router.get("/route-prediction", response_model=schemas.RoutePrediction)
def get_route_prediction(lat: float, lon: float):
    eta = random.randint(8, 25)
    distance = round(eta * 0.6, 1)
    major_roads = ["Anna Salai", "Poonamallee High Road", "Sardar Patel Road", "GST Road"]
    route_summary = f"Via {random.choice(major_roads)}, avoiding known congestion."
    return {"eta_minutes": eta, "route_summary": route_summary, "distance_km": distance}
