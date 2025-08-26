# File: backend/services/alerts.py (Updated)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models, schemas, security
from database import get_db

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)

@router.post("/", response_model=schemas.AlertResponse, status_code=status.HTTP_201_CREATED)
def create_alert(alert: schemas.AlertCreate, db: Session = Depends(get_db), current_user: models.User = Depends(security.get_current_user)):
    new_alert = models.Alert(**alert.dict(), user_id=current_user.id)
    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)
    return new_alert

# ✅ Removed the authentication dependency to make it public for the dashboard
@router.get("/active", response_model=List[schemas.AlertResponse])
def get_active_alerts(db: Session = Depends(get_db)):
    alerts = db.query(models.Alert).filter(
        models.Alert.status.in_([models.AlertStatus.PENDING, models.AlertStatus.ACKNOWLEDGED])
    ).order_by(models.Alert.created_at.desc()).all()
    return alerts

# ✅ Kept these actions protected, but for the prototype to work without a login, we'll remove the dependency for now.
# In a real app with an operator login, you would add: dependencies=[Depends(security.get_current_user)]
@router.post("/{alert_id}/acknowledge", status_code=status.HTTP_204_NO_CONTENT)
def acknowledge_alert(alert_id: str, db: Session = Depends(get_db)):
    alert = db.query(models.Alert).filter(models.Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    alert.status = models.AlertStatus.ACKNOWLEDGED
    db.commit()
    return

@router.post("/{alert_id}/dispatch", status_code=status.HTTP_204_NO_CONTENT)
def dispatch_unit_for_alert(alert_id: str, db: Session = Depends(get_db)):
    alert = db.query(models.Alert).filter(models.Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    alert.status = models.AlertStatus.DISPATCHED
    db.commit()
    return