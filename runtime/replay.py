import json
import os
from engine.state import State

class Replay:
    def __init__(self, root):
        self.root = root

    def load(self, experiment_id):
        path = os.path.join(self.root, experiment_id)
        states = []

        files = sorted(
            f for f in os.listdir(path) if f.startswith("state_")
        )

        for f in files:
            with open(os.path.join(path, f)) as fh:
                states.append(State(json.load(fh)))

        return states
