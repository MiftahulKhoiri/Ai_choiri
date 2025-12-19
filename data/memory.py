import json
import os

FILE_PATH = "memory.json"

def load_memory():
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except Exception:
        return []

def save_memory(memory):
    try:
        with open(FILE_PATH, "w") as f:
            json.dump(memory, f, indent=2)
    except Exception:
        pass