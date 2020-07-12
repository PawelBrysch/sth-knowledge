import pandas as pd
from math_linreg2.less_sklearn.lib import ModelWrapper
import pathlib as pl

# Parse data
path_to_data = pl.Path.cwd().joinpath("data").joinpath("linreg_1st_attempt")
df_calories = pd.read_excel(io=path_to_data.joinpath("calories.xlsx"), header=0, usecols="C:F", nrows=80)
df_density_big = pd.read_excel(
    io=path_to_data.joinpath("confoundOmitted_bigIntercept.xlsx"), header=0, usecols="C:E", nrows=80
)
df_density_small = pd.read_excel(
    io=path_to_data.joinpath("nearlyPerfectlyCorrelatedConfoundOmitted_smallIntercept.xlsx"),
    header=0, usecols="C:F", nrows=80
)

# Create models
model_calories = ModelWrapper(df_calories, "calories")
model_density_big = ModelWrapper(df_density_big, "bone density")
model_density_small = ModelWrapper(df_density_small, "bone density")

# Create child models
model_density_big_wo_weight = model_density_big.create_similar("weight")
model_density_small_wo_years = model_density_small.create_similar("years")
