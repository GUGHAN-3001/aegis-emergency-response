# File: backend/schemas.py

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime
from models import VulnerabilityStatus, AlertType, AlertStatus, UserRole

class UserCreate(BaseModel):
    phone_number: str
    password: str
    full_name: str
    vulnerability_status: VulnerabilityStatus = VulnerabilityStatus.NONE
    default_floor_level: int = 0

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    phone_number: str
    full_name: str
    vulnerability_status: VulnerabilityStatus
    role: UserRole
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class AlertCreate(BaseModel):
    latitude: float = Field(..., example=13.0827)
    longitude: float = Field(..., example=80.2707)
    alert_type: AlertType
    details: Optional[str] = None

class AlertResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    user_id: str
    latitude: float
    longitude: float
    alert_type: AlertType
    status: AlertStatus
    details: Optional[str]
    created_at: datetime
    user: UserResponse

class RiskResponse(BaseModel):
    risk_level: str
    confidence: float
    reason: str

class RoutePrediction(BaseModel):
    eta_minutes: int
    route_summary: str
    distance_km: float