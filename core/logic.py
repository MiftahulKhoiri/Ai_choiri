from ml.model import IntentModel
from core.context import ContextMemory
from utils.entity_extractor import extract_entities
from data.profile import load_profile, save_profile

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
        self.profile = load_profile()   # 🔥 memory jangka panjang

    def respond(self, user_input: str) -> str:
        self.context.add(user_input)
        context_text = self.context.get()

        intent = self.intent_model.predict(context_text)
        entities = extract_entities(context_text)

        # === SIMPAN KE PROFIL ===
        if "nama" in entities:
            self.profile["nama"] = entities["nama"]
            save_profile(self.profile)

        # === RESPON BERBASIS PROFIL ===
        if intent == "greeting":
            if "nama" in self.profile:
                return f"Halo {self.profile['nama']} 👋"
            return "Halo 👋"

        if intent == "bye":
            if "nama" in self.profile:
                return f"Sampai jumpa {self.profile['nama']} 👋"
            return "Sampai jumpa 👋"

        return RESPONSES.get(intent, RESPONSES["unknown"])