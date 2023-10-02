import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.random((10,10)), index = ['a','b','c','d','e','f','g','h','i','j'])
df.columns = ['A','B','C','D','E','F','G','H','I','J']


print(df)
print(df.shape)
print(df.columns)
print(df.mean().mean())
df.to_csv('my_random_dataset.csv')
df.to_csv('my_random_dataset_1.csv', header=False, index = False)