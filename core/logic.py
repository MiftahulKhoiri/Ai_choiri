from ml.model import IntentModel
from core.context import ContextMemory
from utils.entity_extractor import extract_entities
from data.profile import load_profile, save_profile
from data.chatlog import log_chat
from data.learned import load_learned, save_learned, add_suggestion
from ml.auto_tag import suggest_intent
from config.settings import ADMIN_MODE


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

        # 2️⃣ prediksi intent + confidence
        intent, score = self.intent_model.predict(context_text)
        entities = extract_entities(context_text)

        # 3️⃣ update profil
        self._update_profile(entities)

        # 4️⃣ simpan log chat
        log_chat(user_input, intent)

        # 5️⃣ BELAJAR JIKA TIDAK YAKIN
        if intent == "unknown":
            self._learn_from_chat(user_input)
            self.context.clear()
            return "Aku belum paham 🤔 Aku simpan ini untuk dipelajari."

        # 6️⃣ respon normal
        return self._generate_response(intent)

    # ===============================
    # 🔽 BAGIAN INTERNAL
    # ===============================

    def _update_profile(self, entities: dict):
        if "nama" in entities:
            self.profile["nama"] = entities["nama"]
            save_profile(self.profile)

    def _learn_from_chat(self, text: str):
        # simpan unknown
        learned = load_learned()
        learned.setdefault("unknown", [])
        learned["unknown"].append(text)
        save_learned(learned)

        # 🔮 AUTO TAG
        intent, score = suggest_intent(text, self.intent_model.dataset)
        if intent:
            add_suggestion(text, intent, score)

    def _generate_response(self, intent: str) -> str:
        name = self.profile.get("nama")

        if intent == "greeting":
            return f"Halo {name} 👋" if name else RESPONSES["greeting"]

        if intent == "bye":
            return f"Sampai jumpa {name} 👋" if name else RESPONSES["bye"]

        return RESPONSES.get(intent, RESPONSES["unknown"])