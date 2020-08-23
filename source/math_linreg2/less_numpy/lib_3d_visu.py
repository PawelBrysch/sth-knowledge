import numpy as np
import pandas as pd

def adjust_to_fromfunction(func, x_array, y_array, **kwargs):
    class LinearFunction:
        def __init__(self, image):
            self.min_ = image.min()
            self.step = (image.max() - self.min_) / (image.size - 1)

        def evaluate(self, arg):
            return self.min_ + arg * self.step

    x_func = LinearFunction(x_array)
    y_func = LinearFunction(y_array)

    def wrapper(x, y):
        print("Do sth")
        return func(x_func.evaluate(x), y_func.evaluate(y), **kwargs)

    return wrapper


def some_func(x, y):
    return x ** 2 * y


def cartesian_map(Xs: pd.Series, Ys: pd.Series, func):
    def series_accepting(func_):
        def wrapper(series):
            return func_(series['X'], series['Y'])
        return wrapper


    Xs = pd.Series(Xs, name='X')
    Ys = pd.Series(Ys, name='Y')
    func = series_accepting(func)

    combinations = Xs.to_frame().assign(key=1).\
        merge(Ys.to_frame().assign(key=1), on='key')
    map_ = combinations.apply(func, axis=1).\
        values.reshape(Xs.size, Ys.size)
    return map_

"""test"""
# def trivial_sum(x: int, y: int):
#     return x + y
#
# Xs = pd.Series([1, 2, 3])
# Ys = pd.Series([10, 20, 30, 40])
#
# np.testing.assert_array_equal(cartesian_map(Xs, Ys, trivial_sum), np.array([[11, 21, 31, 41], [12, 22, 32, 42], [13, 23, 33, 43]]))




# X_MIN = 2
# X_MAX = 4
#
# Y_MIN = 4
# Y_MAX = 6
#
# PRECISION_X = 11
# PRECISION_Y = 5
#
# x_series = np.linspace(X_MIN, X_MAX, PRECISION_X)
# y_series = np.linspace(Y_MIN, Y_MAX, PRECISION_Y)
#
# some_func_adjusted = adjust_to_fromfunction(some_func, x_series, y_series)
#
# z = np.fromfunction(some_func_adjusted, (x_series.size, y_series.size), dtype=int)