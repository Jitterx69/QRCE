import json
import time
import uuid

def log(component, event, payload=None):
    record = {
        "timestamp": time.time(),
        "component": component,
        "event": event,
        "payload": payload or {},
    }
    print(json.dumps(record))

def metric(name, value, labels=None):
    record = {
        "name": name,
        "value": value,
        "labels": labels or {},
    }
    print(json.dumps(record))

class Trace:
    def __init__(self, span):
        self.trace_id = str(uuid.uuid4())
        self.span = span
        self.start = time.time()

    def close(self):
        end = time.time()
        record = {
            "trace_id": self.trace_id,
            "span": self.span,
            "start": self.start,
            "end": end,
        }
        print(json.dumps(record))
