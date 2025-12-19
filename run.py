from utils.updater import git_update

# 🔴 WAJIB di atas, sebelum import lain
git_update()

from core.logic import SimpleAI
from config.settings import AI_NAME, VERSION
from data.memory import load_memory, save_memory

def main():
    memory = load_memory()
    ai = SimpleAI(memory)

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

        memory.append({"user": user, "ai": respon})
        save_memory(memory)

        if user.lower() == "bye":
            break

if __name__ == "__main__":
    main()