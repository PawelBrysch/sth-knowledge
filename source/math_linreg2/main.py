from sklearn.linear_model import LinearRegression
import pandas as pd
import os

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

