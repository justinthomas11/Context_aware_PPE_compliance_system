import random

class MockDetector:
    def detect(self):
        return [
            {"temp_id": 1, "bbox": [random.randint(50,500), random.randint(50,500), 60, 140]},
            {"temp_id": 2, "bbox": [random.randint(50,500), random.randint(50,500), 60, 140]}
        ]
