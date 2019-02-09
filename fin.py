import os
import pandas as pd


def total_year(d):

	a=[]
	for i in d.iterrows():
		a.append(i[1].iloc[4])

	return int(sum(a))

def total_month(d,m):

	a=[]
	for i in d.iterrows():
		if i[1].iloc[1] == m:
			a.append(i[1].iloc[4])
	return int(sum(a))

def display_cat(d):

	s=set()
	for i in d.iterrows():
		if i[1].iloc[3] not in s:
			s.add(i[1].iloc[3])
	print("\nCategories:\n")
	for i in s:
		tm=0
		for n in d.iterrows():
			if n[1].iloc[3] == i:
				tm = tm + int(n[1].iloc[4])
		print (i + ": " + format(tm,",d"))		




os.chdir("/home/akabawi/pCloudDrive/Finances/")

file='Expenses 2018.xlsx'

xl=pd.ExcelFile(file)

#print(xl.sheet_names)

df = xl.parse('Expenses')

for i in range(2,13):
	print(format(i,"02d") + ": " + format(total_month(df,i), ",d"))

print("\nTotal for the year: " + format(total_year(df) , ",d") ) 
print("\nAverage Monthly Spend: " + format(int(total_year(df)/11),",d") + "\n")

display_cat(df)
