import matplotlib.pyplot as plt
import pandas as pd

data = {
    'ID': [30, 6, 38, 23],
    'Name': ['Nana', 'Rhina', 'Mendes', 'Shawn'],
    'Age': [12, 24, 42, 30],
    'Height': [160, 163, 181, 178],
    'Gender': ['F', 'F', 'M', 'M']
}

df = pd.DataFrame(data)
df.set_index('ID', inplace=True)
print(df)

# print(df.ndim)  # number of dimensions
# print(df.shape)
# print(df.T) #this returns the transpose of the data frame. meaning the rows become the columns

print(df.head(2))
print(df['Name'].iloc[1])
print(df.iloc[1])
print(df.iloc[0:2])

# df['Age'].plot()
# df.hist()

df.plot.bar()
plt.show()
