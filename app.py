from core.zone_manager import ZoneManager
from simulator.mock_detector import MockDetector
from core.tracker import Tracker
from core.ppe_validator import PPEValidator
from core.temporal import TemporalEngine
from core.reasoning import ReasoningEngine
from core.risk_engine import RiskEngine
from core.alerts import AlertEngine
from core.reid import ReIDEngine
from core.logger import JSONLogger
from simulator.scenario_generator import run_loop


class Pipeline:
    def __init__(self):
        self.cam_id = "cam1"

        self.event_pid = 1   
        self.detector = MockDetector()
        self.tracker = Tracker()
        self.zone_manager = ZoneManager("config/zones.json")
        self.ppe = PPEValidator()
        self.temporal = TemporalEngine()
        self.reasoner = ReasoningEngine()
        self.risk = RiskEngine()
        self.alerts = AlertEngine()
        self.reid = ReIDEngine()
        self.logger = JSONLogger()
    
    def step(self):
        detections = self.detector.detect()
        tracks = self.tracker.update(detections)
        
        for t in tracks:
            bbox = t["bbox"]
        
            gid = self.reid.assign_global_id(bbox)
            t["gid"] = gid
        
            zone = self.zone_manager.assign_zone(bbox)
        
            ppe_status = self.ppe.validate(t)
        
            self.temporal.update(gid, ppe_status, zone)
        
            decision, missing = self.reasoner.decide(gid, zone, self.temporal)
        
            risk_tag = self.risk.tag(decision)
        
            self.alerts.emit(gid, bbox, zone, risk_tag, missing)

        
            self.logger.log({
                "pid": self.event_pid,
                "gid": t["gid"],
                "zone": zone,
                "decision": decision,
                "ppe": ppe_status
            })
            self.event_pid += 1 
        
            # 9. Alert / display
            self.alerts.emit(gid, bbox, zone, risk_tag, missing)


if __name__ == "__main__":
    pipeline = Pipeline()
    run_loop(pipeline)
