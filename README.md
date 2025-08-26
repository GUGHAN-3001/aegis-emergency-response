# Aegis: AI-Powered Emergency Response Platform

Aegis is an intelligent, multi-agent AI platform designed to make emergency response in cities faster, more equitable, and more resilient. It features a Python (FastAPI) backend and two web-based frontends (a Citizen App and an Authority Dashboard).

## Key Features
- **Proactive Risk Prediction:** Uses an XGBoost model to forecast flood risk in real-time.
- **Intelligent Dispatch & Routing:** Employs a Deep Q-Network (DQN) to find the genuinely fastest and safest routes for responders.
- **Resilient Offline Communication:** A built-in Bluetooth Low Energy (BLE) mesh network allows citizens to send SOS alerts even when all cellular networks fail.
- **Post-Crisis Analytics:** Uses DBSCAN clustering to identify disaster hotspots from historical data, helping to build more climate-resilient cities.
