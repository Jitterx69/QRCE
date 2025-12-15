import numpy as np

def trajectory_norms(history):
    return [s.norm() for s in history]

def lyapunov_estimate(history):
    if len(history) < 3:
        return 0.0
    diffs = [history[i+1].distance(history[i]) for i in range(len(history)-1)]
    ratios = [diffs[i+1] / diffs[i] for i in range(len(diffs)-1) if diffs[i] > 0]
    return np.log(np.mean(ratios)) if ratios else 0.0

def detect_divergence(history, threshold=1e3):
    return any(s.norm() > threshold for s in history)
