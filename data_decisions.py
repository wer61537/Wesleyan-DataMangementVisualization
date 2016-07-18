# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 18:50:19 2016

@author: wer61
"""

import pandas as pd
import matplotlib.pyplot as plt


#get the dataset from git
url = "https://raw.githubusercontent.com/wer61537/Wesleyan-DataMangementVisualization/master/all.csv"
usage=pd.read_csv(url)

#some lines come in w/ no data and show as NaN for variables.
#remove these records
usage =usage.dropna() 

#crete secondary variables
#data is by 15 minute interval from 2/1/2016 0:00 through 7/6/2016 23:45
#Want to compare:
#    day (S, M, T, W Th, F,Sa) from week to week
#    week to week
#    sequential intervals in days and weeks
#   so need the following new variables (DayInYear, DayInWeek, WeekInYear, 
#   SequentialIntervalInDay, SequentialIntervalInWeek)
#While data is in Celsius, for understanding convert air_temp and dew_pt to Farenheit

#add 
#convert to date
usage['Date']=pd.to_datetime(usage['Date'])

#add DayInYear
usage['DayInYear']=usage['Date'].dt.dayofyear

#add DayInWeek  0=Sunday so add one
usage['DayInWeek']=usage['Date'].dt.dayofweek+1

#add WeekInYear
usage['WeekInYear']=usage['Date'].dt.weekofyear
#usage.head(100)

#Add Fahrenheit Air Temp
usage['air_temp_f']=(usage['air_temp'] * 1.8) + 32

#Add Fahrenheit dewpoint
usage['dew_pt_f']=(usage['dew_pt']* 1.8) + 32

usage['SequentialIntervalInDay']=usage.groupby('DayInYear').cumcount()

#the data starts on Feb 1 which is the second day of the week
#set all 
usage['SequentialIntervalInWeek']=usage.groupby('WeekInYear').cumcount()
#update first weeks values
usage.loc[usage['WeekInYear'] ==5, 'SequentialIntervalInWeek'] = usage['SequentialIntervalInWeek']+98
#export to verify
#usage.to_csv("c:/temp/data_decisions.csv")


#try a few plots
usage.plot(x='SequentialIntervalInDay', y='Consumption Value')

usage.plot(x='SequentialIntervalInWeek', y='Consumption Value')


