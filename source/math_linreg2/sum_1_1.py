import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt




TIMES_LOG = []
def benchmark(func):
    global TIMES_LOG
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        TIMES_LOG.append(time.clock()-t)
        return res
    return wrapper



def create_normal_array(m, n, seed):
    np.random.seed(seed)
    array = np.random.normal(size=(m, n))
    return array

@benchmark
def qr(A):
    # return la.qr(A, pivoting=True)
    return np.linalg.qr(A)



PAR_SEED = 1
MAX_POWER = 4


m_sizes = np.logspace(1, MAX_POWER, 20).astype(int)
n_sizes = m_sizes

ARRAYS = []
for m in m_sizes:
    A = create_normal_array(m, 10, 1)
    ARRAYS.append(A)
    # Q, R, perm = qr(A)
    Q, R = qr(A)
    diagonal_of_H = np.apply_along_axis(lambda x: sum(x * x), 1, Q)

fig, ax = plt.subplots(1, 1)
ax.scatter(m_sizes, TIMES_LOG)
ax.set_yscale('log')
ax.set_yscale('log')


"""test_czy dziala"""
# A = create_normal_array(100, 10, 1)
# Q, R = np.linalg.qr(A)
# diagonal_of_H = np.apply_along_axis(lambda x: sum(x * x), 1, Q)
# res2 = A.dot(np.linalg.inv(A.T.dot(A))).dot(A.T)
# diag_test = np.diag(res2)

"""remove"""
# test_array = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [11, 12, 13]
# ])
# z1 = np.apply_along_axis(lambda x: sum(x * x), 1, test_array)
# np.apply_along_axis(lambda x: print(sum(x * x)), 1, test_array)