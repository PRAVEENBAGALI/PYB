import pandas as pd

df = pd.read_csv('C:\\Users\\pyb\\Downloads\\Test1_Data.csv')
print(df)

# print(df['temperature'])
print(df['temperature'].max())
# print(df[['event','windspeed']])

print(df['day'][df['event'] == 'Rain'])


