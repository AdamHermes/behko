# a Series represents a single column of data, and a DataFrame represents
# a collection of Series objects arranged as columns
import pandas as pd
data = []
n = int(input("Enter the number of values in the list: "))
for i in range(n):
    h = int(input("Enter value: "))
    data.append(h)
list = pd.Series(data)
print(list.sum())
print(list.mean())
print(list.std())
print(list.min())
print(list.max())
print(list.idxmin())
print(list.idxmax())
print(list.median())
print(list.mode())
print(list.value_counts())



