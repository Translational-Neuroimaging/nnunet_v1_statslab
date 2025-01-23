#%%
import pygwalker as pgw
import pandas as pd


#%%

df = pd.read_csv("https://raw.githubusercontent.com/Kanaries/pygwalker/main/tests/bike_sharing_dc.csv", parse_dates=['date'])
df


#%%
pgw.walk(df)

