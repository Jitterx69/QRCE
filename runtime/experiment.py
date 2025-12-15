import uuid
from datetime import datetime

class Experiment:
    def __init__(self, name, initial_state, max_steps):
        self.id = str(uuid.uuid4())
        self.name = name
        self.initial_state = initial_state
        self.max_steps = int(max_steps)
        self.created_at = datetime.utcnow()
