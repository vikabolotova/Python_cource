import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('emojis.csv')
print(df)
print(df.groupby('Year')['Year'].count())
plt.plot(df.groupby('Year')['Year'].count())
plt.savefig('year_pop.png')