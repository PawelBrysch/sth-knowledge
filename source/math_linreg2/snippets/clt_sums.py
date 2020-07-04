import json
import pandas as pd
from matplotlib.pyplot import hist
import pathlib as pl

# with open(rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\source\another_math\linreg\output.json") as json_file:
with open(pl.Path.cwd().joinpath("data").joinpath("sample_100k_customdistro.json")) as json_file:
    imported_data = json.load(json_file)

dataframe = pd.DataFrame(imported_data['data'])
hist(x=dataframe.sum(), bins=100)