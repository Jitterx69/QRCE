def ethical_violation_rate(events):
    if not events:
        return 0.0
    return sum(events) / len(events)
