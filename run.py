from utils.updater import git_update
from core.logic import SimpleAI
from config.settings import AI_NAME, VERSION

def main():
    # update repo dulu
    git_update()

    # jalankan AI
    ai = SimpleAI()

    print("=" * 30)
    print(f"{AI_NAME} v{VERSION}")
    print("Ketik 'bye' untuk keluar")
    print("=" * 30)

    while True:
        user_input = input("Kamu: ").strip()
        if not user_input:
            continue

        respon = ai.respond(user_input)
        print("AI :", respon)

        if respon.lower().startswith("sampai"):
            break

if __name__ == "__main__":
    main()