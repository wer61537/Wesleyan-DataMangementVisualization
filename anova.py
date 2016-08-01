# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 19:00:48 2016

@author: wer61
"""
#=========================================
#   get libs
#=========================================
import pandas as pd
import numpy as np
#to do categorical explanatory variable with levels
import statsmodels.formula.api as frm
#for tukey
import statsmodels.stats.multicomp as multi
#=========================================
#   get libs
#=========================================

#=========================================
#   set panda options
#=========================================
#Set PANDAS to show all columns in DataFrame
pd.set_option('display.max_columns', None)
#Set PANDAS to show all rows in DataFrame
pd.set_option('display.max_rows', None)
# bug fix for display formats to avoid run time errors
pd.set_option('display.float_format', lambda x:'%f'%x)
#=========================================
#   set panda options
#=========================================

#=========================================
#   set working directory
#=========================================
#change this to local for saving files
wd="C:/temp/coursera/Wesleyan/PythonWorkingDirectory/"
#=========================================

#=========================================
#   helper functions
#=========================================
def doAnova(df, response_var, explan_var):
    print("Means and Standard deviatons of explantory variable, " + explan_var + ".")
    print(df.groupby(explan_var).mean())
    print(df.groupby(explan_var).std())
    if (df[explan_var].value_counts().sort_values().count() ==2):
        model=frm.ols(formula= "'" + response_var +"'~C('" + explan_var +"')'", data =df)
        results = model.fit()
        print(results.summary())
    else:
        mc1=multi.MultiComparison(usage_days[response_var],usage_days[explan_var])
        res1=mc1.tukeyhsd()
        print(res1.summary())

#=========================================
#   helper functions
#=========================================


#=========================================
#   get the datset from git
#=========================================
url = "https://raw.githubusercontent.com/wer61537/Wesleyan-DataMangementVisualization/master/data_decisions.csv"
usage=pd.read_csv(url)
#=========================================
#   get the datset from git
#=========================================
usage.describe()
#=========================================
#   clean up NaN
#=========================================
#some lines come in w/ no data and show as NaN for variables.
#remove these records
usage =usage.dropna() 
#=========================================
#   clean up NaN
#=========================================

#=========================================
#   create new cat var that is Sunday or Not Sunda
#========================================
usage['Sunday'] =np.where(usage['DayInWeek']==1, '1', '0')
usage['Sunday']=usage['Sunday'].astype('category')
usage['Consumption_Value']=usage['Consumption Value']

usage_sunday=usage[['Consumption_Value','Sunday']].dropna()
usage_sunday.apply(pd.Series.value_counts, axis=1).fillna(0)

model1=frm.ols(formula= 'Consumption_Value ~C(Sunday)', data =usage_sunday)
results1 = model1.fit()
print(results1.summary())
#=========================================
#   create new cat var that is Sunday or Not Sunda
#=========================================
#doAnova(usage_sunday,'Consumption_Value', 'Sunday')


#=========================================
#   use 7 level DayInWeek var
#=========================================
usage_days=usage[['Consumption_Value','DayInWeek']].dropna()

model2=frm.ols(formula= 'Consumption_Value ~C(DayInWeek)', data =usage_days)
results1 = model2.fit()
print(results1.summary())

print(usage_days.groupby('DayInWeek').mean())
print(usage_days.groupby('DayInWeek').std())
mc1=multi.MultiComparison(usage_days['Consumption_Value'],usage_days['DayInWeek'])
res2=mc1.tukeyhsd()
print(res2.summary())
#=========================================
#   use 7 level DayInWeek var
#=========================================


#=========================================
#   try 12 level month var; this does not work
#=========================================
#convert to date
usage['Date']=pd.to_datetime(usage['Date'])
usage['MonthInYear']=usage['Date'].dt.month

usage_month=usage[['Consumption_Value','MonthInYear']].dropna()
usage_month.apply(pd.Series.value_counts, axis=1).fillna(0)

usage_month['MonthInYear']=usage_month['MonthInYear'].astype('category')
model3=frm.ols(formula= 'Consumption_Value ~C(MonthInYear)', data =usage_month)
results3 = model3.fit()
print(results3.summary())
mc3=multi.MultiComparison(usage_month['Consumption_Value'],usage_month['MonthInYear'])
res3=mc3.tukeyhsd()
print(res3.summary())
#=========================================
#   try 12 level month var
#=========================================

#=========================================
#   try 12 level month var; this does not work
#=========================================
usage_interval=usage[['Consumption_Value','SequentialIntervalInDay_cat']].dropna()
usage_interval.apply(pd.Series.value_counts, axis=1).fillna(0)

usage_month['MonthInYear']=usage_month['SequentialIntervalInDay_cat'].astype('category')
model4=frm.ols(formula= 'Consumption_Value ~C(SequentialIntervalInDay_cat)', data =usage_month)
results4 = model3.fit()
print(results4.summary())
mc4=multi.MultiComparison(usage_month['Consumption_Value'],usage_month['SequentialIntervalInDay_cat'])
res4=mc4.tukeyhsd()
print(res4.summary())
#=========================================
#   try 12 level month var
#=========================================