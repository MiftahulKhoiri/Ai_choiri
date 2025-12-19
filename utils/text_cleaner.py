import re

STOPWORDS = {
    "yang", "dan", "di", "ke", "dari", "ini", "itu",
    "aku", "kamu", "saya", "dia", "apa", "ada"
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = text.split()
    words = [w for w in words if w not in STOPWORDS]

    return " ".join(words)