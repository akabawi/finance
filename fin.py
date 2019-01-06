import os
import pandas as pd


def total_year(d):

	a=[]
	for i in d.iterrows():
		a.append(i[1].iloc[4])

	return sum(a)

def total_month(d,m):

	a=[]
	for i in d.iterrows():
		if i[1].iloc[1] == m:
			a.append(i[1].iloc[4])
	return sum(a)


os.chdir("/home/akabawi/Documents/Mobills/")

file='Expenses 2018.xlsx'

xl=pd.ExcelFile(file)

#print(xl.sheet_names)

df = xl.parse('Expenses')

for i in range(2,13):
	print(str(i) + ": " + str(total_month(df,i)))

print("\nTotal for the year: AED " + str(total_year(df)))
print("\nAverage Monthly Spend: AED " + str(total_year(df)/11))
