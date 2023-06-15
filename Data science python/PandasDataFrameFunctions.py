import pandas as pd
import numpy as np

data = {
    'ID': [30, 6, 38, 23],
    'Name': ['Nana', 'Rhina', 'Mendes', 'Shawn'],
    'Age': [12, 24, 42, 30],
    'Height': [160, 163, 181, 178],
    'Gender': ['F', 'F', 'M', 'M']
}

df = pd.DataFrame(data)
df.set_index('ID', inplace=True)

print(df['Height'].apply(np.sqrt))
print(df['Age'].apply(lambda x: x * 100))

# functions for iterating through data frames
for x in df:
    print(x)

for x in df['Age']:
    print(x)
    print('\n')

for key, value in df.items():
    print("{}: {}".format(key, value))
    print('\n')

for row in df.iterrows():
    print(row)
    print('\n')

# sorting values in the data frames
print("Sorting....")
df.sort_index(inplace=True)
print(df)

df.sort_values(by=['Name', 'Age'], inplace=True)
print(df)
