import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math_linreg2.less_sklearn.lib import ModelWrapper

def result(model):
    f_pvalue = model.value_statsmodels.f_pvalue
    rsquared = model.value_statsmodels.rsquared
    print("F: {:.4f}, R: {:.4f}".format(f_pvalue, rsquared))

def get_param(model):
    f_pvalue = model.value_statsmodels.f_pvalue
    rsquared = model.value_statsmodels.rsquared
    return f_pvalue * rsquared

# TODO to sfajluje, wiec trzeba bedzie naprawic
def scatter(model):
    ref = plt.scatter(model.X['Xs'], model.y)
    # plt.xticks(model.X['Xs'].values)
    # plt.yticks(model.X['Xs'].values)
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# model_calories.value_statsmodels.fvalue        < 5
# model_calories.value_statsmodels.rsquared      > 0.6

#     Xs = pd.Series(np.random.uniform(0, 10, (10)))
#     Ys = pd.Series(np.random.uniform(0, 10, (10)))

#         # TODO dlaczego jest takie duze F-statistic? Czy nie interesuje nas czasem Prob (F-statistic)? - porownac z Jimem.
#           # TODO zrobic prawie plaski wykres. F powinno byc wtedy male


# TODO zrobic drugi przyklad, kiedy beda w ciul liniowo pod duzym katem
    # TODO znalezc prob i bledow przyklad z duzym R
# Xs = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Ys = pd.Series([4.8, 5.2, 4.9, 5.1, 5.2, 5.3, 4.8, 4.9, 5.0, 5.0])

params = []


Fs = []
Rs = []

SAMPLE_SIZE = 10

for i in range(300):
    # TODO sparametryzuj
    Xs = pd.Series(np.random.uniform(0, 10, (SAMPLE_SIZE)))
    Ys = pd.Series(np.random.uniform(0, 10, (SAMPLE_SIZE)))
    Zs = pd.Series(np.random.uniform(0, 10, (SAMPLE_SIZE)))
    Z1s = pd.Series(np.random.uniform(0, 10, (SAMPLE_SIZE)))

    df = pd.DataFrame().assign(Xs=Xs, Ys=Ys, Zs=Zs, Z1s=Z1s)
    model = ModelWrapper(df, "Z1s")

    param = get_param(model)
    # params.append(param)
    # result(model)

    F = model.value_statsmodels.f_pvalue
    R = model.value_statsmodels.rsquared

    Fs.append(F)
    Rs.append(R)

    # if 0.1 < F < 0.9 and 0.5 < R < 0.9:
    #     print("OK!")
    #     scatter(model)
    #     result(model)
    #     # model.value_statsmodels.summary()
    #     break

# TODO policzenie procentow

plt.scatter(Fs, Rs)
plt.xticks(np.linspace(0, 1, 11))
plt.yticks(np.linspace(0, 1, 11))
plt.axvline(x=0.05)
plt.axhline(y=0.5)