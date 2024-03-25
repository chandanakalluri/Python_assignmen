import numpy as np

def min_max():
    c, d = map(int, input().split())
    arr = np.array([input().split() for _ in range(c)], dtype=int)

    # Compute min along axis 0 and then find the max of that result
    result = np.max(np.min(arr, axis=0))

    # Output
    return result
