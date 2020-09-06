import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from math_linreg2.less_matplotlib.lib_lines import get_line_data

np.random.seed(1)

earnings = pd.Series(np.random.gamma(shape=2.5, scale=3000, size=1500), name="EARNINGS").apply(lambda x: int(np.round(x, -2)))
earnings = earnings[earnings > 2000]
is_rich = (earnings > earnings.quantile(0.85)).astype(int)
df = pd.DataFrame(earnings).assign(IS_RICH=is_rich)

PROB_RICH_ABROAD = 0.7
# PROB_POOR_ABROAD = 0.15
PROB_POOR_ABROAD = 0.15
PROB_RICH_QUICK = 0.95
PROB_POOR_QUICK = 0.7

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

"""prod"""
# logreg_0 = LogisticRegression(random_state=0, solver='lbfgs').fit(feature_df[['ABROAD']], feature_df['QUICK_FNSH'])
# logreg_1 = LogisticRegression(random_state=0, solver='lbfgs').fit(feature_df[['ABROAD', 'EARNINGS_NORM']], feature_df['QUICK_FNSH'])
# abroad_0 = logreg_0.coef_[0][0]
# abroad_1 = logreg_1.coef_[0][0]
# earnings_1 = logreg_1.coef_[0][1]

"""print coeffs"""
# print(abroad_0, abroad_1, earnings_1)
# assert (abroad_0, abroad_1, earnings_1) == (0.49082455274035736, 0.29659040631463157, 2.3878329997419536)

"""predict little sample"""
# test_sample = pd.DataFrame.from_dict({
#     'EARNINGS_NORM': [0.8, 0.2],
#     'STUDY_ABROAD': [0, 1]
# })
# logreg_1.predict(test_sample)


def split(data: pd.DataFrame):
    return data[["ABROAD", "EARNINGS_NORM"]], data["QUICK_FNSH"]

def visualize(data: pd.DataFrame, model: LogisticRegression, ax):
    ax.axis(xmin=-1, xmax=2)
    ax.axis(ymin=-1, ymax=2)

    Y1, Y0 = [x for _, x in data.groupby(data['QUICK_FNSH'] < 0.5)]
    Y1.plot(kind="scatter", x="ABROAD", y="EARNINGS_NORM", color="r", ax=ax)
    Y0.plot(kind="scatter", x="ABROAD", y="EARNINGS_NORM", color="b", ax=ax)
    line_data = get_line_data(model=model, axes=ax)
    ax.plot(*line_data, label="orig", color='g')

# TODO 1. obliczac procent i wypisywac
"""##########################
BADANIE
#########################"""
data_good = pd.read_pickle("/home/devoted/PROJECTS/sth_knowledge_top/sth-knowledge/source/math_linreg2/snippets/data/confound_variable_v3_perfect.pickle")
data_bad = feature_df[['ABROAD', 'EARNINGS_NORM', "QUICK_FNSH"]]

X_good, y_good = split(data_good)
X_bad, y_bad = split(data_bad)

logreg_good = LogisticRegression(random_state=0, solver='lbfgs').fit(X_good, y_good)
logreg_bad = LogisticRegression(random_state=0, solver='lbfgs').fit(X_bad, y_bad)

score_good = logreg_good.score(X_good, y_good)
score_bad = logreg_bad.score(X_bad, y_bad)

data_good = data_good.assign(SCORE=logreg_good.predict(X_good))
data_bad = data_bad.assign(SCORE=logreg_bad.predict(X_bad))

print(score_good, score_bad)

"""visualize"""
fig, (ax1, ax2) = plt.subplots(1, 2)

visualize(data_good, logreg_good, ax1)
visualize(data_bad, logreg_bad, ax2)
