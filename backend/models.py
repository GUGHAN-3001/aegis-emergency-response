# File: backend/models.py

from sqlalchemy import Column, String, Integer, Float, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import uuid
import enum
from datetime import datetime
from database import Base

class VulnerabilityStatus(str, enum.Enum):
    NONE = "NONE"
    WHEELCHAIR = "WHEELCHAIR"
    VISUALLY_IMPAIRED = "VISUALLY_IMPAIRED"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    ELDERLY = "ELDERLY"

class AlertType(str, enum.Enum):
    FLOOD = "FLOOD"
    FIRE = "FIRE"
    MEDICAL = "MEDICAL"
    STRUCTURE_COLLAPSE = "STRUCTURE_COLLAPSE"

class AlertStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACKNOWLEDGED = "ACKNOWLEDGED"
    DISPATCHED = "DISPATCHED"
    RESOLVED = "RESOLVED"
    FALSE_ALARM = "FALSE_ALARM"

class UserRole(str, enum.Enum):
    CITIZEN = "citizen"
    OPERATOR = "operator"
    SUPERVISOR = "supervisor"

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    phone_number = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    vulnerability_status = Column(Enum(VulnerabilityStatus), default=VulnerabilityStatus.NONE)
    default_floor_level = Column(Integer, default=0)
    role = Column(Enum(UserRole), default=UserRole.CITIZEN, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    alerts = relationship("Alert", back_populates="user")

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    alert_type = Column(Enum(AlertType), nullable=False)
    status = Column(Enum(AlertStatus), default=AlertStatus.PENDING)
    details = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="alerts")