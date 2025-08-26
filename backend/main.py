# File: backend/main.py

import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# This adds the project's root directory (backend) to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import engine
import models
from services import users, alerts, mlmodels

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Aegis Emergency Response Platform API",
    description="This is the central backend for the Aegis project.",
    version="1.0.0",
)

# --- CORRECTED CORS SETTINGS ---
# Using a wildcard allows requests from any origin.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- END OF CORRECTION ---

app.include_router(users.router)
app.include_router(alerts.router)
app.include_router(mlmodels.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Aegis API. Visit /docs for API documentation."}