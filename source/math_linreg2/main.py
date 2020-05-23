from sklearn.linear_model import LinearRegression
import pandas as pd
import os
from yellowbrick.regressor import ResidualsPlot

def linreg_wrapper(df, output_column):
    X = df.iloc[:, :-1]
    y = df[output_column]
    reg = LinearRegression().fit(X, y)
    return reg

class Experiment:
    def __init__(self, df, output_column, column_to_exclude=None):
        self.df_with = df
        self.reg_with = linreg_wrapper(self.df_with, output_column)

        self.reg_without = None
        if column_to_exclude is not None:
            self.df_without = df.drop([column_to_exclude], axis="columns")
            self.reg_without = linreg_wrapper(self.df_without, output_column)

    def __repr__(self):
        regs = list(filter(None, [self.reg_with, self.reg_without]))
        reprs = [f"{reg.coef_} {reg.intercept_}" for reg in regs]
        return "\n".join(reprs)


df_calories = pd.read_excel(io=os.path.abspath("data/calories.xlsx"), header=0, usecols="C:F", nrows=80)
df_density_big = pd.read_excel(io=os.path.abspath("data/confoundOmitted_bigIntercept.xlsx"), header=0, usecols="C:E", nrows=80)
df_density_small = pd.read_excel(io=os.path.abspath("data/nearlyPerfectlyCorrelatedConfoundOmitted_smallIntercept.xlsx"), header=0, usecols="C:F", nrows=80)


exp_calories = Experiment(df_calories, "calories")
exp_density_big = Experiment(df_density_big, "bone density", "weight")
exp_density_small = Experiment(df_density_small, "bone density", "years")

# TODO Resolve FutureWarning

visualizer = ResidualsPlot(exp_calories.reg_with)
df = exp_calories.df_with
output_column = "calories"
X = df.iloc[:, :-1]
y = df[output_column]
visualizer.score(X, y)
visualizer.show()

assert "[3.84990315 8.92499051 2.19968337] 250.9495035007924" == repr(exp_calories)
assert """[0.58707936 0.83484872] 2.8340167340040523\n[0.18930451] 90.69592806454129""" == repr(exp_density_big)
assert """[-0.54460774  0.7615358   0.93237663] 4.079731215362401\n[0.5649755  0.76466156] 7.673955643254104""" == repr(exp_density_small)
