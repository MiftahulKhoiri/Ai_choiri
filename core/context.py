class ContextMemory:
    def __init__(self):
        self.memory = []

    def add(self, text: str):
        self.memory.append(text)

    def get(self) -> str:
        return " ".join(self.memory)

    def clear(self):
        self.memory = []