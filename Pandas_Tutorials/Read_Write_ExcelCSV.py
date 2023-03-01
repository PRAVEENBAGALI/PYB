import pandas as pd

# df = pd.read_csv("C:\\Users\\pyb\\Downloads\\stock.csv")
# print(df)

df = pd.read_csv("C:\\Users\\pyb\\Downloads\\stock.csv",
                 skiprows=1)  # when the data have one header for all columns and skip this row
print(df)

# headers are not there but now we are adding the headers to the information
df = pd.read_excel("C:\\Users\\pyb\\Downloads\\stock.xlsx", header=None,
                   names=['tickers', 'eps', 'revenue', 'price', 'people'])
print(df)

print('#########################################################################')

#df =pd.read_csv("C:\\Users\\pyb\\Downloads\\stock_check.csv",nrows=3)
#print(df)

df =pd.read_csv("C:\\Users\\pyb\\Downloads\\stock_check.csv",na_values=['not available','n.a'])
print(df)