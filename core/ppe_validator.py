class PPEValidator:
    def __init__(self):
        self.zone_requirements = {
            "Office (Safe Zone)": [],
            "Storage/Production Walkways (Moderate-Risk zone)": ["helmet", "goggles", "boots", "trousers"],
            "Machinery Area (High-Risk Zone)": ["helmet", "vest", "goggles", "gloves", "boots"]
        }

    def validate(self, track, zone):
        ppe_status = track.get("ppe", {})

        required = self.zone_requirements.get(zone, [])
        missing = []

        for item in required:
            if not ppe_status.get(item, False):
                missing.append(item)

        return ppe_status, missing
