# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 18:50:19 2016

@author: wer61
"""

#=========================================
#   get libs
#=========================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import scipy.stats as st
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
#change this to local for saving graphs
wd="C:/temp/coursera/Wesleyan/PythonWorkingDirectory/images/"
#=========================================
#   set working directory
#=========================================

#=========================================
#   helper functions
#=========================================
def dist_plot(df, var):
    g=seaborn.distplot(df[var],
            kde_kws={"color":"g","lw":4,"label":"KDE Estim","alpha":0.5},
            hist_kws={"color":"r","alpha":0.3,"label":"Freq"})
    g.set_ylabel("Density",size = 14,color="black",alpha=0.5)
    plt.title(r'$Distribution Plot\ of\ ' + var + '$')    
    plt.savefig(wd + "Distribution Plot of  " + var + '.png')
    plt.close
            
def eda_plot(df,var,units):
    #histogram of var
    #print(wd + var + '.png')
    try:
        plt.gcf().clear() 
        plt.xlabel(var + ", " + units)
        plt.ylabel('Frequency') 
        plt.title(r'$Histogram\ of\ ' + var + '$')
        plt.grid(True)
        n, bins, patches = plt.hist(df[var], 50, normed=1, facecolor='green', alpha=0.75)
        n,  patches = plt.hist(df[var],  facecolor='green', alpha=0.75)
        plt.show()
        plt.savefig(wd + "Univariate Plot of  " + var + '.png')
        plt.close
        #clear so previous plot does not show
    except:
        #save even if error        
        plt.savefig(wd + "Univariate Plot of  " + var + '.png')
        plt.close 
        pass
    
#function to do descriptives and eda
def eda_var(df, var, units):
    #statistical summary
    print("Statistical Summary of " + var + ".")
    print(df[var].describe())
    print("Distribution Analysis " + var + ".")
    st.describe(df[var])
    #requency dsitributions    
    print("Frequency distribution of " + var +".")
    print( df[var].value_counts().sort_values())
    print("Normalized frequency distribution of " + var + ".")                              
    print(df[var].value_counts( normalize=True))
    #eda_plot(df,var, units)    
    dist_plot(usage,var)




#helper functions
def bivariate_bar_plot(df,dep_var, indep_var,grpby, units):
    #grpby is used to add hue to graph
    if grpby:
        seaborn.factorplot(x=indep_var, y=dep_var, data=df, hue =grpby , kind="bar", ci=None)
    else:
        seaborn.factorplot(x=indep_var, y=dep_var, data=df, kind="bar", ci=None)
    #would be great to figure out how to remove '_cat'    
    plt.xlabel(indep_var)
    plt.ylabel(dep_var)   
    plt.title(dep_var + " by " + indep_var)   
    plt.savefig(wd + "Bivariate Plot of " + dep_var + "_vs_"+ indep_var + '.png')
    plt.close
    

def lm_plot(df,dep_var, indep_var,grpby,units):
    if grpby:
        seaborn.lmplot(x=indep_var, y=dep_var, data=df, hue =grpby,fit_reg=False )
    else:
        seaborn.lmplot(x=indep_var, y=dep_var, data=df,fit_reg=False)
    
    #seaborn.lmplot(x=indep_var, y=dep_var, data=df, fit_reg=False)
    #would be great to figure out how to remove '_cat'    
    plt.xlabel(indep_var)
    plt.ylabel(dep_var + ", " + units)   
    plt.title("Scatterplot of " + dep_var + " versus " + indep_var)  
    plt.savefig(wd + "Scatterplot_" + dep_var + "_vs_"+ indep_var + '.png')
    plt.close
    
    
def scatter_plot(df,dep_var, indep_var,units):
    seaborn.regplot(x=indep_var, y=dep_var, data=df, fit_reg=False)
    #would be great to figure out how to remove '_cat'    
    plt.xlabel(indep_var)
    plt.ylabel(dep_var + ", " + units)   
    plt.title("Scatterplot of " + dep_var + " versus " + indep_var)  
    plt.savefig(wd + "Scatterplot_" + dep_var + "_vs_"+ indep_var + '.png')
    plt.close
    
#=========================================
#   helper functions
#=========================================

#=========================================
#   get the datset from git
#=========================================
url = "https://raw.githubusercontent.com/wer61537/Wesleyan-DataMangementVisualization/master/all.csv"
usage=pd.read_csv(url)
#=========================================
#   get the datset from git
#=========================================

#=========================================
#   clean up NaN
#=========================================
#some lines come in w/ no data and show as NaN for variables.
#remove these records
usage =usage.dropna() 
#=========================================
#   clean up NaN

#=========================================
#   create new vars
#=========================================

#create secondary variables
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


#create categorical variables for bivariate plots
usage['DayInWeek_cat'] = usage['DayInWeek'].astype('category')
usage['DayInYear_cat'] = usage['DayInYear'].astype('category')
usage['WeekInYear_cat'] = usage['WeekInYear'].astype('category')
usage['SequentialIntervalInDay_cat'] = usage['SequentialIntervalInDay'].astype('category')
usage['SequentialIntervalInWeek_cat'] = usage['SequentialIntervalInWeek'].astype('category')

#export to verify
#usage.to_csv("c:/temp/data_decisions.csv")
#=========================================
#   create new vars
#=========================================

#for each variable do freq (as counts and normalized),
#   describe, scatter plots (usage vs DayInYear, usage vs temp and dewpoint 
#   and then usage by category (WeekInYear,
#   DayInWeek, SequentialIntervalInDay, SequentialIntervalInWeek
#   ).

#=========================================
#   Statistical summary and distribution plots
#=========================================#do each var
eda_var(usage,'Consumption Value', 'kw')
eda_var(usage,'Demand Value', 'kwH')
eda_var(usage,'DayInWeek', '')
eda_var(usage,'DayInYear', '')
eda_var(usage,'WeekInYear', '')
eda_var(usage, 'air_temp_f', 'degrees, Fahrenheit')
eda_var(usage, 'dew_pt_f', 'degrees, Fahrenheit')
eda_var(usage, 'SequentialIntervalInDay', '')
eda_var(usage, 'SequentialIntervalInWeek', '')
#=========================================
#   Statistical summary and distribution plots
#=========================================#do each var


#=========================================
#   create bivariate graphs
#=========================================
#day in week
bivariate_bar_plot(usage, "Consumption Value","DayInWeek_cat","","kw")
bivariate_bar_plot(usage, "Consumption Value","DayInWeek_cat","WeekInYear_cat","kw")
bivariate_bar_plot(usage, "Demand Value","DayInWeek_cat","", "kwH")
bivariate_bar_plot(usage, "air_temp_f","DayInWeek_cat","","degrees, Fahrenheit")
bivariate_bar_plot(usage, "dew_pt_f","DayInWeek_cat","","degrees, Fahrenheit")


#day in year
bivariate_bar_plot(usage, "Consumption Value","DayInYear_cat","","kw")
bivariate_bar_plot(usage, "Demand Value","DayInYear_cat","","kwH")
bivariate_bar_plot(usage, "air_temp_f","DayInYear_cat","","degrees, Fahrenheit")
bivariate_bar_plot(usage, "dew_pt_f","DayInYear_cat","","degrees, Fahrenheit")

#week in year
bivariate_bar_plot(usage, "Consumption Value","WeekInYear_cat","","kw")
bivariate_bar_plot(usage, "Demand Value","WeekInYear_cat","","kwH")
bivariate_bar_plot(usage, "air_temp_f","WeekInYear_cat","","degrees, Fahrenheit")
bivariate_bar_plot(usage, "dew_pt_f","WeekInYear_cat","","degrees, Fahrenheit")

#SequentialIntervalInDay_cat in year
bivariate_bar_plot(usage, "Consumption Value","SequentialIntervalInDay_cat","","kw")
bivariate_bar_plot(usage, "Consumption Value","SequentialIntervalInDay_cat","DayInWeek_cat","kw")
bivariate_bar_plot(usage, "Demand Value","SequentialIntervalInDay_cat","","kwH")
bivariate_bar_plot(usage, "air_temp_f","SequentialIntervalInDay_cat","","degrees, Fahrenheit")
bivariate_bar_plot(usage, "dew_pt_f","SequentialIntervalInDay_cat","","degrees, Fahrenheit")

#SequentialIntervalInWeek_cat in year
bivariate_bar_plot(usage, "Consumption Value","SequentialIntervalInWeek_cat","","kw")
bivariate_bar_plot(usage, "Demand Value","SequentialIntervalInWeek_cat","","kwH")
bivariate_bar_plot(usage, "air_temp_f","SequentialIntervalInWeek_cat","","degrees, Fahrenheit")
bivariate_bar_plot(usage, "dew_pt_f","SequentialIntervalInWeek_cat","","degrees, Fahrenheit")


#week in year
bivariate_bar_plot(usage, "Consumption Value","WeekInYear_cat","","kw")
bivariate_bar_plot(usage, "Demand Value","WeekInYear_cat","","kwH")
bivariate_bar_plot(usage, "air_temp_f","WeekInYear_cat","","degrees, Fahrenheit")
bivariate_bar_plot(usage, "dew_pt_f","WeekInYear_cat","","degrees, Fahrenheit")
#=========================================
#   create bivariate graphs
#=========================================


#=========================================
#   create scatter plots using seaborn's lmplot
#=========================================
lm_plot(usage, "Consumption Value","DayInWeek","","")
lm_plot(usage, "Consumption Value","DayInYear","WeekInYear","")
lm_plot(usage, "Consumption Value","WeekInYear","","")
lm_plot(usage, "Consumption Value","SequentialIntervalInDay","","")
lm_plot(usage, "Consumption Value","SequentialIntervalInWeek","","")
lm_plot(usage, "Consumption Value","SequentialIntervalInWeek","WeekInYear","")
lm_plot(usage, "Consumption Value","air_temp_f","DayInWeek","degrees, Fahrenheit")
lm_plot(usage, "Consumption Value","dew_pt_f","DayInWeek","degrees, Fahrenheit")
#=========================================
#   create scatter plots
#=========================================


