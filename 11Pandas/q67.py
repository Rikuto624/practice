import pandas as pd

df = pd.read_csv("weather.csv")
print(df.dtypes)
print(df.shape)
print(df.columns)
print(df.index)