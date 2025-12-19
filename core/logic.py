from utils.text import normalize
import random

class SimpleAI:
    def __init__(self):
        self.intent = {
            "salam": ["halo", "hai"],
            "pamit": ["bye", "keluar"],
            "belajar": ["python", "belajar", "coding"]
        }

        self.responses = {
            "salam": ["Halo.", "Hai, ada yang bisa dibantu?"],
            "pamit": ["Sampai jumpa."],
            "belajar": ["Mau belajar apa?", "Topik apa yang kamu pilih?"],
            "default": ["Saya belum paham."]
        }

    def respond(self, pesan: str) -> str:
        pesan = normalize(pesan)

        for intent, kata_kunci in self.intent.items():
            for kata in kata_kunci:
                if kata in pesan:
                    return random.choice(self.responses[intent])

        return random.choice(self.responses["default"])