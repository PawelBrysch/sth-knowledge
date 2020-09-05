import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
np.random.seed(1)

earnings = pd.Series(np.random.gamma(shape=2.5, scale=3000, size=1500), name="EARNINGS").apply(lambda x: int(np.round(x, -2)))
earnings = earnings[earnings > 2000]
is_rich = (earnings > earnings.quantile(0.85)).astype(int)
df = pd.DataFrame(earnings).assign(IS_RICH=is_rich)

PROB_RICH_ABROAD = 0.7
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


logreg_0 = LogisticRegression(random_state=0, solver='lbfgs').fit(feature_df[['ABROAD']], feature_df['QUICK_FNSH'])
logreg_1 = LogisticRegression(random_state=0, solver='lbfgs').fit(feature_df[['ABROAD', 'EARNINGS_NORM']], feature_df['QUICK_FNSH'])

# logreg_without.coef_
# logreg_with.coef_

abroad_0 = logreg_0.coef_[0][0]
abroad_1 = logreg_1.coef_[0][0]
earnings_1 = logreg_1.coef_[0][1]

print(abroad_0, abroad_1, earnings_1)
assert (abroad_0, abroad_1, earnings_1) == (0.49082455274035736, 0.29659040631463157, 2.3878329997419536)