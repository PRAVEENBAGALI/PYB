import pandas as pd

df = pd.read_csv("C:\\Users\\pyb\\Downloads\\student.csv")
print(df)

rows, columns = df.shape  # to get the number of rows and columns of sheet
print(rows)
print(columns)

print(df.head())  # prints the first 5 rows of the sheet
print(df.head(2))  # prints only first 2 rows of the sheet
print(df.tail())  # prints the last 5 rows of the sheet
print(df.tail(1))  # prints only last row of the sheet

print(df[2:5])  # prints the rows from 2-5 rows of the sheet

print(df.columns)  # prints the columns of the sheet

print(df["mark"]) #print the values od column with specified header

type(df["mark"])

print(df[['mark','name']])

print(df['mark'])
print(df['mark'].max())
print(df['mark'].min())
print(df['mark'].mean())
print(df['mark'].std())

print(df.describe())

print(df[df.mark ==df['mark'].max()])
print(df['id'][df.mark ==df['mark'].max()])
print(df[['id','mark']][df.mark ==df['mark'].max()])
print(df[['id','mark','name']][df.mark ==df['mark'].max()])


print(df.index) #gives the range of the table

print(df.set_index('mark')) # this id set the ond one of the columns as reference and start analysing
print(df.loc[22])
print(df.reset_index(inplace=True))
print(df)

print(df.set_index('id'))
print(df)
