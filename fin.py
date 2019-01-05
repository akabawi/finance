import os
import pandas as pd


def total_year(d):

	a=[]
	for i in d.iterrows():
		a.append(i[1].iloc[4])

	return sum(a)





os.chdir("/home/akabawi/Documents/Mobills/")

file='Expenses 2018.xlsx'

xl=pd.ExcelFile(file)

#print(xl.sheet_names)

df = xl.parse('Expenses')

print(total_year(df))