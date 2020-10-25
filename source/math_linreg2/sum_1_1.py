import itertools
import time
import numpy as np
import matplotlib.pyplot as plt


def solution(X):
    Q, R = np.linalg.qr(X)
    return np.apply_along_axis(lambda x: sum(x * x), 1, Q)


"""helper method"""
def sample_normal_array(m, n):
    np.random.seed(1)
    array = np.random.normal(size=(m, n))
    return array


"""TEST OF PERFORMANCE"""
# LOG_M_UPPER_BOUND = 3
# m_sizes = np.logspace(1, LOG_M_UPPER_BOUND, 20).astype(int)
# n_sizes = [10, 20, 50, 100, 200, 500]
#
# pairs = list(itertools.product(m_sizes, n_sizes))
# realistic_pairs = list(filter(lambda x: x[0] > x[1], pairs))
#
# array_sizes = []
# computation_times = []
# for m, n in realistic_pairs:
#     X = sample_normal_array(m, n)
#
#     start = time.clock()
#     diagonal_of_H = solution(X)
#     stop = time.clock()
#
#     array_sizes.append(m * n)
#     computation_times.append(stop - start)
#
# fig, ax = plt.subplots(1, 1)
# ax.scatter(array_sizes, computation_times)
# ax.set_xlabel('m x n')
# ax.set_ylabel('time [s]')


"""TESTS OF CORRECTNESS"""
# def calculate_leverages_brute_force(X):
#     H = X.dot(np.linalg.inv(X.T.dot(X))).dot(X.T)
#     return np.diag(H)
#
# test_cases = [
#     (10, 10),
#     (100, 10),
#     (1000, 10),
#     (10000, 10),
#     (1000, 100),
#     (10000, 100)
# ]
#
# for m, n in test_cases:
#     X = sample_normal_array(m, n)
#     leverages = solution(X)
#     leverages_brute_force = calculate_leverages_brute_force(X)
#     np.testing.assert_array_almost_equal(leverages, leverages_brute_force)
