from utils.text import normalize
from config.settings import THRESHOLD_RESPON

class SimpleAI:
    def __init__(self, memory):
        self.memory = memory
        self.keyword_score = self._belajar_dari_memori()

    def _belajar_dari_memori(self):
        skor = {}
        for item in self.memory:
            pesan = item.get("user", "")
            for kata in pesan.split():
                skor[kata] = skor.get(kata, 0) + 1
        return skor

    def respond(self, pesan: str) -> str:
        pesan = normalize(pesan)
        score = 0

        for kata in pesan.split():
            score += self.keyword_score.get(kata, 0)

        if "bye" in pesan:
            return "Sampai jumpa."

        if score >= THRESHOLD_RESPON:
            return "Aku mulai memahami pola bicaramu."
        elif score > 0:
            return "Aku menangkap sedikit maksudmu."
        else:
            return "Aku belum paham, jelaskan lagi."