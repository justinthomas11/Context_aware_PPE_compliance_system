import json
import time

class JSONLogger:
    def __init__(self, path="events.json"):
        self.path = path
        self.buffer = []

    def log(self, data):
        data["ts"] = time.time()
        self.buffer.append(data)

        with open(self.path, "a") as f:
            f.write(json.dumps(data) + "\n")

    def get_recent(self, n=20):
        return self.buffer[-n:]
