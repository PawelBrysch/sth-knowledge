from scipy.stats import norm, t
import statistics
from math import sqrt

norm.cdf(1.76)
norm.ppf(0.95)
norm.ppf(0.975)
norm.ppf(0.05)
norm.ppf(0.025)

t.cdf(0, 11)
t.ppf(0.95, 3)

alis = [3.58, 10.03, 4.77, 14.66]

mean = statistics.mean(alis)
variance = statistics.variance(alis)
pvariance = statistics.pvariance(alis)

class Field:
    def __init__(self, m, sd , n):
        self.mean = m
        self.variance = sd ** 2
        self.n = n


field_A = Field(1.3, 0.5, 22)
field_B = Field(1.6, 0.3, 24)

alpha = 0.05
t = (field_A.mean - field_B.mean) / sqrt(
    field_A.variance/field_A.n + field_B.variance/field_B.n
)

