
import pandas as pd
import numpy as np

# series = pd.Series([1,2,3,4,5,np.nan,"a string",6])
# print(series)

# series = pd.Series([1,2,np.nan,4])
# print(series)
df = pd.DataFrame(np.array([1,2,3,4,5,6]).reshape(2,3))
print(df)