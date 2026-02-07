class ReasoningEngine:
    def decide(self, gid, zone, temporal):
        state = temporal.memory.get(gid, {})
        ppe_state = state.get("ppe", [{}])[-1] if state else {}

        # ✅ Zone-specific PPE requirements
        required = {
            "office": [],

            "storage": [
                "helmet",
                "goggles",
                "boots",
                "trousers"
            ],

            "factory": [
                "helmet",
                "vest",
                "goggles",
                "gloves",
                "boots"
            ]
        }

        req = required.get(zone, [])
        missing = [r for r in req if not ppe_state.get(r, False)]

        # ✅ Decision logic
        if zone == "office":
            decision = "GREEN"
        elif missing:
            decision = "RED"
        else:
            decision = "YELLOW"

        return decision, missing
