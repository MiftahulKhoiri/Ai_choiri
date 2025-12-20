from ml.tokenizer import tokenize
from ml.similarity import vectorize, cosine_similarity


class IntentModel:
    def __init__(self, dataset: dict):
        self.dataset = dataset
        self.pattern_vectors = self._prepare_patterns()

    def _prepare_patterns(self):
        vectors = []
        for intent, data in self.dataset.items():
            for pattern in data["patterns"]:
                tokens = tokenize(pattern)
                vectors.append({
                    "intent": intent,
                    "vector": vectorize(tokens)
                })
        return vectors

    def predict(self, text: str):
        input_vec = vectorize(tokenize(text))

        best_score = 0.0
        best_intent = "unknown"

        for item in self.pattern_vectors:
            score = cosine_similarity(input_vec, item["vector"])
            if score > best_score:
                best_score = score
                best_intent = item["intent"]

        # 🔥 THRESHOLD CERDAS
        if best_score < 0.3:
            return "unknown", best_score

        return best_intent, best_score