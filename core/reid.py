import hashlib

class ReIDEngine:
    def assign_global_id(self, bbox):
        x,y,w,h = bbox
        key = f"{x}{y}{w}{h}"
        return hashlib.md5(key.encode()).hexdigest()[:6]
