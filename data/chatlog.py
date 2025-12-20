import json
from pathlib import Path

FILE = Path("data/chatlog.json")

def log_chat(user, intent):
    data = json.loads(FILE.read_text())
    data.append({
        "user": user,
        "intent": intent
    })
    FILE.write_text(json.dumps(data, indent=2))