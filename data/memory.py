import json
import os

FILE = "memory.json"

def load_memory():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

def save_memory(memory):
    try:
        with open(FILE, "w") as f:
            json.dump(memory, f, indent=2)
    except Exception:
        pass

def clear_memory():
    save_memory([])