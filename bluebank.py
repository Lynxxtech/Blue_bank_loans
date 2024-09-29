# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:01:28 2024

@author: DE
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

# Method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
# Transform to dataframe
loandata = pd.DataFrame(data)

# Finding unique values for the purpose column
loandata['purpose'].unique()

# Describe the data
loandata.describe()

# Describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

# Using EXP() to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualIncome'] = income


# Working with IF statements


# FICO
# fico >= 300 and < 400:
# 'Very Poor'
# fico >= 400 and ficoscore < 600:
# 'Poor'
# fico >= 601 and ficoscore < 660:
# 'Fair'
# fico >= 660 and ficoscore < 780:
# 'Good'
# fico >=780:
# 'Excellent'

    
# Applying for loop to loan data

# Using first 10
length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    try:
        if category >= 300 and category < 400:
            cat ='Very poor'
        elif category >= 400 and category < 600:
            cat = "Poor"
        elif category >= 600 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
            cat = 'Unknown'
    ficocat.append(cat)

ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat

#df.loc as conditional statements

#df.loc[df[columname] condition, newcolumnname] = 'value if the condition is met'
# for interest rate a new column is wanted. rate > 0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#nubers of loans by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.2)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.2)
plt.show()

#scatter plot

ypoint = loandata['annualIncome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'red')
plt.show()

# writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)























