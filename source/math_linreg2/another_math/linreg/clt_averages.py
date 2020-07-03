import json
from matplotlib.pyplot import hist
import pathlib as pl


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


with open(pl.Path.cwd().joinpath("data").joinpath("sample_100k_customdistro.json")) as json_file:
    imported_data = json.load(json_file)

population = sum(imported_data['data'], [])

population_size = len(population)
sample_size = 1000
no_of_samples = int(population_size / sample_size)

samples = list(chunks(population, no_of_samples))
averages = [sum(sample) / sample_size for sample in samples]
hist(averages, 50)
