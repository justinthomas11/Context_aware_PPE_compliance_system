class TemporalEngine:
    def __init__(self):
        self.memory = {}

    def update(self, pid, ppe, zone):
        if pid not in self.memory:
            self.memory[pid] = {
                "ppe": [],
                "zone": [],
                "transitions": []
            }

        prev_zone = self.memory[pid]["zone"][-1] if self.memory[pid]["zone"] else None

        if prev_zone and prev_zone != zone:
            self.memory[pid]["transitions"].append(f"{prev_zone}->{zone}")

        self.memory[pid]["ppe"].append(ppe)
        self.memory[pid]["zone"].append(zone)

        self.memory[pid]["ppe"] = self.memory[pid]["ppe"][-30:]
        self.memory[pid]["zone"] = self.memory[pid]["zone"][-15:]
