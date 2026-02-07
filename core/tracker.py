class Tracker:
    def __init__(self):
        self.next_id = 1
        self.map = {}

    def update(self, detections):
        tracks = []

        for d in detections:
            tid = self.map.get(d["temp_id"])
            if not tid:
                tid = self.next_id
                self.map[d["temp_id"]] = tid
                self.next_id += 1

            tracks.append({
                "id": tid,
                "bbox": d["bbox"],
                "ppe": d.get("ppe", {})   # ✅ keep PPE
            })

        return tracks
