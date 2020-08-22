from bs4 import BeautifulSoup
import re
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
import numpy as np
import pathlib as pl
from math_linreg2.less_matplotlib.lib_lines import get_line_data


def parse_data(path):
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

# create df
# path_ = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\source\math_linreg2\logreg\test_dataset.html"
path_ = pl.Path.cwd().joinpath("data").joinpath("logreg_vs_gda.html")
data = parse_data(path_)
data["X"] = pd.to_numeric(data["X"])
data["Y"] = pd.to_numeric(data["Y"])

# fit models
X = data.loc[:, ["X", "Y"]]
y = data["is_red"]
logreg = LogisticRegression(random_state=0, solver='lbfgs').fit(X, y)
gda = LinearDiscriminantAnalysis().fit(X, y)

# fast scoring
logreg_score = logreg.score(X, y)
gda_score = gda.score(X, y)

# check how observations has been divided
result = data.assign(
    Y_true=y,
    logreg=logreg.predict(X),
    gda=gda.predict(X),
    logreg_P=logreg.predict_proba(X)[:, 1],
    gda_P=gda.predict_proba(X)[:, 1])

# plot results
ref1 = data.loc[:33, :].plot(kind="scatter", x="X", y="Y", color="r")
data.loc[33:, :].plot(kind="scatter", x="X", y="Y", color="b", ax=ref1)
plt.plot(*get_line_data(model=logreg, axes=ref1), label="logreg")
plt.plot(*get_line_data(model=gda, axes=ref1), label="gda", color='0.9')
plt.legend(loc='upper left')