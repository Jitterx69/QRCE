from engine.metrics import trajectory_norms

def runtime_metrics(history):
    norms = trajectory_norms(history)
    return {
        "max_norm": max(norms),
        "final_norm": norms[-1],
    }
