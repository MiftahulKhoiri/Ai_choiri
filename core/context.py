from collections import deque

class ContextMemory:
    def __init__(self):
        self.memory = []

    def add(self, text):
        self.memory.append(text)

    def get(self):
        return " ".join(self.memory)

    def clear(self):
        self.memory = []