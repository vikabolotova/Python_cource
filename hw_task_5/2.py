import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 11,(10,10)), index = ['a','b','c','d','e','f','g','h','i','j'])
#print(df)

filtered_row = df[df.loc[:, 0:] > 5].dropna()

if filtered_row.empty:
    print('Нет строк подходящих под условие')
else:
    print(filtered_row)