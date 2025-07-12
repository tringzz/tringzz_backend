# memory/memory_store.py

class MemoryStore:
    def __init__(self):
        self.store = {}

    def save_message(self, session_id, role, message):
        if session_id not in self.store:
            self.store[session_id] = []
        self.store[session_id].append({"role": role, "message": message})

    def get_conversation(self, session_id):
        return self.store.get(session_id, [])

    def clear_conversation(self, session_id):
        if session_id in self.store:
            del self.store[session_id]
