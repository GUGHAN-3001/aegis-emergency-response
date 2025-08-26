### 🛡️ Aegis: AI-Powered Emergency Response Platform
Aegis is a mobile-first, real-time emergency management and risk prediction platform designed for urban environments. It connects citizens facing emergencies directly with authority dispatch centers, using an intelligent risk model to prioritize alerts and streamline the response process.

### 📝 Table of Contents
Key Features

App Architecture

Getting Started

Contributing

License

### ✨ Key Features
### Real-time Alerts & Dashboard: 
The platform provides a live, centralized dashboard for authorities to view incoming alerts on an interactive map. New alerts appear instantly without needing to refresh the page.

### Proactive Risk Prediction: 
A rule-based machine learning model analyzes each alert based on location (flood-prone zones in Chennai) and user vulnerability status (e.g., elderly, visually impaired). This generates a risk level (High, Medium, Low) that helps authorities prioritize critical situations.

### Intuitive Citizen Interface: 
A simple, mobile-friendly interface allows citizens to quickly send an alert with just a few taps, providing essential information to responders instantly.

### Secure & Scalable Backend: 
Built on Firebase, the application uses a robust, serverless backend that handles authentication and real-time data efficiently, ensuring reliable performance even under high load.

### 🏗️ App Architecture
The application follows a client-server architecture, with the client (the web app) communicating directly with the Firebase backend. This allows for a fast, responsive, and highly scalable application.

# Client (Frontend)
The entire application logic and user interface are contained within a single HTML file, making it a true single-page application (SPA).

HTML, CSS, & JavaScript: The user interface is built with standard web technologies, styled with Tailwind CSS for a clean, modern look. The JavaScript handles all the app's logic, from user authentication to real-time rendering.

Local Risk Model: The risk prediction logic is embedded directly in the frontend, eliminating the need for a separate backend server and allowing the app to run on Firebase's free Spark plan.

# Backend (Firebase)
The backend is entirely serverless, powered by Google's Firebase services.

Firebase Hosting: Deploys the frontend web application to a live URL.

Firebase Authentication: Handles all user sign-in and sign-up processes, managing both citizen and authority accounts securely.

Cloud Firestore: Serves as the real-time database, storing all user data and emergency alerts.

# Data Flow:
A citizen's alert is sent directly from the frontend to Firestore. The authority dashboard, which is constantly listening to the Firestore database, receives the new alert in real time and updates the map and queue automatically.

# 🚀 Getting Started
To run this project, you need to have Node.js and the Firebase CLI installed.

# Clone the repository:

git clone https://github.com/GUGHAN-3001/aegis-emergency-response.git
cd aegis-emergency-response

# Initialize Firebase:

firebase init

Follow the prompts to connect your project to Firebase and select Hosting. When prompted for the public directory, enter frontend.

# Deploy to Live URL:

firebase deploy --only hosting

After deployment, the terminal will provide a live URL for your application.

# 🤝 Contributing
We welcome contributions! If you would like to help improve this project, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m 'feat: Add new feature').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

# 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
