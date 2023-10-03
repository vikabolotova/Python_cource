import pandas as pd

df = pd.read_csv('BCT-USD.csv')
df_1 = df.sort_values(['Volume'], ascending=True)
df_1['month'] = pd.DatetimeIndex(df_1['Date']).month
print(df_1.iloc[0].month)

