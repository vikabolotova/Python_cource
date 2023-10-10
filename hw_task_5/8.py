import pandas as pd

df = pd.read_csv('BCT-USD.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year_month'] = df['Date'].dt.strftime('%Y-%m')
df['Year_month'] = pd.to_datetime(df['Year_month'])

df_sum_month = df.groupby('Year_month')['Volume'].sum().reset_index()
print(df_sum_month)

min_value = df_sum_month.iloc[:, 1].min() # Предполагается, что второй столбец имеет индекс 1
min_date = df_sum_month[df_sum_month.iloc[:, 1] == min_value]['Year_month'].iloc[0]
min_month = min_date.month_name()
min_year = min_date.year
print(min_month,min_year)