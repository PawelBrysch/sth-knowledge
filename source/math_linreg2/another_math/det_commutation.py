import numpy as np
import random
a = np.array([random.randint(1, 4) for i in range(15)]).reshape(3, 5)
b = np.array([random.randint(1, 4) for i in range(15)]).reshape(5, 3)

a_b = np.matmul(a, b)
b_a = np.matmul(b, a)