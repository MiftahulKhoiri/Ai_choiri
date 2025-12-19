from ml.dataset import dataset
from ml.model import IntentModel

class SimpleAI:
    def __init__(self, memory):
        self.memory = memory
        self.intent_model = IntentModel(dataset)

    def respond(self, text):
        intent = self.intent_model.predict(text)

        if intent == "greeting":
            return "Halo juga 👋"

        if intent == "goodbye":
            return "Sampai jumpa 👋"

        if intent == "python":
            return "Python itu bahasa yang keren 🐍"

        return "Aku masih belajar 🤖"