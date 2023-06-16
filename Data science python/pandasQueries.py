import pandas as pd
import numpy as np

df = pd.read_csv('people.csv', delimiter=',')
df.set_index('SSN', inplace=True)
print(df)

print('\n')

print(df.loc[df['Age'] >= 45])
print(df.loc[(df['Age'] >= 45) & (df['Height'] > 170)]['Name'])
