import os
import json
import joblib
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# =========================
# PATH CONFIG
# =========================
MODEL_PATH = "data/intent_model.pkl"
LEARN_PATH = "data/learned_data.json"

# =========================
# TEXT CLEANER (Indonesia ringan)
# =========================
STOPWORDS = {
    "yang", "dan", "di", "ke", "dari", "ini", "itu",
    "aku", "kamu", "saya", "dia", "apa", "ada",
    "bagaimana", "gimana"
}

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    words = text.split()
    words = [w for w in words if w not in STOPWORDS]
    return " ".join(words)

# =========================
# INTENT MODEL
# =========================
class IntentModel:
    def __init__(self, dataset: dict):
        self.dataset = dataset

        # 🔥 CHAR N-GRAM (anti typo)
        self.vectorizer = CountVectorizer(
            analyzer="char",
            ngram_range=(2, 4)
        )
        self.model = MultinomialNB()

        if os.path.exists(MODEL_PATH):
            self.load()
        else:
            self.train()
            self.save()

    # =====================
    # TRAINING
    # =====================
    def train(self):
        X, y = [], []

        # dataset utama
        for intent, texts in self.dataset.items():
            for text in texts:
                X.append(clean_text(text))
                y.append(intent)

        # dataset hasil belajar
        if os.path.exists(LEARN_PATH):
            with open(LEARN_PATH, "r") as f:
                learned = json.load(f)

            for intent, texts in learned.items():
                for text in texts:
                    X.append(clean_text(text))
                    y.append(intent)

        if not X:
            raise ValueError("Dataset kosong, tidak bisa training")

        X_vec = self.vectorizer.fit_transform(X)
        self.model.fit(X_vec, y)

    # =====================
    # PREDICT + CONFIDENCE
    # =====================
    def predict(self, text: str, threshold: float = 0.35) -> str:
        cleaned = clean_text(text)

        if not cleaned:
            return "unknown"

        vec = self.vectorizer.transform([cleaned])
        probs = self.model.predict_proba(vec)[0]

        intent = self.model.classes_[probs.argmax()]
        confidence = probs.max()

        if confidence < threshold:
            return "unknown"

        return intent

    # =====================
    # SAVE / LOAD
    # =====================
    def save(self):
        os.makedirs("data", exist_ok=True)
        joblib.dump(
            {
                "vectorizer": self.vectorizer,
                "model": self.model
            },
            MODEL_PATH
        )
        print("[INFO] Model intent disimpan.")

    def load(self):
        data = joblib.load(MODEL_PATH)
        self.vectorizer = data["vectorizer"]
        self.model = data["model"]
        print("[INFO] Model intent dimuat.")

    # =====================
    # INCREMENTAL LEARNING
    # =====================
    def learn(self, intent: str, text: str):
        os.makedirs("data", exist_ok=True)

        if os.path.exists(LEARN_PATH):
            with open(LEARN_PATH, "r") as f:
                data = json.load(f)
        else:
            data = {}

        data.setdefault(intent, [])
        if text not in data[intent]:
            data[intent].append(text)

        with open(LEARN_PATH, "w") as f:
            json.dump(data, f, indent=2)

        self.train()
        self.save()