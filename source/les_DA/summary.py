import numpy as np
import pandas as pd
import statsmodels.regression.linear_model as rg
import statsmodels.tools.tools as ct

def get_model(path_to_data, index_name, dependent_var_name, parse_dates=False):
    data = pd.read_csv(path_to_data, index_col=index_name, parse_dates=parse_dates)
    data.loc[:, 'int'] = ct.add_constant(data)
    lmivar = list(data._series.keys())
    lmivar.remove(dependent_var_name)
    lm = rg.OLS(data[dependent_var_name], data[lmivar], hasconst=bool).fit()
    return lm


lm = get_model(path_to_data='Data//Multiple-Regression-Analysis-Data.txt', index_name="Date",
               dependent_var_name="stocks", parse_dates=True)
lm2 = get_model(path_to_data='Data//excel_develop.csv', index_name="MonkeyID", dependent_var_name="Length")

print('')
print(lm2.summary())
print('')
print('== Analysis of Variance ANOVA ==')
print('')
print('== Degrees of Freedom DF ==')
print('regression degrees of freedom:', lm.df_model)
print('residuals degrees of freedom:', lm.df_resid)
print('total degrees of freedom:', lm.df_model + lm.df_resid)
print('')
print('== Sum of Squares SS ==')
print('regression sum of squares:', np.round(lm.ess, 6))
print('residuals sum of squares:', np.round(lm.ssr, 6))
print('total sum of squares:', np.round(lm.ess + lm.ssr, 6))
print('')
print('== Mean Square Error MSE ==')
print('regression mean square error:', np.round(lm.mse_model, 6))
print('residuals mean square error:', np.round(lm.mse_resid, 6))
print('total mean square error:', np.round(lm.mse_total, 6))
print('')
print('== F Test ==')
print('F-statistic:', np.round(lm.fvalue, 6))
print('Prob (F-statistic):', np.round(lm.f_pvalue, 6))


