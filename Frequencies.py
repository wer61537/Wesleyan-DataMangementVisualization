# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 16:05:55 2016

@author: Bill Rowe
"""
import pandas as pd
import matplotlib.pyplot as plt

#get the dataset from git
url = "https://raw.githubusercontent.com/wer61537/Wesleyan-DataMangementVisualization/master/all.csv"
usage=pd.read_csv(url)

#some lines come in w/ no data and show as NaN for variables.
#remove these records
usage =usage.dropna() 


#get summary of data in datareader
#what are the column names

#get shape or dimensions of the data
print("The usage dataframe has the shape or dimensions of " + str(usage.shape))

#get the names of the variables
print("Names of the variables, valued cells and datatype are:")
print(usage.info())


print("The first 10 columns to get a sense of the data are:")
usage.head(10)

#freq distribution of Usage, Demand, air_temp, dew_pt
#Usage
print("Frequency distribution of Usage (kw).")                              
usage['Consumption Value'].value_counts()

print("Normalized frequency distribution of Usage (kw).")                              
usage['Consumption Value'].value_counts( normalize=True)
 
#histogram of usage
plt.xlabel('Usage, kw')
plt.ylabel('Frequency') 
plt.title(r'$Histogram\ of\ Usage$')
plt.grid(True)
n, bins, patches = plt.hist(usage['Consumption Value'], 50, normed=1, facecolor='green', alpha=0.75)
n,  patches = plt.hist(usage['Consumption Value'],  facecolor='green', alpha=0.75)
plt.show()

#Demand
print("Frequency distribution of Demand (kwH).")                              
usage['Demand Value'].value_counts()

print("Normalized frequency distribution of Demand (kwH).")                              
usage['Demand Value'].value_counts( normalize=True)

#histogram of usage
plt.xlabel('Demand, kwH')
plt.ylabel('Frequency') 
plt.title(r'$Histogram\ of\ Demand$')
plt.grid(True)
n, bins, patches = plt.hist(usage['Demand Value'], 50, normed=1, facecolor='green', alpha=0.75)
plt.show()
         
#air_temp
print("Frequency distribution of air temperature (celsius).")                              
usage['air_temp'].value_counts()

print("Normalized frequency distribution of air temperature (celsius).")                              
usage['air_temp'].value_counts( normalize=True)

#histogram of usage
plt.xlabel('Air Temperature (Celsius)')
plt.ylabel('Frequency') 
plt.title(r'$Histogram\ of\ Air Temperature\ (Celsius)$')
plt.grid(True)
n, bins, patches = plt.hist(usage['air_temp'], 50, normed=1, facecolor='green', alpha=0.75)
plt.show()
        
         
#dew_pt
print("Frequency distribution of dew point (celsius).")                              
usage['dew_pt'].value_counts()

print("Normalized frequency distribution of dew point (celsius).")                              
usage['dew_pt'].value_counts( normalize=True)

#histogram of usage
plt.xlabel('Dew Point (Celsius)')
plt.ylabel('Frequency') 
plt.title(r'$Histogram\ of\ Dew Point\ (Celsius)$')
plt.grid(True)
n, bins, patches = plt.hist(usage['dew_pt'], 50, normed=1, facecolor='green', alpha=0.75)
plt.show()                              



