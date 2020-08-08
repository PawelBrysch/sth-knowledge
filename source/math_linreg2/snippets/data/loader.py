import json
import pathlib as pl

class SawlikePop1M:
    def __new__(cls, *args, **kwargs):
        with open(pl.Path(__file__).with_name("sample_100k_customdistro.json")) as json_file:
            imported_data = json.load(json_file)

        population = sum(imported_data['data'], [])
        return population


def chunks(lst, chunk_size):
    res = []
    for i in range(0, len(lst), chunk_size):
        res.append(lst[i:i + chunk_size])
    return res
