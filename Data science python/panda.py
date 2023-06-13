import pandas as pd
import matplotlib.pyplot as plt

series = pd.Series([10, 20, 30, 40], ['A', 'B', 'C', 'D'])
s1 = pd.Series([1, 3, 5, 2], ['a', 'b', 'c', 'd'])
s2 = pd.Series([9, 6, 5, 7], ['a', 'b', 'c', 'd'])
s3 = pd.Series([9, 6, 5, 7], ['c', 'b', 'a', 'd'])
s4 = pd.Series([1, 2, 3, 4, 7, 5, 1, 2], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

series.name = "My series"


def mysquare(x):
    return x ** 2


squares = s2.apply(mysquare)

print(series)
print(series.iloc[2])
print(series['D'])
print(dict(series))  # converting a series to a dictionary
print(s1 + s2)
print(s1 + s3)
print(s3.head(2))
print(s3.tail(2))
print(squares)

print(s2.sort_values())  # this does not permanently change the series. to do so, use s2.sort_values(inplace=True)
print(s3.sort_index())

# visualization with pandas
s4.plot.bar()  # s4.plot.barh()  s4.plot.pie()  s4.plot.hist()
plt.show()

# exporting the series into another format
s4.to_csv(
    'myseries.csv')  # s4.to_json()  s4.to_sql() s4.to_hdf() s4.to_excel() s4.tolist()  s4.to_frame()  s4.to_string  (), etc
