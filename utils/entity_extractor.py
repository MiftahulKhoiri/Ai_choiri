import re

def extract_entities(text: str) -> dict:
    entities = {}

    text = text.lower()

    # =====================
    # WAKTU
    # =====================
    waktu_match = re.findall(
        r"(pagi|siang|sore|malam|besok|hari ini|jam\s?\d+)",
        text
    )
    if waktu_match:
        entities["waktu"] = waktu_match

    # =====================
    # NAMA (sederhana)
    # =====================
    nama_match = re.search(
        r"(nama saya|namaku|aku bernama)\s+([a-z]+)",
        text
    )
    if nama_match:
        entities["nama"] = nama_match.group(2).capitalize()

    # =====================
    # ANGKA
    # =====================
    angka = re.findall(r"\d+", text)
    if angka:
        entities["angka"] = angka

    return entities