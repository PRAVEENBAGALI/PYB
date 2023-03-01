import pandas as pd

df = pd.read_csv("C:\\Users\\pyb\\Downloads\\student.csv")
print(df)

print(df.index)

print(df.set_index('mark',inplace=True))
print(df)
print(df.loc[88])


