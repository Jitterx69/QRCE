def iterate(phi, s0, tol=1e-8, max_iter=500):
    s = s0.copy()
    history = [s.copy()]

    for k in range(max_iter):
        s_next = phi(s)
        history.append(s_next.copy())

        if s_next.distance(s) < tol:
            return {
                "fixed_point": s_next,
                "converged": True,
                "iterations": k + 1,
                "history": history,
            }

        s = s_next

    return {
        "fixed_point": s,
        "converged": False,
        "iterations": max_iter,
        "history": history,
    }
