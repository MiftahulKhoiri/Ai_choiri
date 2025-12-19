from utils.updater import git_update

# 🔴 WAJIB: sebelum import ML
git_update()

from core.logic import SimpleAI
from config.settings import AI_NAME, VERSION
from data.memory import load_memory, save_memory
from data.dataset import DATASET   # 🔥 DATASET DIPISAH

def main():
    # memory chat (history)
    memory = load_memory()

    # AI pakai DATASET, bukan memory
    ai = SimpleAI(DATASET)

    print("=" * 30)
    print(f"{AI_NAME} v{VERSION}")
    print("Ketik 'bye' untuk keluar")
    print("=" * 30)

    while True:
        user = input("Kamu: ").strip()
        if not user:
            continue

        respon = ai.respond(user)
        print("AI :", respon)

        # simpan history chat
        memory.append({
            "user": user,
            "ai": respon
        })
        save_memory(memory)

        if user.lower() == "bye":
            break

if __name__ == "__main__":
    main()