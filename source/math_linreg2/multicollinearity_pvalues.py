from scipy.stats import norm

beta = 3

# Variance is increasing => p values are getting high
for var in [0.1, 0.5, 1, 5, 10, 50, 100, 500, 1000]:
    p_value_1sided = 1 - norm(0, var).cdf(beta)
    p_value_2sided = 2 * norm(0, var).cdf(-abs(beta))
    print("{:<25} {}".format(p_value_1sided, p_value_2sided))
