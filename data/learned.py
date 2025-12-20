import json
from pathlib import Path

FILE = Path("data/learned.json")

def load_learned():
    return json.loads(FILE.read_text())

def save_learned(data):
    FILE.write_text(json.dumps(data, indent=2))

def add_suggestion(text, intent, score):
    data = load_learned()
    data.setdefault("suggested", [])
    data["suggested"].append({
        "text": text,
        "suggested_intent": intent,
        "confidence": round(score, 2)
    })
    save_learned(data)