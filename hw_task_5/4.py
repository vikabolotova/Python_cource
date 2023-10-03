import pandas as pd


df = pd.read_csv('emojis.csv')
df1 = df.Subcategory.value_counts()
print(df1.index[0])


