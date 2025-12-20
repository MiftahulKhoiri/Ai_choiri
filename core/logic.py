from ml.model import IntentModel
from core.context import ContextMemory
from utils.entity_extractor import extract_entities
from data.profile import load_profile, save_profile


RESPONSES = {
    "greeting": "Halo 👋",
    "bye": "Sampai jumpa 👋",
    "python": "Python itu bahasa yang keren 🐍",
    "creator_python": "Python dibuat oleh Guido van Rossum 👨‍💻",
    "unknown": "Aku masih belajar 🤖"
}


class SimpleAI:
    def __init__(self, dataset):
        self.intent_model = IntentModel(dataset)
        self.context = ContextMemory()
        self.profile = load_profile()

    def respond(self, user_input: str) -> str:
        # 1️⃣ simpan konteks
        self.context.add(user_input)
        context_text = self.context.get()

        # 2️⃣ prediksi intent & entity
        intent = self.intent_model.predict(context_text)
        entities = extract_entities(context_text)

        # 3️⃣ update profil (memory panjang)
        self._update_profile(entities)

        # 4️⃣ generate respon
        return self._generate_response(intent)

    # ===============================
    # 🔽 BAGIAN INTERNAL (BERSIH)
    # ===============================

    def _update_profile(self, entities: dict):
        if "nama" in entities:
            self.profile["nama"] = entities["nama"]
            save_profile(self.profile)

    def _generate_response(self, intent: str) -> str:
        name = self.profile.get("nama")

        if intent == "greeting":
            return f"Halo {name} 👋" if name else RESPONSES["greeting"]

        if intent == "bye":
            return f"Sampai jumpa {name} 👋" if name else RESPONSES["bye"]

        return RESPONSES.get(intent, RESPONSES["unknown"])