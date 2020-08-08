import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math_linreg2.less_sklearn.lib import ModelWrapper

F_BORDER = 0.05
R_BORDER = 0.5

def result(model):
    f_pvalue = model.value_statsmodels.f_pvalue
    rsquared = model.value_statsmodels.rsquared
    print("F: {:.4f}, R: {:.4f}".format(f_pvalue, rsquared))

def get_param(model):
    f_pvalue = model.value_statsmodels.f_pvalue
    rsquared = model.value_statsmodels.rsquared
    return f_pvalue * rsquared

def scatter(model):
    ref = plt.scatter(model.X['Xs'], model.y)
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def get_quaters(Fs_, Rs_):
    global F_BORDER, R_BORDER
    quater1 = 0
    quater2 = 0
    quater3 = 0
    quater4 = 0

    for f, r in zip(Fs_, Rs_):
        if f < F_BORDER:
            if r < R_BORDER:
                quater3 += 1
            else:
                quater2 += 1
        else:
            if r < R_BORDER:
                quater4 += 1
            else:
                quater1 += 1

    return [quater1, quater2, quater3, quater4]

def FR_scatter(Fs_, Rs_):
    plt.scatter(Fs_, Rs_)
    plt.xticks(np.linspace(0, 1, 11))
    plt.yticks(np.linspace(0, 1, 11))
    plt.axvline(x=F_BORDER)
    plt.axhline(y=R_BORDER)




"""###################################
High F, High P (nieprawdziwa precyzja) - ostatecznie nieznaleziony (!)
###################################"""
"""1. Czy istnieje?"""
# Gdy robilismy wykres F(R), to przypadki takie istnialy tylko w sytuacjach lamiacyh regule kciuka (20 sampli na 1 zmienna),
# wiec nie powinna istniec. Pomyslalem sobie: a co jesli mielibysmy "prawie pozioma" linie?
# "pozioma" => high F, "prawie linia" => high R
# Jednak tak nie jest ( o czym nizej).
"""2. "Krecenie" linia wokol poziomu"""
# Z niewiadomych powodow 'R' spada do zera w momencie, gdy linia robi sie prosta.
""""""
# PAR_B = 5
# SAMPLE_SIZE = 10
#
# a_params = np.linspace(-0.5, 0.5, SAMPLE_SIZE + 1)
# f_values = []
# r_squares = []
#
# for PAR_A in a_params:
#     Xs = np.linspace(1, SAMPLE_SIZE, SAMPLE_SIZE)
#     Ys = PAR_A * Xs + PAR_B + np.random.uniform(-0.2, 0.8, (SAMPLE_SIZE))
#     df = pd.DataFrame().assign(Xs=Xs, Ys=Ys)
#     model = ModelWrapper(df, "Ys")
#
#     f_values.append(model.f_value)
#     r_squares.append(model.r_squared)
#
# ax = plt.subplot()
# ax.scatter(a_params, f_values, label="F")
# ax.scatter(a_params, r_squares, label="R")
# ax.legend()


"""###################################
Low F, low P (nieprawdziwa precyzja)
###################################"""
# TODO pokazanie zaleznosc
# TODO przyklad low F, low P - zobaczenie jego residuals_plot

"""Zaleznosc miedyz F i R (szok!)"""
# range_ = {'dim': [2], 'size': [10]}

"""High F, High P (lamie jednak regule kciuka)"""
# range_ = {'dim': [5], 'size': [10]}

"""Low F, low P"""
# range_ = {'dim': [3], 'size': [40]}

"""___________"""
model_example = None
for NO_DIMENSIONS in range_['dim']:
    for SAMPLE_SIZE in range_['size']:

        Fs = []
        Rs = []
        for i in range(300):
            series = {f"X_{i}s": pd.Series(np.random.uniform(0, 10, (SAMPLE_SIZE))) for i in range(NO_DIMENSIONS)}
            df = pd.DataFrame().assign(**series)
            model = ModelWrapper(df, f"X_{NO_DIMENSIONS - 1}s")

            F = model.value_statsmodels.f_pvalue
            R = model.value_statsmodels.rsquared

            Fs.append(F)
            Rs.append(R)

            if F < F_BORDER and R < R_BORDER and model_example is None:
                model_example = model

        # FR_scatter(Fs, Rs)
        # model_example.residuals_against_fitted()
