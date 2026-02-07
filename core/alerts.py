class AlertEngine:
    def emit(self, gid, bbox, zone, risk, missing):
        print(f"[{risk}] GID={gid} ZONE={zone} MISSING={missing}")
