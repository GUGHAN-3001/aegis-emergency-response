# Aegis Emergency Platform
Aegis is a modern emergency platform designed to connect citizens in distress with local authorities in real-time. The application provides a simple, mobile-friendly interface for citizens to report emergencies and a comprehensive dashboard for authorities to manage and respond to live alerts.

# Key Features
### Citizen-Facing Mobile App: 
A responsive interface for users to report various types of emergencies with a single tap.

### Real-time Risk Prediction: 
The platform assesses a user's local risk level based on their location and declared vulnerability status, helping authorities prioritize alerts.

### Authority Command Center: 
A secure, live dashboard that provides a centralized view of all active alerts, complete with mapping, triage, and alert details.

### User Authentication: 
Secure sign-in and sign-up flows for both citizens and authorized personnel.

### Real-time Data Visualization: 
Alerts are displayed on a live map, allowing authorities to visualize and respond to incidents efficiently.

# Tech Stack
### Frontend:

HTML, CSS (Tailwind CSS)

JavaScript

### Backend & Database:

Firebase Authentication for user management

Firestore for real-time, NoSQL data storage

### Mapping:

Google Maps JavaScript API

# Setup and Installation
To run this project, you will need to set up a Firebase project and obtain a Google Maps API key.

### Step 1: Firebase Project Setup
Go to the Firebase Console and create a new project.

In your project, go to Authentication and enable Email/Password sign-in.

Navigate to Firestore Database and create a new database. Start in "production mode."

In the project settings, add a web app to your Firebase project. Copy the firebaseConfig object provided.

### Step 2: Google Maps API Key
Go to the Google Cloud Console.

Create a new project or select an existing one.

Enable the Maps JavaScript API.

Create a new API key under "Credentials." You may want to restrict the key for security.

### Step 3: Update the Code
Open the index.html file.

Replace the placeholder Firebase configuration with your own firebaseConfig object from Step 1.

```
// --- PASTE YOUR FIREBASE CONFIGURATION HERE ---
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_SENDER_ID",
    appId: "YOUR_APP_ID",
    measurementId: "YOUR_MEASUREMENT_ID"
};
// -----------------------------------------


Replace the placeholder Google Maps API key in the <script> tag with your own key from Step 2.

<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY&callback=initApp" async defer></script>
```

### Step 4: Add an Authority User (for testing)
For the authority dashboard to be accessible, you must manually add a user to your Firebase users collection with the role field set to 'authority'.

Register a new user in the citizen app.

In your Firebase Console, navigate to Firestore Database and find the new user document in the users collection.

Edit the document to add a new field: role with the value authority.

# How to Use
### Citizen App: 
Simply open the index.html file in a web browser. Register a new account, log in, and press the "SOS" button to send an alert.

### Authority Dashboard: 
Log in with the account you have granted 'authority' permissions to in Firebase. You will be automatically redirected to the command center.