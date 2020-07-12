from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import pandas as pd
import os
from yellowbrick.regressor import ResidualsPlot

# TODO znajdz .score() dla regresji liniowej
# TODO doinstaluj to gowno https://stackoverflow.com/questions/57743230/userwarning-could-not-import-the-lzma-module-your-installed-python-is-incomple           i miej spokoj


class ModelWrapper:
    def __init__(self, df, output_column):
        self.X = df.iloc[:, :-1]
        self.y = df[output_column]
        self.value_sklearn = LinearRegression().fit(self.X, self.y)
        self.value_statsmodels = sm.OLS(self.y, sm.add_constant(self.X)).fit()
        # Private
        self._df = df
        self._output_column = output_column

    def __repr__(self):
        return "{:<45} {}".format(
            ", ".join(list(self._df)[:-1]),
            str(self.value_sklearn.coef_) + " " + str(self.value_sklearn.intercept_)
        )

    def __eq__(self, other):
        print(self)
        print(other)

    def residuals_against_fitted(self):
        visualizer = ResidualsPlot(self.value_sklearn)
        visualizer.score(self.X, self.y)
        visualizer.show()
        return visualizer

    class ModelWrapperFactory:
        @staticmethod
        def create(model, column_to_exclude: str):
            new_df = model._df.drop([column_to_exclude], axis="columns")
            new_model = ModelWrapper(new_df, model._output_column)
            return new_model


    def create_similar(self, column_to_exclude: str):
        return ModelWrapper.ModelWrapperFactory.create(self, column_to_exclude)


if __name__ == '__main__':
    df_calories = pd.read_excel(io=os.path.abspath("data/calories.xlsx"), header=0, usecols="C:F", nrows=80)
    df_density_big = pd.read_excel(io=os.path.abspath("data/confoundOmitted_bigIntercept.xlsx"), header=0,
                                   usecols="C:E", nrows=80)
    df_density_small = pd.read_excel(
        io=os.path.abspath("data/nearlyPerfectlyCorrelatedConfoundOmitted_smallIntercept.xlsx"), header=0,
        usecols="C:F", nrows=80)

    model_calories = ModelWrapper(df_calories, "calories")
    model_density_big = ModelWrapper(df_density_big, "bone density")
    model_density_small = ModelWrapper(df_density_small, "bone density")

    model_density_big_wo_weight = model_density_big.create_similar("weight")
    model_density_small_wo_years = model_density_small.create_similar("years")
