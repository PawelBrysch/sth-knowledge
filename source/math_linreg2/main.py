from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import pandas as pd
import os
from yellowbrick.regressor import ResidualsPlot

# TODO znajdz .score() dla regresji liniowej


class ModelWrapper:
    def __init__(self, df, output_column):
        self.X = df.iloc[:, :-1]
        self.y = df[output_column]
        self.value_sklearn = LinearRegression().fit(self.X, self.y)
        self.value_statsmodels = sm.OLS(self.y, sm.add_constant(self.X)).fit()
        # Private
        self._output_column = output_column

    def __repr__(self):
        return f"{self.value_sklearn.coef_} {self.value_sklearn.intercept_}"

    def residuals_against_fitted(self):
        visualizer = ResidualsPlot(self.value_sklearn)
        visualizer.score(self.X, self.y)
        visualizer.show()
        return visualizer

    def factory_method(self, column_to_exclude: str):
        new_model = None
        # new_df = df.drop([column_to_exclude], axis="columns")
        new_model = ModelWrapper(new_df, self.output_column)
        return new_model




# TODO z tego zrob funkcji, ktora generuje następny model
class ExperimentIncludedExcluded:

    def __init__(self, df, output_column, column_to_exclude=None):
        self.df_included = df
        self.model_included = ModelWrapper(self.df_included, output_column)
        self.model_excluded = None
        if column_to_exclude is not None:
            self.df_excluded = df.drop([column_to_exclude], axis="columns")
            self.model_excluded = ModelWrapper(self.df_excluded, output_column)

    # TODO przenies to do wrappera jako compare with
    def __repr__(self):
        regs = [model.value_sklearn for model in [self.model_included, self.model_excluded] if model is not None]
        reprs = [f"{reg.coef_} {reg.intercept_}" for reg in regs]
        return "\n".join(reprs)


df_calories = pd.read_excel(io=os.path.abspath("data/calories.xlsx"), header=0, usecols="C:F", nrows=80)
df_density_big = pd.read_excel(io=os.path.abspath("data/confoundOmitted_bigIntercept.xlsx"), header=0, usecols="C:E", nrows=80)
df_density_small = pd.read_excel(io=os.path.abspath("data/nearlyPerfectlyCorrelatedConfoundOmitted_smallIntercept.xlsx"), header=0, usecols="C:F", nrows=80)


exp_calories = ExperimentIncludedExcluded(df_calories, "calories")
exp_density_big = ExperimentIncludedExcluded(df_density_big, "bone density", "weight")
exp_density_small = ExperimentIncludedExcluded(df_density_small, "bone density", "years")

exp_density_big.model_excluded.value_statsmodels.summary()