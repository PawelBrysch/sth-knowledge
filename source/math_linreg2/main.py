from sklearn.linear_model import LinearRegression
import pandas as pd
import os
from yellowbrick.regressor import ResidualsPlot



def residuals_against_fitted(model):
    visualizer = ResidualsPlot(model.value)
    visualizer.score(model.X, model.y)
    visualizer.show()
    return visualizer

class ModelWrapper:
    def __init__(self, df, output_column):
        self.X = df.iloc[:, :-1]
        self.y = df[output_column]
        self.value = LinearRegression().fit(self.X, self.y)


class ExperimentIncludedExcluded:
    def __init__(self, df, output_column, column_to_exclude=None):
        self.df_included = df
        self.model_included = ModelWrapper(self.df_included, output_column)

        self.model_excluded = None
        if column_to_exclude is not None:
            self.df_excluded = df.drop([column_to_exclude], axis="columns")
            self.model_excluded = ModelWrapper(self.df_excluded, output_column)

    def __repr__(self):
        regs = [model.value for model in [self.model_included, self.model_excluded] if model is not None]
        reprs = [f"{reg.coef_} {reg.intercept_}" for reg in regs]
        return "\n".join(reprs)


df_calories = pd.read_excel(io=os.path.abspath("data/calories.xlsx"), header=0, usecols="C:F", nrows=80)
df_density_big = pd.read_excel(io=os.path.abspath("data/confoundOmitted_bigIntercept.xlsx"), header=0, usecols="C:E", nrows=80)
df_density_small = pd.read_excel(io=os.path.abspath("data/nearlyPerfectlyCorrelatedConfoundOmitted_smallIntercept.xlsx"), header=0, usecols="C:F", nrows=80)


exp_calories = ExperimentIncludedExcluded(df_calories, "calories")
exp_density_big = ExperimentIncludedExcluded(df_density_big, "bone density", "weight")
exp_density_small = ExperimentIncludedExcluded(df_density_small, "bone density", "years")




# TODO zrob z tego testy
     # TODO porownaj zapisy obrazu (!!!!!!! już prawie zrobione)
import matplotlib.pyplot as plt
# some_png = os.path.abspath("some_png.png")
#
# retval_out = residuals_against_fitted(exp_calories.model_included)
# # plt.close(retval_out.fig)
#
# retval_out.fig.savefig(some_png) # TODO to !!!!

# TODO dodaj alternatywny
    # https://stackoverflow.com/questions/27928275/find-p-value-significance-in-scikit-learn-linearregression
# TODO porownaj ze swoja summary
"""###################################
tests
###################################"""
# retval_out = residuals_against_fitted(exp_calories.model_included)


assert "[3.84990315 8.92499051 2.19968337] 250.9495035007924" == repr(exp_calories)
assert """[0.58707936 0.83484872] 2.8340167340040523\n[0.18930451] 90.69592806454129""" == repr(exp_density_big)
assert """[-0.54460774  0.7615358   0.93237663] 4.079731215362401\n[0.5649755  0.76466156] 7.673955643254104""" == repr(exp_density_small)
