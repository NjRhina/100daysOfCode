import pandas as pd

data = {
    'ID': [30, 6, 38, 23],
    'Name': ['Nana', 'Rhina', 'Mendes', 'Shawn'],
    'Age': [12, 24, 42, 30],
    'Height': [160, 165, 181, 178],
    'Gender': ['F', 'F', 'M', 'M']
}

df = pd.DataFrame(data)
df.set_index('ID', inplace=True)

print(df.count())
print(df['Height'].count())
print(df.sum())
print(df['Age'].sum())
print(df['Height'].prod())  # this gets the product of the height
print(df['Height'].mean())
print(df['Height'].median())  # mode() number that appears the most
print(df['Height'].std())  # standard deviation
print(df['Age'].min())  # max()
print(df['Height'].describe())
print(df.describe())
