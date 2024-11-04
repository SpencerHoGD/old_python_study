import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(10**5, 4))
print(df.describe())