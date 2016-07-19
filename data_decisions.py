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

print("Frequency distribution of DayInYear.")                              
usage['DayInYear'].value_counts()

print("Normalized frequency distribution of DayInYear.")                              
usage['DayInYear'].value_counts( normalize=True)

plt.xlabel('DayInYear')
plt.ylabel('Frequency') 
plt.title(r'$Histogram\ of\ DayInYear$')
plt.grid(True)
n, bins, patches = plt.hist(usage['DayInYear'], 50, normed=1, facecolor='green', alpha=0.75)
n,  patches = plt.hist(usage['DayInYear'],  facecolor='green', alpha=0.75)
plt.show()


print("Frequency distribution of DayInWeek.")                              
usage['DayInWeek'].value_counts()

print("Normalized frequency distribution of DayInWeek.")                              
usage['DayInWeek'].value_counts( normalize=True)

plt.xlabel('DayInWeek')
plt.ylabel('Frequency') 
plt.title(r'$Histogram\ of\ DayInWeek$')
plt.grid(True)
n, bins, patches = plt.hist(usage['DayInWeek'], 50, normed=1, facecolor='green', alpha=0.75)
n,  patches = plt.hist(usage['DayInWeek'],  facecolor='green', alpha=0.75)
plt.show()


print("Frequency distribution of WeekInYear.")                              
usage['WeekInYear'].value_counts()

print("Normalized frequency distribution of WeekInYear.")                              
usage['WeekInYear'].value_counts( normalize=True)

plt.xlabel('WeekInYear')
plt.ylabel('Frequency') 
plt.title(r'$Histogram\ of\ WeekInYear$')
plt.grid(True)
n, bins, patches = plt.hist(usage['WeekInYear'], 50, normed=1, facecolor='green', alpha=0.75)
n,  patches = plt.hist(usage['WeekInYear'],  facecolor='green', alpha=0.75)
plt.show()


print("Frequency distribution of air_temp_f.")                              
usage['air_temp_f'].value_counts()

print("Normalized frequency distribution of air_temp_f.")                              
usage['air_temp_f'].value_counts( normalize=True)

plt.xlabel('air_temp_f')
plt.ylabel('Frequency') 
plt.title(r'$Histogram\ of\ air_temp_f$')
plt.grid(True)
n, bins, patches = plt.hist(usage['air_temp_f'], 50, normed=1, facecolor='green', alpha=0.75)
n,  patches = plt.hist(usage['air_temp_f'],  facecolor='green', alpha=0.75)
plt.show()

print("Frequency distribution of dew_pt_f.")                              
usage['dew_pt_f'].value_counts()

print("Normalized frequency distribution of dew_pt_f.")                              
usage['dew_pt_f'].value_counts( normalize=True)

plt.xlabel('dew_pt_f')
plt.ylabel('Frequency') 
plt.title(r'$Histogram\ of\ dew_pt_f$')
plt.grid(True)
n, bins, patches = plt.hist(usage['dew_pt_f'], 50, normed=1, facecolor='green', alpha=0.75)
n,  patches = plt.hist(usage['dew_pt_f'],  facecolor='green', alpha=0.75)
plt.show()


print("Frequency distribution of SequentialIntervalInDay.")                              
usage['SequentialIntervalInDay'].value_counts()

print("Normalized frequency distribution of SequentialIntervalInDay.")                              
usage['SequentialIntervalInDay'].value_counts( normalize=True)
#histogram of usage, errors due to "too many values to unpack"
plt.xlabel('SequentialIntervalInDay')
plt.ylabel('Frequency') 
plt.title(r'$Histogram\ of\ SequentialIntervalInDay$')
plt.grid(True)
n, bins, patches = plt.hist(usage['SequentialIntervalInDay'], 50, normed=1, facecolor='green', alpha=0.75)
n,  patches = plt.hist(usage['SequentialIntervalInDay'],  facecolor='green', alpha=0.75)
plt.show()




print("Frequency distribution of SequentialIntervalInWeek.")                              
usage['SequentialIntervalInWeek'].value_counts()

print("Normalized frequency distribution of SequentialIntervalInWeek.")                              
usage['SequentialIntervalInWeek'].value_counts( normalize=True)

#histogram of usage
plt.xlabel('SequentialIntervalInWeek')
plt.ylabel('Frequency') 
plt.title(r'$Histogram\ of\ SequentialIntervalInWeek$')
plt.grid(True)
n, bins, patches = plt.hist(usage['SequentialIntervalInWeek'], 50, normed=1, facecolor='green', alpha=0.75)
n,  patches = plt.hist(usage['SequentialIntervalInWeek'],  facecolor='green', alpha=0.75)
plt.show()

#try a few plots
usage.plot(x='SequentialIntervalInDay', y='Consumption Value')

usage.plot(x='SequentialIntervalInWeek', y='Consumption Value')


