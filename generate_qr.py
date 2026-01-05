import json, qrcode, os

BASE = "https://charudatta10.github.io/forensic-fathers-library/people"

with open("data/people.json") as f:
    people = json.load(f)

os.makedirs("qr", exist_ok=True)

for p in people:
    url = f"{BASE}/{p['slug']}/"
    img = qrcode.make(url)
    img.save(f"qr/{p['slug']}.png")
