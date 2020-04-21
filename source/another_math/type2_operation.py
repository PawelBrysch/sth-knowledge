import numpy as np
import random
import copy


def get_random_4x4():
    return np.array([random.randint(1, 4) for i in range(16)]).reshape(4, 4)


target = 2
source = 1
factor_ = 4


for i in range(5):
    a = get_random_4x4()
    elem_mat = np.identity(4)
    elem_mat[target][source] = factor_
    res = np.matmul(elem_mat, a)
    print(np.linalg.det(a), np.linalg.det(res))

