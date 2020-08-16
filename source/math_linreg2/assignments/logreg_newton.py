import pathlib as pl
import pandas as pd
import numpy as np
from typing import List

"""notatka"""
# X.__matmul__(X.T)
# np.identity(X.__len__())

x = pl.Path(__file__).with_name('x.dat')
y = pl.Path(__file__).with_name('y.dat')
pt1 = pd.read_csv(x, sep=r'\s{2,}', engine='python')
pt2 = pd.read_csv(y, sep=r'\s{2,}', engine='python')




class Step:
    @staticmethod
    def _w(X1: pd.Series, X2: pd.Series, arg_x: List[int], tau: float):
        return np.exp(-np.sqrt((X1 - arg_x[0]) ** 2 + (X2 - arg_x[1]) ** 2) / (2 * tau ** 2))

    @staticmethod
    def _h(X1: pd.Series, X2: pd.Series, theta: np.array):
        return 1 / (
                1 + np.exp(
                    -(theta[0] + X1 * theta[1] + X2 * theta[2])
                )
        )

    @staticmethod
    def _D(h: pd.Series, w: pd.Series):
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

    def __init__(self, data, theta0, lambda_, tau, x):
        self.X = data.loc[:, ['X0', 'X1', 'X2']]
        self.X1 = data['X1']
        self.X2 = data['X2']
        self.Y = data['Y']
        self.lambda_ = lambda_
        self.tau = tau
        self.x = x

        self.theta0 = theta0


    def next_theta(self):
        w = Step._w(self.X1, self.X2, self.x, self.tau)
        h = Step._h(self.X1, self.X2, self.theta0)
        z = Step._z(h, self.Y, w)
        gradient = Step._gradient(self.X, z, self.theta0, self.lambda_)
        D = Step._D(h, w)
        H = Step._H(self.X, D, self.lambda_)
        next_theta = Step._theta_1(self.theta0, H, gradient)

        return next_theta

class Algorithm:
    def __init__(self, data, theta0, lambda_, tau, x):
        self.X = data.loc[:, ['X0', 'X1', 'X2']]
        self.X1 = data['X1']
        self.X2 = data['X2']
        self.Y = data['Y']
        self.lambda_ = lambda_
        self.tau = tau
        self.x = x

        self.steps = []
        self.step1 = Step(data=data_, theta0=np.array([1, 1, 1]), lambda_=0.0001, tau=0.5, x=x_avg)
        self.theta0 = theta0


data_ = pt2.assign(X1=pt1['X1'], X2=pt1['X2'])
data_ = data_.assign(X0=pd.Series(np.ones(data_.shape[0])))
x_avg = [-0.065, 0.015]


algo = Algorithm(data=data_, theta0=np.array([1, 1, 1]), lambda_=0.0001, tau=0.5, x=x_avg)
res = algo.step1.next_theta()
print(res)

# step1 = Step(data=data_, theta0=np.array([1, 1, 1]), lambda_=0.0001, tau=0.5, x=x_avg)
# res = step1.next_theta()
# print(res)