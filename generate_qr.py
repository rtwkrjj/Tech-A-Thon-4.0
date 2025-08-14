import qrcode
import os

data_list = ["DRUG1234", "DRUG5678", "FAKE0001"]

os.makedirs("static/qrcodes", exist_ok=True)

for drug_id in data_list:
    img = qrcode.make(drug_id)
    img.save(f"static/qrcodes/{drug_id}.png")

print("QR Codes generated")