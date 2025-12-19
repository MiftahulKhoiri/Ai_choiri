from ml.model import IntentModel
from core.context import ContextMemory

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
        # simpan ke context
        self.context.add(user_input)

        # gabungkan context
        context_text = self.context.get()

        intent = self.intent_model.predict(context_text)

        return RESPONSES.get(intent, RESPONSES["unknown"])