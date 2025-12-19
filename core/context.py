from collections import deque

class ContextMemory:
    def __init__(self, max_len=3):
        self.memory = deque(maxlen=max_len)

    def add(self, text):
        self.memory.append(text)

    def get(self):
        return " ".join(self.memory)