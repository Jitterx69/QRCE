import numpy as np

def state_variance(x):
    return np.var(x)

def entropy_like(p):
    p = np.asarray(p)
    p = p[p > 0]
    return -np.sum(p * np.log(p))
