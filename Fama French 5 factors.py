import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.formula.api import ols

# import data
FF5_data = pd.read_csv('/Users/.../Fama_French_5_2*3.csv', index_col = 0)
FF5_data = FF5_data.loc['196307' : '201312']
FF5_data = FF5_data # original data are in %
# initial table using dataframe
table_column = FF5_data.columns.tolist()
table_column.insert(0,'Intercept')
Regression_tvalue_table = pd.DataFrame(index = FF5_data.columns, columns = table_column)
table_column.append('R-square')
Regression_coef_table =pd.DataFrame(index = FF5_data.columns, columns = table_column)
# regression
for factor in FF5_data.columns:
    factor_list = FF5_data.columns.tolist()
    factor_list.remove(factor)
    model = ols(str(factor) + '~'+ str(factor_list[0]) + '+' + str(factor_list[1]) + '+' + str(factor_list[2]) + '+' + str(factor_list[3]), FF5_data).fit()
    Regression_coef_table.loc[factor]['R-square'] = model.rsquared
    Regression_coef_table.loc[factor]['Intercept'] = model.params[0]
    Regression_tvalue_table.loc[factor]['Intercept'] = model.tvalues[0]
    Regression_coef_table.loc[factor][factor_list[0]] = model.params[1]
    Regression_tvalue_table.loc[factor][factor_list[0]] = model.tvalues[1]
    Regression_coef_table.loc[factor][factor_list[1]]= model.params[2]
    Regression_tvalue_table.loc[factor][factor_list[1]] = model.tvalues[2]
    Regression_coef_table.loc[factor][factor_list[2]] = model.params[3]
    Regression_tvalue_table.loc[factor][factor_list[2]] = model.tvalues[3]
    Regression_coef_table.loc[factor][factor_list[3]] = model.params[4]
    Regression_tvalue_table.loc[factor][factor_list[3]] = model.tvalues[4]

Regression_coef_table.to_csv('/Users/.../Table1_coef.csv')
Regression_tvalue_table.to_csv('/Users/.../Table1_tvalue.csv')

# add UMD
UMD = pd.read_csv('/Users/junqi/Desktop/UMD.csv', index_col = 0)
UMD = UMD.loc['196307' : '201312']
UMD = UMD
FF5_data['UMD'] = UMD.values

# initial table using dataframe
table_column = FF5_data.columns.tolist()
table_column.insert(0,'Intercept')
Regression_tvalue_table = pd.DataFrame(index = FF5_data.columns, columns = table_column)
table_column.append('R-square')
Regression_coef_table =pd.DataFrame(index = FF5_data.columns, columns = table_column)
# regression
for factor in FF5_data.columns:
    factor_list = FF5_data.columns.tolist()
    factor_list.remove(factor)
    model = ols(str(factor) + '~'+ str(factor_list[0]) + '+' + str(factor_list[1]) + '+' + str(factor_list[2]) + '+' + str(factor_list[3]) + '+' + str(factor_list[4]), FF5_data).fit()
    Regression_coef_table.loc[factor]['R-square'] = model.rsquared
    Regression_coef_table.loc[factor]['Intercept'] = model.params[0]
    Regression_tvalue_table.loc[factor]['Intercept'] = model.tvalues[0]
    Regression_coef_table.loc[factor][factor_list[0]] = model.params[1]
    Regression_tvalue_table.loc[factor][factor_list[0]] = model.tvalues[1]
    Regression_coef_table.loc[factor][factor_list[1]] = model.params[2]
    Regression_tvalue_table.loc[factor][factor_list[1]] = model.tvalues[2]
    Regression_coef_table.loc[factor][factor_list[2]] = model.params[3]
    Regression_tvalue_table.loc[factor][factor_list[2]] = model.tvalues[3]
    Regression_coef_table.loc[factor][factor_list[3]] = model.params[4]
    Regression_tvalue_table.loc[factor][factor_list[3]] = model.tvalues[4]
    Regression_coef_table.loc[factor][factor_list[4]] = model.params[5]
    Regression_tvalue_table.loc[factor][factor_list[4]] = model.tvalues[5]

Regression_coef_table.to_csv('/Users/.../Table2_coef.csv')
Regression_tvalue_table.to_csv('/Users/.../Table2_tvalue.csv')

#import HML-DEV
HML_Dev = pd.read_csv('/Users/junqi/Desktop/HML_DEV.CSV', index_col = 0)
HML_Dev = HML_Dev * 100 # make data in %
HML_Dev = HML_Dev['7/31/63' : '12/31/13']
FF5_data['HML'] = HML_Dev.values
FF5_data.columns = FF5_data.columns.str.replace('HML','HML_DEV')

# initial table using dataframe
table_column = FF5_data.columns.tolist()
table_column.insert(0,'Intercept')
Regression_tvalue_table = pd.DataFrame(index = FF5_data.columns, columns = table_column)
table_column.append('R-square')
Regression_coef_table =pd.DataFrame(index = FF5_data.columns, columns = table_column)
# regression
for factor in FF5_data.columns:
    factor_list = FF5_data.columns.tolist()
    factor_list.remove(factor)
    model = ols(str(factor) + '~'+ str(factor_list[0]) + '+' + str(factor_list[1]) + '+' + str(factor_list[2]) + '+' + str(factor_list[3]) + '+' + str(factor_list[4]), FF5_data).fit()
    Regression_coef_table.loc[factor]['R-square'] = model.rsquared
    Regression_coef_table.loc[factor]['Intercept'] = model.params[0]
    Regression_tvalue_table.loc[factor]['Intercept'] = model.tvalues[0]
    Regression_coef_table.loc[factor][factor_list[0]] = model.params[1]
    Regression_tvalue_table.loc[factor][factor_list[0]] = model.tvalues[1]
    Regression_coef_table.loc[factor][factor_list[1]] = model.params[2]
    Regression_tvalue_table.loc[factor][factor_list[1]] = model.tvalues[2]
    Regression_coef_table.loc[factor][factor_list[2]] = model.params[3]
    Regression_tvalue_table.loc[factor][factor_list[2]] = model.tvalues[3]
    Regression_coef_table.loc[factor][factor_list[3]] = model.params[4]
    Regression_tvalue_table.loc[factor][factor_list[3]] = model.tvalues[4]
    Regression_coef_table.loc[factor][factor_list[4]] = model.params[5]
    Regression_tvalue_table.loc[factor][factor_list[4]] = model.tvalues[5]

Regression_coef_table.to_csv('/Users/.../Table3_coef.csv')
Regression_tvalue_table.to_csv('/Users/.../Table3_tvalue.csv')
