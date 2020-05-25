from math_linreg2.main import ExperimentIncludedExcluded, ModelWrapper, residuals_against_fitted
from unittest.mock import patch
import pandas as pd
import matplotlib.pyplot as plt
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

        exp_calories = ExperimentIncludedExcluded(df_calories, "calories")
        exp_density_big = ExperimentIncludedExcluded(df_density_big, "bone density", "weight")
        exp_density_small = ExperimentIncludedExcluded(df_density_small, "bone density", "years")

        assert "[3.84990315 8.92499051 2.19968337] 250.9495035007924" == repr(exp_calories)
        assert """[0.58707936 0.83484872] 2.8340167340040523\n[0.18930451] 90.69592806454129""" == repr(exp_density_big)
        assert """[-0.54460774  0.7615358   0.93237663] 4.079731215362401\n[0.5649755  0.76466156] 7.673955643254104""" == repr(exp_density_small)

   # TODO wpisac gdzie zmagania z tad

    @patch("yellowbrick.base.plt.show")
    def test_visualise(self, mock_show):
        df_calories = pd.read_excel(io=os.path.abspath("data/calories.xlsx"), header=0, usecols="C:F", nrows=80)
        exp_calories = ExperimentIncludedExcluded(df_calories, "calories")

        output_path = os.path.abspath("temp/received.png")
        expected_path = os.path.abspath("data/expected.png")
        try:
            os.remove(output_path)
        except:
            pass

        retval_out = residuals_against_fitted(exp_calories.model_included)
        retval_out.fig.savefig(output_path)
        assert filecmp.cmp(expected_path, output_path)

