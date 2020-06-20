from bs4 import BeautifulSoup
import re
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
import numpy as np


# TODO notka: re.group(i) zwraca wyniki z kolejnych nawiasow z patternu
# TODO znajdz .score() dla regresji liniowej

# NOTE: LDA vs QDA
# NOTE: GDA z CS229 to LDA, bo zaklada, ze covariancje sa takie same dla y=1 i y=2

def get_data_for_linreg(path):
    with open(path, "r") as infile:
        text = infile.read()

    soup = BeautifulSoup(text, "html.parser")
    rows = soup.find_all("tr")
    pattern = re.compile(r"\= \(([\d\.]+), ([\d\.]+)\)")
    text = pd.Series([row.text for row in rows[1:]])
    Xs = text.apply(lambda x: re.search(pattern, x).group(1))
    Ys = text.apply(lambda x: re.search(pattern, x).group(2))
    flag_list = pd.Series([i <= 33 for i in range(80)])
    return pd.DataFrame().assign(X=Xs, Y=Ys, is_red=flag_list)


path_ = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\source\math_linreg2\logreg\test_dataset.html"
data = get_data_for_linreg(path_)
data["X"] = pd.to_numeric(data["X"])
data["Y"] = pd.to_numeric(data["Y"])

X = data.loc[:, ["X", "Y"]]
y = data["is_red"]

logreg = LogisticRegression(random_state=0, solver='lbfgs').fit(X, y)
logreg_score = logreg.score(X, y)
gda = LinearDiscriminantAnalysis().fit(X, y)
gda_score = gda.score(X, y)
result = data.assign(
    Y_true=y,
    logreg=logreg.predict(X),
    gda=gda.predict(X),
    logreg_P=logreg.predict_proba(X)[:, 1],
    gda_P=gda.predict_proba(X)[:, 1])


ref1 = data.loc[:33, :].plot(kind="scatter", x="X", y="Y", color="r")
data.loc[33:, :].plot(kind="scatter", x="X", y="Y", color="b", ax=ref1)

# model = logreg

def get_super_line(model):
    coeff_A = - (model.coef_[0][0] / model.coef_[0][1])
    coeff_B = - (model.intercept_[0] / model.coef_[0][1])
    x = np.linspace(data["X"].min(), data["X"].max(), 100)
    y = coeff_A * x + coeff_B
    return (x, y)


plt.plot(*get_super_line(logreg), label="logreg")
plt.plot(*get_super_line(gda), label="gda")
plt.legend(loc='upper left')