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



"""##########################
GOOD
#########################"""
data = pd.read_pickle("/home/devoted/PROJECTS/sth_knowledge_top/sth-knowledge/source/math_linreg2/snippets/data/confound_variable.pickle")
data["X"] = pd.to_numeric(data["X"])
data["Y"] = pd.to_numeric(data["Y"])

X = data[["X", "Y"]]
y = data["is_red"]

data2 = pd.DataFrame().assign(
    ABROAD=data['X'],
    EARNINGS_NORM=data['Y'],
    QUICK_FINISH=data['is_red']
)

logreg = LogisticRegression(random_state=0, solver='lbfgs').fit(X, y)

fig, ax = plt.subplots(1, 1)

data.loc[:33, :].plot(kind="scatter", x="X", y="Y", color="r", ax=ax)
data.loc[33:, :].plot(kind="scatter", x="X", y="Y", color="b", ax=ax)
# data.loc[:33, :].plot(kind="scatter", x="ABROAD", y="EARNINGS_NORM", color="r", ax=ax)
# data.loc[33:, :].plot(kind="scatter", x="ABROAD", y="EARNINGS_NORM", color="b", ax=ax)
plt.plot(*get_line_data(model=logreg, axes=ax), label="logreg")

plt.legend(loc='upper left')


"""##########################
BAD
#########################"""
# X = feature_df[['ABROAD', 'EARNINGS_NORM']]
# y = feature_df['QUICK_FNSH']
# logreg_test = LogisticRegression(random_state=0, solver='lbfgs').fit(X, y)
# res_test = logreg_test.predict_proba(X)
# score_test = logreg_test.score(X, y)
#
# fig, ax = plt.subplots(1, 1)
# Y1, Y0 = [x for _, x in feature_df.groupby(feature_df['QUICK_FNSH'] < 0.5)]
# Y1.plot(kind="scatter", x="ABROAD", y="EARNINGS_NORM", color="r", ax=ax)
# Y0.plot(kind="scatter", x="ABROAD", y="EARNINGS_NORM", color="b", ax=ax)
# ax.axis(xmin=-1, xmax=2)
# ax.axis(ymin=-1, ymax=2)
# # ax.ylim([-1, 2])
# line_data = get_line_data(model=logreg_test, axes=ax)
# ax.plot(*line_data, label="orig", color='g')
# # ax.plot(*get_line_data(model=logreg_test, axes=ax), label="orig", color='g')
