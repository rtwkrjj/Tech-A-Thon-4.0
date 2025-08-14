# Counterfeit Drug Detection & Verification System

A secure, cloud-native solution to detect and prevent counterfeit medicines by integrating with global drug databases, enabling real-time verification, and providing supply chain transparency.  
Developed as part of **Tech-A-Thon 4.0**.

---

## 📜 Problem Statement
Counterfeit drugs are a growing global threat to public health and safety.  
This system verifies medicine authenticity through cryptographically signed QR/DataMatrix codes, integrates with regulators like **WHO, FDA, and EMA**, and provides tracking from manufacturing to dispensing.

---

## 🚀 Features
- **International Drug Database Integration** – Verified data from WHO, FDA, EMA.
- **Scalable Cloud-Native Infrastructure** – Built on AWS/Azure/GCP for global deployment.
- **Real-Time Verification** – Mobile app & API to scan and validate medicines.
- **Track & Trace** – Full supply chain visibility.
- **Modular Design** – Easily add features like patient apps, AI analytics, multilingual support.

---

## 🛠️ Tech Stack :
- **Architecture:** Web based client -> flask API -> JSON (simulated blockchain )
- **Frontend:** Html, CSS , JavaScript 
- **Backend:** Python Flask
- **Database:** JSON Database (drug_data_extended.json) 
- **Voice:** Hindi output using pyttsx3
- **QR Genarator:** Auto generates QR codes on startupt for drug IDs.   


---

## 📦 Installation
```bash
# Clone the repository
git clone https://github.com/<your-username>/Tech-A-Thon-4.0.git
cd Tech-A-Thon-4.0

# Install backend dependencies
cd backend
pip install -r requirements.txt   # or npm install for Node backend

# Install frontend dependencies
cd ../frontend
npm install

# Run backend
cd backend
uvicorn main:app --reload   # or npm start for Node

# Run frontend
cd ../frontend





npm start

📸 Usage

Scan the QR/DataMatrix code on the medicine package using the mobile app.

App verifies code authenticity offline & online.

Receive verification status (Genuine / Suspected / Expired).

Track product movement through supply chain dashboard.

📈 Impact

Protects public health by reducing fake drug circulation.

Builds trust among consumers, manufacturers, and regulators.

Enables global-scale monitoring and analytics.

🔮 Future Scope

Blockchain integration for immutable tracking.

AI-powered predictive analytics for counterfeit detection.

Expansion to cover medical devices and vaccines.

🤝 Contributors

Your Team Name – BUG BOUNTERS
Team Members - Ritwik Raj | Roshan Kumar Gupta | Riyanshu Gupta |
