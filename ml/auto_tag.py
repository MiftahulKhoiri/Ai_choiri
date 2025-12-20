from ml.tokenizer import tokenize
from ml.similarity import vectorize, cosine_similarity

def suggest_intent(text: str, dataset: dict):
    input_vec = vectorize(tokenize(text))

    best_score = 0.0
    best_intent = None

    for intent, data in dataset.items():
        for pattern in data["patterns"]:
            score = cosine_similarity(
                input_vec,
                vectorize(tokenize(pattern))
            )
            if score > best_score:
                best_score = score
                best_intent = intent

    if best_score > 0.15:
        return best_intent, best_score

    return None, 0.0