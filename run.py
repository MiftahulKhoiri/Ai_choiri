from utils.updater import git_update
from core.logic import SimpleAI
from config.settings import AI_NAME, VERSION
from data.memory import load_memory, save_memory, clear_memory

def main():
    git_update()

    memory = load_memory()
    ai = SimpleAI(memory)

    print("=" * 30)
    print(f"{AI_NAME} v{VERSION}")
    print("Ketik 'bye' untuk keluar | ketik 'reset' untuk hapus memori")
    print("=" * 30)

    while True:
        user = input("Kamu: ").strip()
        if not user:
            continue

        # 🔴 Perintah khusus RESET
        if user.lower() == "reset":
            clear_memory()
            memory.clear()
            ai.memory = []
            print("AI : Memori direset.")
            continue

        respon = ai.respond(user)
        print("AI :", respon)

        memory.append({"user": user, "ai": respon})
        save_memory(memory)

        # 🔴 Keluar
        if respon.lower().startswith("sampai"):
            break

if __name__ == "__main__":
    main()