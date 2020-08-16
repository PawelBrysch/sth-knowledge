import pytest
from .logreg_newton import Step, weights, func_H
import pandas as pd
import numpy as np


class TestName:
    def test_func_H(self):
        THETA_0 = np.array([-1, 2, 1])

        assert func_H(2, 3, THETA_0) == 0.9975273768433653
        assert func_H(1, 4, THETA_0) == 0.9933071490757153

    def test_calculate_h(self):
        THETA_0 = np.array([-1, 2, 1])
        small_testdata = pd.DataFrame.from_dict({
            'Y': [0, 0],
            'X1': [2, 1],
            'X2': [3, 4],
        })
        res = Step.calculate_h(small_testdata, THETA_0)
        pd.testing.assert_series_equal(res, pd.Series([0.99752738, 0.99330715]))


    def test_calculate_D(self):
        h1 = pd.Series([4, 5, 6])
        w1 = pd.Series([3, 2, 1])

        res = Step.calculate_D(h1, w1)
        np.testing.assert_array_equal(res, np.array([[36,  0,  0], [0, 40,  0], [0,  0, 30]]))


    def test_H(self):
        X1 = pd.DataFrame.from_dict({
            'X1': [1, 3, 5],
            'X2': [2, 4, 6],
        })
        D1 = np.diag([1, 2, -1])
        lambda1 = 0.5

        res = Step._H(X1, D1, lambda1)
        np.testing.assert_array_equal(res, np.array([[-6.5, -4.], [-4., -0.50]]))

    def test_z(self):
        h1 = pd.Series([1, 2, 3])
        y1 = pd.Series([6, 5, 4])
        w1 = pd.Series([2, 4, 6])

        res = Step._z(h1, y1, w1)
        np.testing.assert_array_equal(res, np.array([10, 12, 6]))

    def test_gradient(self):
        X1 = pd.DataFrame.from_dict({
            'X1': [1, 3, 5],
            'X2': [2, 4, 6],
        })
        z1 = pd.Series([1, 0, -1])
        theta1 = np.array([-2, 2])
        lambda1 = 0.5

        res = Step._gradient(X1, z1, theta1, lambda1)
        np.testing.assert_array_equal(res, np.array([-3., -5.]))

    def test_theta_1(self):
        H1 = np.array([[1, 2], [3, 4]])
        gradient1 = np.array([1, -1])
        theta_00 = np.array([1, 1])

        res = Step._theta_1(theta_00, H1, gradient1)
        np.testing.assert_array_almost_equal(res, np.array([4., -1.]))


