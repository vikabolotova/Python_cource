import pandas as pd
import matplotlib.pyplot as plt


def data_range(start,end):
    df = pd.read_csv('BCT-USD.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df1 = df.set_index('Date')
    print(df1)
    plt.plot(df1.loc[start:end,'Open'], df1.loc[start:end,'Close'])
    return plt.savefig('open_close.png')


data_range('2021-Feb','2023-09')
