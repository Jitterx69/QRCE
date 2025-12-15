def detect_nonhalting(history, tol=1e-8, window=10):
    if len(history) < window:
        return False

    recent = history[-window:]
    deltas = [
        recent[i+1].distance(recent[i])
        for i in range(len(recent)-1)
    ]

    return all(abs(deltas[i+1] - deltas[i]) < tol for i in range(len(deltas)-1))


def detect_oscillation(history, tol=1e-6):
    for i in range(len(history)-2):
        if history[i].distance(history[i+2]) < tol:
            return True
    return False
