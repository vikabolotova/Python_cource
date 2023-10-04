import pandas as pd


df = pd.read_csv('emojis.csv')

df1 = df.groupby('Subcategory')['Rank'].sum()
min_value = df1.min()

print(df1[df1 == min_value].index)





