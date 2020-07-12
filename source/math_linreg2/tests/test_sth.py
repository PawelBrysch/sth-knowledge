# from math_linreg2.main import ModelWrapper
from math_linreg2.less_sklearn.lib import ModelWrapper
from unittest.mock import patch
import pandas as pd
import filecmp
import os


class TestName:
    def test_calculate(self):
        df_calories = pd.read_excel(io=os.path.abspath("data/calories.xlsx"), header=0, usecols="C:F", nrows=80)
        df_density_big = pd.read_excel(io=os.path.abspath("data/confoundOmitted_bigIntercept.xlsx"), header=0,
                                       usecols="C:E", nrows=80)
        df_density_small = pd.read_excel(
            io=os.path.abspath("data/nearlyPerfectlyCorrelatedConfoundOmitted_smallIntercept.xlsx"), header=0,
            usecols="C:F", nrows=80)

        model_calories = ModelWrapper(df_calories, "calories")
        model_density_big = ModelWrapper(df_density_big, "bone density")
        model_density_big_wo_weight = model_density_big.create_similar("weight")
        model_density_small = ModelWrapper(df_density_small, "bone density")
        model_density_small_wo_years = model_density_small.create_similar("years")

        assert repr(model_calories) == "height, weight, iq                            [3.84990315 8.92499051 2.19968337] 250.94950350079193"
        assert repr(model_density_big) == "weight, activity                              [0.58707936 0.83484872] 2.8340167340040523"
        assert repr(model_density_big_wo_weight) == "activity                                      [0.18930451] 90.69592806454129"
        assert repr(model_density_small) == "activity, weigth, years                       [-0.54460774  0.7615358   0.93237663] 4.0797312153622585"
        assert repr(model_density_small_wo_years) == "activity, weigth                              [0.5649755  0.76466156] 7.673955643254075"


   # TODO wpisac gdzies zmagania z tad

    @patch("yellowbrick.base.plt.show")
    def test_visualise(self, mock_show):
        df_calories = pd.read_excel(io=os.path.abspath("data/calories.xlsx"), header=0, usecols="C:F", nrows=80)
        exp_calories = ModelWrapper(df_calories, "calories")

        output_path = os.path.abspath("temp/received.png")
        expected_path = os.path.abspath("data/expected.png")
        try:
            os.remove(output_path)
        except:
            pass

        retval_out = exp_calories.residuals_against_fitted()
        retval_out.fig.savefig(output_path)

        assert filecmp.cmp(expected_path, output_path)

