import pandas as pd
df= pd.read_csv('C:\\Users\\pyb\\Downloads\\student.csv')
print(df)

print(df["mark"].max())
print(df["name"][df["mark"]==88])
print(df["name"][df["mark"]==88][df["class"]=="Four"])
print(df["mark"].min())
print(df["mark"].mean())

df.fillna(0,inplace=True)
