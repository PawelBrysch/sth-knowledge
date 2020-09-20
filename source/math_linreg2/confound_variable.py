import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.linear_model import LogisticRegression
from math_linreg2.less_matplotlib.lib_lines import get_line_data
import matplotlib.pyplot as plt
np.random.seed(1)

"""
Myslalem, ze fajnie stworzylem dataset, a tu dupa. Regresja logistyczna jest 'glupia' Trzeba bedzie chyba pokombinowac w 
strone regresji liniowej (chociaz tam algo to same i tez nie powinno zadzialac, ALE warto sprawdzic!) albo w ogole nie 
kategoryzowac. Albo wymyslec calkiem inne dane.
"""

PROB_RICH_ABROAD = 0.7
PROB_POOR_ABROAD = 0.15
PROB_RICH_QUICK = 0.95
PROB_POOR_QUICK = 0.7
RICH_QUANTILE = 0.85


earnings = pd.Series(np.random.gamma(shape=2.5, scale=3000, size=1500), name="EARNINGS").apply(lambda x: int(np.round(x, -2)))
earnings = earnings[earnings > 2000]
is_rich = (earnings > earnings.quantile(RICH_QUANTILE)).astype(int)
df = pd.DataFrame(earnings).assign(IS_RICH=is_rich)

def get_abroad(single_row_df: pd.DataFrame):
    if single_row_df['IS_RICH']:
        prob_abroad = PROB_RICH_ABROAD
    else:
        prob_abroad = PROB_POOR_ABROAD
    return np.random.binomial(1, prob_abroad)

def get_finish_quick(single_row_df: pd.DataFrame):
    if single_row_df['IS_RICH']:
        prob_finish_quick = PROB_RICH_QUICK
    else:
        prob_finish_quick = PROB_POOR_QUICK
    return np.random.binomial(1, prob_finish_quick)

df = df.assign(
    ABROAD=df.apply(get_abroad, axis=1),
    QUICK_FNSH=df.apply(get_finish_quick, axis=1)
)

feature_df = df.assign(
    EARNINGS_NORM=MinMaxScaler().fit_transform(df[['EARNINGS']]).flatten()
).drop(['EARNINGS', 'IS_RICH'], axis=1)



def split(data: pd.DataFrame):
    return data[["ABROAD", "EARNINGS_NORM"]], data["QUICK_FNSH"]

def visualize(data: pd.DataFrame, model: LogisticRegression, ax):
    _MIN, _MAX = -1, 2
    _MIN, _MAX = 2 * _MIN, 1.5 * _MAX

    ax.axis(xmin=_MIN, xmax=_MAX)
    ax.axis(ymin=_MIN, ymax=_MAX)

    Y1, Y0 = [x for _, x in data.groupby(data['QUICK_FNSH'] < 0.5)]
    Y1.plot(kind="scatter", x="ABROAD", y="EARNINGS_NORM", color="r", ax=ax)
    Y0.plot(kind="scatter", x="ABROAD", y="EARNINGS_NORM", color="b", ax=ax)
    line_data = get_line_data(model=model, axes=ax)
    ax.plot(*line_data, label="orig", color='g')

data_bad = feature_df
X_bad, y_bad = split(data_bad)
logreg_bad = LogisticRegression(random_state=0, solver='lbfgs').fit(X_bad, y_bad)
score_bad = logreg_bad.score(X_bad, y_bad)
data_bad = data_bad.assign(SCORE=logreg_bad.predict(X_bad))
print("SCORE: ", data_bad['SCORE'].mean())

"""visualize"""
fig, ax = plt.subplots(1, 1)
visualize(data_bad, logreg_bad, ax)
