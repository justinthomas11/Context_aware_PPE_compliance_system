import random

class PPEValidator:
    def validate(self, track):
        return {
            "helmet": random.random() > 0.4,
            "vest": random.random() > 0.3,
            "goggles": random.random() > 0.5,
            "gloves": random.random() > 0.4,
            "boots": random.random() > 0.2,
        }
