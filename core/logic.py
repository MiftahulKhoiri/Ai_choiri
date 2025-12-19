from utils.text import normalize
from config.settings import THRESHOLD_RESPON

class SimpleAI:
    def __init__(self):
        self.score = 0

    def respond(self, pesan: str) -> str:
        pesan = normalize(pesan)
        self.score = 0

        if "halo" in pesan:
            self.score += 10
        if "ai" in pesan:
            self.score += 20
        if "python" in pesan:
            self.score += 30
        if "bye" in pesan:
            self.score -= 100

        if self.score >= THRESHOLD_RESPON:
            return "Aku mengerti."
        elif self.score < 0:
            return "Sampai jumpa."
        else:
            return "Jelaskan lagi."