import json
from utils.geometry import point_in_poly

class ZoneManager:
    def __init__(self, path):
        with open(path) as f:
            self.zones = json.load(f)

    def assign_zone(self, bbox):
        x,y,w,h = bbox
        cx, cy = x + w//2, y + h//2

        for name, poly in self.zones.items():
            if point_in_poly(cx, cy, poly):
                return name
        return "unknown"
