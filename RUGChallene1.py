#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:44:36 2019

@author: varakind
"""

import os
import pandas as pd
import datetime
from scipy import stats
import matplotlib.pyplot as plt

print("Hi")

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

df = pd.read_csv("RUGChallene1.csv")

#Change first analysis into a posix number and add to 
firstAnalysisPOSIX = []
for i in range(len(df["first_analysis"])):
    newDate = datetime.datetime.fromisoformat(df["first_analysis"][i][0:10])
    newTime = datetime.time.fromisoformat(df["first_analysis"][i][11:])
    POSIX = newDate.timestamp()#seconds to the date
    timeInSeconds = newTime.hour * 3600 + newTime.minute * 60 + newTime.second#seconds since beginning of date
    first_analysis_POSIX = POSIX + timeInSeconds
    firstAnalysisPOSIX.append(first_analysis_POSIX)
df["first_analysis_POSIX"] = firstAnalysisPOSIX

#print data frame columns just so I have them handy for copy paste...
#for i in df.columns:
#    print (i)

#Fit Model using scipy
slope, intercept, r_value, p_value, std_err = stats.linregress(df["timestamp"],df["first_analysis_POSIX"])
print ("SciPy SLOPE: " + str(slope))
print ("SciPy Intercept: " + str(intercept))

#Make prediction for each model, print result
TIMESTAMP = 636583527529040685#the one from Ben
PredictedPOSIXSciPy = slope*TIMESTAMP + intercept
print ("SciPy PredictedPOSIX: " + str(PredictedPOSIXSciPy))

#Turn numbers back into dates
predicted_date_SCIPy = datetime.datetime.fromtimestamp(int(PredictedPOSIXSciPy))
print("PREDICTED DATE SciPy: " + str(predicted_date_SCIPy))

#Make a graph
Timestamps = []
First_AnalysisPOSIX = []
colors = []

for i in range(len(df["first_analysis_POSIX"])):
    Timestamps.append(df["timestamp"][i])
    First_AnalysisPOSIX.append(df["first_analysis_POSIX"][i])
    colors.append("red")

#add scipy prediction to the list for the graph    
Timestamps.append(TIMESTAMP)
First_AnalysisPOSIX.append(PredictedPOSIXSciPy)
colors.append("blue")

plt.style.use('ggplot')
plt.scatter(Timestamps,First_AnalysisPOSIX,s=500,alpha=.75,marker=r'$\heartsuit$',c=colors)
plt.xlabel("POSIX Timestamp")
plt.ylabel("First_Analysis (POSIX)")
plt.show()




