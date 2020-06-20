from scipy.linalg import null_space
import numpy as np
import random

def get_random_4x4():
    return np.array([random.randint(1, 4) for i in range(16)]).reshape(4, 4)

# A = np.array([[1, 2], [2, 4]])
# ns = null_space(A)
# ns * np.sign(ns[0,0])  # Remove the sign ambiguity of the vector

singular = []
nonsingular = []

for i in range(100):
    arr = get_random_4x4()
    det = np.linalg.det(arr)
    if det == 0.0:
        singular.append(arr)
    else:
        nonsingular.append(arr)

for arr in nonsingular:
    print(null_space(arr))