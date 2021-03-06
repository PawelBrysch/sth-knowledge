import json
import random
import numpy as np
import scipy.integrate as integrate
from math import sqrt
from matplotlib.pyplot import scatter
from matplotlib.pyplot import hist
from math_linreg2.less_scipy.main import RandomObservationGenerator

def create_framework_matrix(height, first_line_length):
    h = height
    len0 = first_line_length
    sqrt3 = sqrt(3)

    low1 = [0, h]
    low2 = [(0.5 + sqrt3) * len0, h]
    low3 = [(1.5 + 3 * sqrt3) * len0, h]
    low4 = [(3 + 6 * sqrt3) * len0, h]

    high1 = [0.5 * len0, sqrt3 * len0 + h]
    high2 = [(1.5 + 1 * sqrt3) * len0, 2 * sqrt3 * len0 + h]
    high3 = [(3 + 3 * sqrt3) * len0, 3 * sqrt3 * len0 + h]

    retval = np.array([
        low1,
        high1,
        low2,
        high2,
        low3,
        high3,
        low4
    ])
    return retval


class CustomPDF:
    def __init__(self, height, first_line_length):
        self.framework_matrix = create_framework_matrix(height, first_line_length)

    @property
    def min_(self):
        return 0

    @property
    def max_(self):
        return self.framework_matrix[-1, 0]

    def function_(self, object_):
        idx = np.searchsorted(self.framework_matrix[:, 0], object_)

        x1 = self.framework_matrix[idx - 1, 0]
        y1 = self.framework_matrix[idx - 1, 1]
        x2 = self.framework_matrix[idx, 0]
        y2 = self.framework_matrix[idx, 1]

        y = (y1 - y2) * (object_ - x1) / (x1 - x2) + y1

        return y

    def pdf(self, arg_):
        if arg_ < 0 or arg_ > self.framework_matrix[-1, 0]:
            return 0
        else:
            return self.function_(arg_)


custom_pdf = CustomPDF(0.1, 0.16908)

""" boundaries """
# scatter(custom_pdf.framework_matrix[:, 0], custom_pdf.framework_matrix[:, 1])

""" sketch of distribution """
# X_VALUES = [random.randint(0, 10 * int(custom_pdf.max_)) / 10 for i in range(100000)]
# Y_VALUES = custom_pdf.function_(X_VALUES)
# data = np.array([X_VALUES, Y_VALUES]).T
# scatter(data[:, 0], data[:, 1])

""" integral == 1"""
# integral = integrate.quad(lambda x: custom_pdf.pdf(x), 0, custom_pdf.max_)[0]

""" random sample generation """
# helper = CustomPDF(0.1, 0.16908)
# some_gen = RandomObservationGenerator(helper.pdf, helper.min_, helper.max_)
# some_list = [next(some_gen) for i in range(500)]
# hist(some_list, bins=20)



