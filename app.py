from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS
import json, os, qrcode
from datetime import datetime
import pyttsx3

app = Flask(__name__, 
            template_folder='../frontend/templates', 
            static_folder='../frontend/static',
            static_url_path='')
CORS(app)

# Load drug data
with open("drug_data_extended.json") as f:
    blockchain_data = json.load(f)

# Generate QR codes (runs once at startup)
def generate_qr_codes():
    os.makedirs("../frontend/static/qrcodes", exist_ok=True)
    for drug_id in blockchain_data.keys():
        img_path = f"../frontend/static/qrcodes/{drug_id}.png"
        if not os.path.exists(img_path):  # Skip if already exists
            img = qrcode.make(drug_id)
            img.save(img_path)
    print("✅ QR Codes generated in static/qrcodes")

generate_qr_codes()

# Serve the main index.html
@app.route("/")
def home():
    return send_from_directory('../frontend', 'index.html')

# Serve static files
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../frontend', path)

# Route 1 - Form-based verification (renders result page with Hindi voice via JS)
@app.route("/verify", methods=["POST"])
def verify():
    tag_id = request.form["tag_id"].strip().upper()
    drug = blockchain_data.get(tag_id)

    expired = False
    if drug:
        expiry_date = datetime.strptime(drug["expiry"], "%Y-%m-%d")
        expired = datetime.now() > expiry_date

    return render_template(
        "result.html",
        tag_id=tag_id,
        drug=drug,
        expired=expired
    )

# Route 2 - Simple API check for authenticity
@app.route("/verify_basic/<drug_id>")
def verify_basic(drug_id):
    drug = blockchain_data.get(drug_id.upper())
    return jsonify({"valid": drug["authentic"]}) if drug else jsonify({"valid": False})

# Route 3 - API with pyttsx3 Hindi voice output (server-side)
def speak_hindi(message):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(message)
    engine.runAndWait()

@app.route("/verify_voice/<drug_id>")
def verify_voice(drug_id):
    tag_id = drug_id.strip().upper()
    drug = blockchain_data.get(tag_id)

    if drug:
        expiry_date = datetime.strptime(drug["expiry"], "%Y-%m-%d")
        expired = datetime.now() > expiry_date

        if not drug["authentic"]:
            msg = "यह दवा नकली है। कृपया इसका उपयोग न करें।"
        elif expired:
            msg = "दवा की समय सीमा समाप्त हो चुकी है। कृपया उपयोग न करें।"
        else:
            msg = "दवा मान्य है। आप इसे सुरक्षित रूप से ले सकते हैं।"

        speak_hindi(msg)
        return jsonify({"valid": drug["authentic"], "expired": expired, "message": msg})
    else:
        msg = "यह दवा अमान्य है। कृपया डॉक्टर से संपर्क करें।"
        speak_hindi(msg)
        return jsonify({"valid": False, "expired": None, "message": msg})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)