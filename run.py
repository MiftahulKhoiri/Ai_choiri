from core.logic import SimpleAI
from config.settings import AI_NAME, VERSION

def main():
    ai = SimpleAI()

    print("=" * 30)
    print(f"{AI_NAME} v{VERSION}")
    print("Ketik 'bye' untuk keluar")
    print("=" * 30)

    while True:
        user_input = input("Kamu: ")

        if not user_input.strip():
            continue

        respon = ai.respond(user_input)
        print("AI :", respon)

        if respon.lower().startswith("sampai"):
            break

if __name__ == "__main__":
    main()