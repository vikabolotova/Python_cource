import pandas as pd

df = pd.read_csv('BCT-USD.csv')
df['Date'] = pd.to_datetime(df['Date'])

filtered_df = df[df['Close'] > df['Open']]

df_months = filtered_df['Date'].dt.month_name().unique()


if len(df_months) > 0:
    print("Месяцы, в которых цена при закрытии была выше цены открытия:")
    for month in df_months:
        print(month)
else:
    print("Нет месяцев, в которых цена при закрытии была выше цены открытия.")

