import pathlib as pl
import pandas as pd
import numpy as np
from typing import List
import matplotlib.pyplot as plt
from math_linreg2.less_matplotlib.lib_lines import get_line_data
from sklearn.linear_model import LogisticRegression
from math_linreg2.less_numpy.lib_3d_visu import adjust_to_fromfunction, cartesian_map




"""notatka"""
# TODO przenies gdzies
# X.__matmul__(X.T)
# np.identity(X.__len__())

"""parsing"""
path_to_x = pl.Path(__file__).with_name('x.dat')
path_to_y = pl.Path(__file__).with_name('y.dat')
pt1 = pd.read_csv(path_to_x, sep=r'\s{2,}', engine='python')
pt2 = pd.read_csv(path_to_y, sep=r'\s{2,}', engine='python')
DF = pt2.assign(X1=pt1['X1'], X2=pt1['X2'])
DF = DF.assign(X0=pd.Series(np.ones(DF.shape[0])))



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



# CENTER_X = [-0.065, 0.015]
# TODO Experiment(tau=0.01) -> dodstaje thete -> predyktuje thete
class Experiment2:
    def __init__(self, tau):
        self.tau = tau

    def predict(self, x1, x2):
        theta = self._get_theta([x1, x2])
        result = Step._h(x1, x2, theta)
        return result

    def _get_theta(self, x):
        algo = Algorithm(data=DF, theta0=np.array([1, 1, 1]), lambda_=0.0001, tau=self.tau, x=x, no_steps=8)
        algo.execute()
        return algo.result

# TODO [0.01, 0.05, 0.1, 0.5, 1, 5]
exp = Experiment2(0.05)

"""test"""
# np.testing.assert_array_almost_equal(exp._get_theta([-0.75, 0.75]), np.array([0.25687919,  4.24842454, -0.66492687]))
# np.testing.assert_almost_equal(exp.predict(-0.75, 0.75), 0.03142767246588209)


LENGTH = 20

Ys = np.linspace(DF['X2'].min(), DF['X2'].max(), LENGTH)
Xs = np.linspace(DF['X1'].min(), DF['X1'].max(), LENGTH)
Zs = cartesian_map(Xs, Ys, exp.predict)








# TODO wdupienie reszty
    # TODO zwielokrotnienie


"""logreg"""
logreg = LogisticRegression(random_state=0, solver='lbfgs').fit(DF.loc[:, ['X1', 'X2']], DF['Y'])

"""plot"""
Y1, Y0 = [x for _, x in DF.groupby(DF['Y'] < 0.5)]
fig, ax1 = plt.subplots(1, 1)

ref1 = ax1.contourf(
    Ys, Xs, Zs.T,
    # levels=np.array([0., 0.5, 1.]), cmap=plt.get_cmap('PiYG')
    levels=np.array([0., 0.5, 1.]), cmap=plt.get_cmap('coolwarm')
)
plt.colorbar(ref1, ax=ax1)
ax1.set_title(f'{exp.tau}')

Y1.plot(kind="scatter", x="X1", y="X2", color="r", ax=ax1)
Y0.plot(kind="scatter", x="X1", y="X2", color="b", ax=ax1)
ax1.plot(*get_line_data(model=logreg, axes=ax1), label="orig", color='g')
ax1.legend(loc='upper left')



