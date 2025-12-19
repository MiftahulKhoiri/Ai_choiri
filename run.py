from utils.updater import git_update 
from core.logic import SimpleAI
from data.memory import load_memory, save_memory, clear_memory
from config.settings import AI_NAME, VERSION

def main():
    # 🔹 Update repo (AMAN kalau gagal)
    git_update()

    ai = SimpleAI()
    memory = load_memory()

    print("=" * 30)
    print(f"{AI_NAME} v{VERSION}")
    print("Ketik 'bye' untuk keluar | 'reset' untuk hapus memori")
    print("=" * 30)

    while True:
        user = input("Kamu: ").strip()
        if not user:
            continue

        # 🔹 Perintah sistem
        if user.lower() == "reset":
            clear_memory()
            memory.clear()
            print("AI : Memori direset.")
            continue

        respon = ai.respond(user)
        print("AI :", respon)

        memory.append({"user": user, "ai": respon})
        save_memory(memory)

        if respon.lower().startswith("sampai"):
            break

if __name__ == "__main__":
    main()