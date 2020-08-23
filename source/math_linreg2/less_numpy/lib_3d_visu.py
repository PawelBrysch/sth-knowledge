import numpy as np


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