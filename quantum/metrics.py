def entropy_trajectory(history):
    return [s.entropy() for s in history]

def detect_noncontraction(history, tol=1e-6):
    for i in range(len(history)-2):
        if history[i+2].distance(history[i+1]) > history[i+1].distance(history[i]) + tol:
            return True
    return False
