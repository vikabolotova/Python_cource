import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.random((10,10)), index = ['a','b','c','d','e','f','g','h','i','j'])
print(df)