from utils.updater import git_update
from core.logic import SimpleAI
from config.settings import AI_NAME, VERSION
from data.memory import load_memory, save_memory

def main():
    git_update()

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

        if respon.lower().startswith("sampai"):
        
        if user.lower() == "reset":
    clear_memory()
    print("AI : Memori direset.")
    continue
            break

if __name__ == "__main__":
    main()