from sklearn.linear_model import LinearRegression
import pandas as pd
import os

df = pd.read_excel(
    io=os.path.abspath("data_preparing.xlsx"),
    header=0,
    usecols="C:F",
    nrows=20
)

X = df.iloc[:, :-1]
y = df["calories"]

reg = LinearRegression().fit(X, y)
print(reg.coef_)

