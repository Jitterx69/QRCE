import json
import os

class Recorder:
    def __init__(self, root):
        self.root = root
        os.makedirs(root, exist_ok=True)

    def record(self, experiment, history):
        path = os.path.join(self.root, experiment.id)
        os.makedirs(path, exist_ok=True)

        meta = {
            "id": experiment.id,
            "name": experiment.name,
            "created_at": experiment.created_at.isoformat(),
            "steps": len(history),
        }

        with open(os.path.join(path, "meta.json"), "w") as f:
            json.dump(meta, f)

        for i, state in enumerate(history):
            with open(os.path.join(path, f"state_{i}.json"), "w") as f:
                json.dump(state.v.tolist(), f)
