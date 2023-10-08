import pandas as pd

df = pd.read_csv('BCT-USD.csv')
df['Date'] = pd.to_datetime(df['Date'])

df['Year_month'] = df['Date'].dt.strftime('%Y-%m')
df_last_day_close = df.groupby('Year_month')['Close'].last().reset_index()
df_first_day_open = df.groupby('Year_month')['Open'].first().reset_index()

df3_merged = pd.merge(df_last_day_close, df_first_day_open)

filtered_df = df3_merged[df3_merged['Close'] > df3_merged['Open']]
print(filtered_df)
filtered_df['Year_month'] = pd.to_datetime(filtered_df['Year_month'])

if filtered_df.empty:
    print("Нет совпадений")
else:
    print(filtered_df['Year_month'].dt.month_name(),filtered_df['Year_month'].dt.year)


