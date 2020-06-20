import numpy as np

some_arr = np.array([
    [1,2,31,4],
    [0,2,3,4],
    [0,0,3,4],
    [0,0,0,4],
])

det = np.linalg.det(some_arr)