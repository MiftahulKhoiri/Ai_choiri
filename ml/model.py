from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class IntentModel:
    def __init__(self, dataset):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

        X = []
        y = []

        for intent, texts in dataset.items():
            for text in texts:
                X.append(text)
                y.append(intent)

        X_vec = self.vectorizer.fit_transform(X)
        self.model.fit(X_vec, y)

    def predict(self, text):
        vec = self.vectorizer.transform([text])
        return self.model.predict(vec)[0]