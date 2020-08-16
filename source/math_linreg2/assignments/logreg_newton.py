print("elo")
import pathlib as pl
import pandas as pd
import numpy as np
from typing import List

x = pl.Path(__file__).with_name('x.dat')
y = pl.Path(__file__).with_name('y.dat')
pt1 = pd.read_csv(x, sep=r'\s{2,}', engine='python')
pt2 = pd.read_csv(y, sep=r'\s{2,}', engine='python')
data = pt2.assign(X1=pt1['X1'], X2=pt1['X2'])


# X_avg = [-0.065, 0.015]
X_avg = [5, 5]
TAU = 0.5

# def weights(X1: pd.Series, X2: pd.Series, X: List[int]):
#     global TAU
#     return np.exp(-np.sqrt((X1 - X[0]) ** 2 + (X2 - X[1]) ** 2) / (2 * TAU ** 2))

def weights(X: pd.DataFrame, arg_x: List[int]):
    global TAU
    return np.exp(-np.sqrt((X['X1'] - arg_x[0]) ** 2 + (X['X2'] - arg_x[1]) ** 2) / (2 * TAU ** 2))

small_testdata = pd.DataFrame.from_dict({
    'Y': [0, 0],
    'X1': [2, 1],
    'X2': [3, 4],
})
big_testdata = pd.DataFrame.from_dict({
    'Y': np.linspace(0, 0, 10),
    'X1': np.linspace(1, 10, 10),
    'X2': np.linspace(11, 20, 10),
})
"""TEST: weights"""
# w = weights(small_testdata['X1'], small_testdata['X2'], X_avg)
# small_testdata = small_testdata.assign(W=w)
# print(small_testdata)
"""TEST: weights"""
# w = weights(small_testdata, X_avg)
# small_testdata = small_testdata.assign(W=w)
# print(small_testdata)
# pd.testing.assert_series_equal(w, pd.Series([0.00073834, 0.00026225]))
# pd.testing.assert_series_equal(pd.Series([0.00073834, 0.00026225]), pd.Series([0.00073834, 0.00026225]))


# X = big_testdata.loc[:, ['X1', 'X2']]
# TODO
"""notatka"""
# X.__matmul__(X.T)
# np.identity(X.__len__())

THETA_0 = np.array([-1, 2, 1])

def func_H(x1: float, x2: float, theta: np.array):
    return 1 / (
        1 + np.exp(
            -(theta[0] + x1 * theta[1] + x2 * theta[2])
        )
    )

class Step:
    def __init__(self):
        pass

    @staticmethod
    def calculate_h(arg_X: pd.DataFrame, theta: np.array):
        return func_H(arg_X['X1'], arg_X['X2'], theta)

    @staticmethod
    def calculate_D(h: pd.Series, w: pd.Series):
        return np.diag(
            -w * h * (1 - h)
        )

    @staticmethod
    def _H(X: pd.DataFrame, D: np.array, lambda_: float):
        return X.T.__matmul__(D).__matmul__(X) - lambda_ * np.identity(X.shape[1])

    @staticmethod
    def _z(h: pd.Series, y: pd.Series, w: pd.Series):
        return w * (y - h)

    @staticmethod
    def _gradient(X: pd.DataFrame, z: pd.Series, theta: np.array, lambda_: float):
        return X.T.__matmul__(z) - lambda_ * theta

    @staticmethod
    def _theta_1(theta_0: np.array, H: np.array, gradient: np.array):
        return theta_0 - np.linalg.inv(H).__matmul__(gradient)



