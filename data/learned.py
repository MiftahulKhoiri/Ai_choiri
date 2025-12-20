import json
from pathlib import Path

FILE = Path("data/learned.json")

def load_learned():
    return json.loads(FILE.read_text())

def save_learned(data):
    FILE.write_text(json.dumps(data, indent=2))