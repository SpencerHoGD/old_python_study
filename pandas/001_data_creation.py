import numpy as np
import pandas as pd


# s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range("20210820", periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df2 = pd.DataFrame(
  {
        "A": 1.0,
        "B": pd.Timestamp("20210801"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)


# print(s)
# print(dates)
# print(df)
# print(df2)
# print(df2.dtypes)
# print(df.to_numpy())
# print(df.describe())
# print(df.A)
# print()