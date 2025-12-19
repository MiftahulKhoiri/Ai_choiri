from ml.model import IntentModel
from core.context import ContextMemory
from utils.entity_extractor import extract_entities

RESPONSES = {
    "greeting": "Halo juga 👋",
    "bye": "Sampai jumpa 👋",
    "python": "Python itu bahasa yang keren 🐍",
    "creator_python": "Python dibuat oleh Guido van Rossum 👨‍💻",
    "unknown": "Aku masih belajar 🤖"
}

class SimpleAI:
    def __init__(self, dataset):
        self.intent_model = IntentModel(dataset)
        self.context = ContextMemory()

    def respond(self, user_input: str) -> str:
    self.context.add(user_input)
    context_text = self.context.get()

    intent = self.intent_model.predict(context_text)
    entities = extract_entities(context_text)

    # === CONTOH LOGIC BERBASIS ENTITY ===

    if intent == "greeting" and "nama" in entities:
        return f"Halo {entities['nama']} 👋"

    if intent == "tanya_waktu" and "waktu" in entities:
        return f"Kamu menyebut waktu: {', '.join(entities['waktu'])}"

    return RESPONSES.get(intent, RESPONSES["unknown"])