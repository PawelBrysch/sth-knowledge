import pytest
from .logreg_newton import Step
import pandas as pd
import numpy as np


class TestName:
    def test_w(self):
        X1_ = pd.Series([2, 1])
        X2_ = pd.Series([3, 4])
        x_ = [5, 5]
        tau_ = 0.5

        res = Step._w(X1_, X2_, x_, tau_)
        pd.testing.assert_series_equal(res, pd.Series([0.00073834, 0.00026225]))

    def test_h(self):
        THETA_0 = np.array([-1, 2, 1])
        X1 = pd.Series([2, 1])
        X2 = pd.Series([3, 4])

        res = Step._h(X1, X2, THETA_0)
        pd.testing.assert_series_equal(res, pd.Series([0.99752738, 0.99330715]))


    def test_D(self):
        h = pd.Series([4, 5, 6])
        w = pd.Series([3, 2, 1])

        res = Step._D(h, w)
        np.testing.assert_array_equal(res, np.array([[36,  0,  0], [0, 40,  0], [0,  0, 30]]))


    def test_H(self):
        X = pd.DataFrame.from_dict({
            'X1': [1, 3, 5],
            'X2': [2, 4, 6],
        })
        D = np.diag([1, 2, -1])
        lambda1 = 0.5

        res = Step._H(X, D, lambda1)
        np.testing.assert_array_equal(res, np.array([[-6.5, -4.], [-4., -0.50]]))

    def test_z(self):
        h = pd.Series([1, 2, 3])
        y = pd.Series([6, 5, 4])
        w = pd.Series([2, 4, 6])

        res = Step._z(h, y, w)
        np.testing.assert_array_equal(res, np.array([10, 12, 6]))

    def test_gradient(self):
        X = pd.DataFrame.from_dict({
            'X1': [1, 3, 5],
            'X2': [2, 4, 6],
        })
        z = pd.Series([1, 0, -1])
        theta = np.array([-2, 2])
        lambda_ = 0.5

        res = Step._gradient(X, z, theta, lambda_)
        np.testing.assert_array_equal(res, np.array([-3., -5.]))

    def test_theta_1(self):
        H = np.array([[1, 2], [3, 4]])
        gradient = np.array([1, -1])
        theta_0 = np.array([1, 1])

        res = Step._theta_1(theta_0, H, gradient)
        np.testing.assert_array_almost_equal(res, np.array([4., -1.]))


