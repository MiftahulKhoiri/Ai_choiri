import json
from pathlib import Path

FILE = Path("data/chatlog.json")
FILE.touch(exist_ok=True)

def log_chat(user, intent):
    try:
        data = json.loads(FILE.read_text() or "[]")
    except json.JSONDecodeError:
        data = []

    data.append({"user": user, "intent": intent})
    FILE.write_text(json.dumps(data, indent=2))