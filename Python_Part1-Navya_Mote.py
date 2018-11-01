# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:18:38 2018

@author: Navya
"""

import pandas as pd
#%%Import EmployeeAttrition CSV
mydata = pd.read_csv('/Users/Navya/Desktop/AIT580 - Analytics-Big data to information/Python/EmployeeAttrition.csv')
#%%Find the number of entries/rows in the data
tot_rows = len(mydata.index)
print("Total no. of rows is:")
print(tot_rows)
#%%Find the number of columns in the data
tot_col = len(mydata.columns)
print("Total no. of columns is:")
print(tot_col)
print("==============================================")
#%%What is the average Monthly Income
mi_avg = mydata["MonthlyIncome"].mean()
print("Avg Monthly Income is:")
print(mi_avg)
print("==============================================")
#%%What is the highest amount of HourlyRate
hr_max = mydata["HourlyRate"].max()
print("Highest amount of HourlyRate is:")
print(hr_max)
print("==============================================")
#%%What is the Department, JobRole, MaritalStatus and OverTime of EmployeeNumber 10
e10_data = mydata.loc[mydata['EmployeeNumber'] == 10, ['Department', 'JobRole', 'MaritalStatus', 'OverTime']]
print(e10_data)
print("==============================================")
#%%What is the Employee ID of highest MonthlyIncome paid employee
print(mydata[['EmployeeNumber', 'MonthlyIncome']][mydata.MonthlyIncome == mydata.MonthlyIncome.max()])
print("==============================================")
#%%What is the Average (mean) DailyRate for all Employees Group By Age whose age is greater than 58
dr_avg = mydata.groupby(mydata["Age"] > 58)["DailyRate"].mean()
print(dr_avg)
print("==============================================")
#%%How many unique EducationField are there
ef_unique = mydata["EducationField"].nunique()
print("How many unique EducationField are there:")
print(ef_unique)
print("==============================================")
#%%What are the top 5 most common JobRoles
top = mydata['JobRole'].value_counts()[:5]
print("The top 5 most common JobRoles are:")
print(top)
print("==============================================")
#%%How many JobRoles represented by less than 100 employees
jr = mydata.groupby('JobRole')
x = jr.count()
j = x[x['EmployeeCount'] < 100]
tot_jr = len(j.index)
print("How many JobRoles represented by less than 100 employees")
print(tot_jr)
print("==============================================")
#%%What is the correlation between Education and JobSatisfaction
d = mydata[['Education','JobSatisfaction']]
corr = d.corr(method='pearson')
corr1 = d.corr(method='kendall')
corr2 = d.corr(method='spearman')
print("Pearson correlation between Education and JobSatisfaction is:")
print(corr)
print("Kendall correlation between Education and JobSatisfaction is:")
print(corr1)
print("Spearman correlation between Education and JobSatisfaction is:")
print(corr2)
print("==============================================") 
#%%