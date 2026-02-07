class PPEValidator:
    def __init__(self):
        self.zone_requirements = {
            "office": [],
            "storage": ["helmet", "goggles", "boots", "trousers"],
            "factory": ["helmet", "vest", "goggles", "gloves", "boots"]
        }

    def validate(self, track, zone):
        ppe_status = track.get("ppe", {})

        required = self.zone_requirements.get(zone, [])
        missing = []

        for item in required:
            if not ppe_status.get(item, False):
                missing.append(item)

        return ppe_status, missing
