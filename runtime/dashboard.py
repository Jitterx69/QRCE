def summarize(history):
    return {
        "steps": len(history),
        "final_norm": history[-1].norm(),
    }
