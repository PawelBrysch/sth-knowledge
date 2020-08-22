import numpy as np
import pandas as pd

def get_line_data(model=None, theta=None, axes=None):
    if theta is not None and model is None:
        coef_ = [[theta[1], theta[2]]]
        intercept_ = [theta[0]]
    elif theta is None and model is not None:
        coef_ = model.coef_
        intercept_ = model.intercept_
    else:
        raise TypeError('Wrong arguments, buddy.')

    coeff_A = - (coef_[0][0] / coef_[0][1])
    coeff_B = - (intercept_[0] / coef_[0][1])
    x = np.linspace(*axes.get_xlim(), 100)
    y = coeff_A * x + coeff_B
    df = pd.DataFrame().assign(X=x, Y=y)
    df = df[(df.Y > axes.get_ylim()[0]) & (df.Y < axes.get_ylim()[1])]
    return (df['X'], df['Y'])