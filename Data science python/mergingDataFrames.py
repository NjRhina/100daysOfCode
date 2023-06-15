import pandas as pd

names = {
    'ID': [2, 5, 7, 8],
    'Name': ['Nana', 'Rhina', 'Mendes', 'Shawn']
}

ages = {
    'ID': [1, 2, 3, 5],
    'Age': [28, 34, 45, 62]
}

df1 = pd.DataFrame(names)
df2 = pd.DataFrame(ages)

print('\n')
print("Right join.....")
df = pd.merge(df1, df2, on='ID', how='right')
df.set_index('ID', inplace=True)
print(df)

print('\n')
print("Left join.....")
df = pd.merge(df1, df2, on='ID', how='left')
print(df)

print('\n')
print("Outer join.....")
df = pd.merge(df1, df2, on='ID', how='outer')
print(df)

print('\n')
print("Inner join.....")
df = pd.merge(df1, df2, on='ID', how='inner')
print(df)
