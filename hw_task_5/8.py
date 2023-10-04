import pandas as pd

df = pd.read_csv('BCT-USD.csv')
df['Date'] = pd.to_datetime(df['Date'])
min_volum = df['Volume'].min()
print(df['Date'][df['Volume'] == min_volum].dt.month_name().iloc[0])

