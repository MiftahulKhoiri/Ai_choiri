import os
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

MODEL_PATH = "data/intent_model.pkl"

class IntentModel:
    def __init__(self, dataset=None):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

        if os.path.exists(MODEL_PATH):
            self.load()
        elif dataset is not None:
            self.train(dataset)
            self.save()
        else:
            raise ValueError("Dataset tidak ada dan model belum tersimpan")

    def train(self, dataset):
        X, y = [], []

        for intent, texts in dataset.items():
            for text in texts:
                X.append(text.lower())
                y.append(intent)

        X_vec = self.vectorizer.fit_transform(X)
        self.model.fit(X_vec, y)

    def predict(self, text):
        vec = self.vectorizer.transform([text.lower()])
        return self.model.predict(vec)[0]

    def save(self):
        os.makedirs("data", exist_ok=True)
        joblib.dump((self.vectorizer, self.model), MODEL_PATH)
        print("[INFO] Model intent disimpan.")

    def load(self):
        self.vectorizer, self.model = joblib.load(MODEL_PATH)
        print("[INFO] Model intent dimuat.")