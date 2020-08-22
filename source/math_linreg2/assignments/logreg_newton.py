import pathlib as pl
import pandas as pd
import numpy as np
from typing import List
import matplotlib.pyplot as plt
from math_linreg2.less_matplotlib.lib_lines import get_line_data



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

    def __init__(self, theta0, algorithm):
        self.theta0 = theta0
        self.algorithm = algorithm


    def calculate_next_theta(self):
        w = Step._w(self.algorithm.X1, self.algorithm.X2, self.algorithm.x, self.algorithm.tau)
        h = Step._h(self.algorithm.X1, self.algorithm.X2, self.theta0)
        z = Step._z(h, self.algorithm.Y, w)
        gradient = Step._gradient(self.algorithm.X, z, self.theta0, self.algorithm.lambda_)
        D = Step._D(h, w)
        H = Step._H(self.algorithm.X, D, self.algorithm.lambda_)
        self.theta1 = Step._theta_1(self.theta0, H, gradient)

    def perform(self, no_steps):
        self.calculate_next_theta()
        self.algorithm.steps.append(self)
        no_steps -= 1
        if no_steps >= 1:
            next_step = Step(self.theta1, self.algorithm)
            next_step.perform(no_steps)


class Algorithm:
    def __init__(self, data, theta0, lambda_, tau, x, no_steps):
        self.X = data.loc[:, ['X0', 'X1', 'X2']]
        self.X1 = data['X1']
        self.X2 = data['X2']
        self.Y = data['Y']
        self.lambda_ = lambda_
        self.tau = tau
        self.x = x

        self.steps = []
        self.theta0 = theta0
        self.no_steps = no_steps

    def execute(self):
        first_step = Step(self.theta0, self)
        first_step.perform(self.no_steps)

    @property
    def success(self):
        thetas = [elem.theta0 for elem in self.steps]
        return np.allclose(thetas[-2], thetas[-1])

    @property
    def result(self):
        thetas = [elem.theta0 for elem in self.steps]
        return thetas[-1]



data_ = pt2.assign(X1=pt1['X1'], X2=pt1['X2'])
data_ = data_.assign(X0=pd.Series(np.ones(data_.shape[0])))
# TODO zmieniaj barwy powoli, by dostac 'ruch'
x_avg = [-0.065, 0.015]
# x_avg = [0, -10]

# algo = Algorithm(data=data_, theta0=np.array([1, 1, 1]), lambda_=0.0001, tau=0.5, x=x_avg, no_steps=8)
# algo.execute()
# print(algo.success)
results = []
for tau in [0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10, 50]:
    algo = Algorithm(data=data_, theta0=np.array([1, 1, 1]), lambda_=0.0001, tau=tau, x=x_avg, no_steps=8)
    algo.execute()
    # print(algo.success)
    results.append(algo.result)
# TODO jak algorytm ma sie skonczyc
# result = [elem.theta0 for elem in algo.steps]
# np.allclose(result[6], result[7])

"""logreg"""
from sklearn.linear_model import LogisticRegression
X = data_.loc[:, ['X1', 'X2']]
y = data_['Y']
logreg = LogisticRegression(random_state=0, solver='lbfgs').fit(X, y)

"""plot"""
# TODO zrobic fajne kolorki
Y1, Y0 = [x for _, x in data_.groupby(data_['Y'] < 0.5)]
ref1 = Y1.plot(kind="scatter", x="X1", y="X2", color="r")
Y0.plot(kind="scatter", x="X1", y="X2", color="b", ax=ref1)
plt.plot(*get_line_data(model=logreg, axes=ref1), label="orig")
for i, theta_ in enumerate(results):
    plt.plot(*get_line_data(theta=theta_, axes=ref1), label=f"{i}")
plt.legend(loc='upper left')
plt.annotate(xy=x_avg, xytext=x_avg, text='X')