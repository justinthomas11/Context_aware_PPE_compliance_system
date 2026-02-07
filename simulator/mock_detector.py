import random

class MockDetector:
    def detect(self):
        def random_ppe():
            return {
                "helmet": random.choice([True, False]),
                "vest": random.choice([True, False]),
                "goggles": random.choice([True, False]),
                "gloves": random.choice([True, False]),
                "boots": random.choice([True, False]),
                "trousers": random.choice([True, False])
            }

        return [
            {
                "temp_id": 1,
                "bbox": [random.randint(50,500), random.randint(50,500), 60, 140],
                "ppe": random_ppe()
            },
            {
                "temp_id": 2,
                "bbox": [random.randint(50,500), random.randint(50,500), 60, 140],
                "ppe": random_ppe()
            }
        ]
