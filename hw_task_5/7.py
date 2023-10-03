import pandas as pd
import matplotlib.pyplot as plt

def data_range(start,end):
    df = pd.read_csv('BCT-USD.csv').set_index('Date')
    print(df)
    plt.plot(df.loc[start:end,'Open'], df.loc[start:end,'Close'])
    return plt.savefig('open_close.png')

data_range('2021-10-21','2021-10-29')

