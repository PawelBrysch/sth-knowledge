import pandas as pd
from sklearn.linear_model import LogisticRegression
from math_linreg2.less_matplotlib.lib_lines import get_line_data
import matplotlib.pyplot as plt

"""
W ogole nie rozumiem dalczego regresja logistyczna wybrala taka glupia linie (wykres po prawej). Przeciez na oko widac 
linie, ktore to lepiej rodziela.
Rozkmina tej kwestii wniesie na pwno bardzo duzo do rozumienia regresji logistycznej.
"""
# TODO sproboj na pale znalezc lepsza linie (czyli taka, ktora lepiej rozdzieli).
    # TODO policz dla znalezionej linii oraz dla pierwotnej linii ich "loss functions"

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

data_bad = pd.read_pickle("/home/devoted/PROJECTS/sth_knowledge_top/sth-knowledge/source/math_linreg2/snippets/data/mean_sample")
data_good = pd.read_pickle("/home/devoted/PROJECTS/sth_knowledge_top/sth-knowledge/source/math_linreg2/snippets/data/equi_distributed_sample")

X_good, y_good = split(data_good)
X_bad, y_bad = split(data_bad)

logreg_good = LogisticRegression(random_state=0, solver='lbfgs').fit(X_good, y_good)
logreg_bad = LogisticRegression(random_state=0, solver='lbfgs').fit(X_bad, y_bad)

score_good = logreg_good.score(X_good, y_good)
score_bad = logreg_bad.score(X_bad, y_bad)

data_good = data_good.assign(SCORE=logreg_good.predict(X_good))
data_bad = data_bad.assign(SCORE=logreg_bad.predict(X_bad))

print("SCORE: ", data_bad['SCORE'].mean())

"""visualize"""
fig, (ax1, ax2) = plt.subplots(1, 2)
visualize(data_good, logreg_good, ax1)
visualize(data_bad, logreg_bad, ax2)