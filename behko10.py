import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"D:\Python\PythonFiles\Datasets\NintendoGames.csv",header = None)
print(data.head())# Prints the first 5 rows of a DataFrame as default
print(data.shape) # Prints no. of rows and columns of a DataFrame
print(data.iloc[1,1]) # data.iloc[row,column]
print(data.iloc[0:5,:]) # print from row 1 to row 5 index 0 to 4 including every columns
print(data.iloc[3:,:3]) # print from third row and first 3 columns
# Indexing can be worked with labels using the pandas.DataFrame.loc method,
# which allows to index using labels instead of positions.
# example:
data1 = pd.read_csv(r"D:\Python\PythonFiles\Datasets\NintendoGames.csv")
print(data1.loc[:5,"platform"]) # print the first 5 rows of the platform column
# instead of using the index, we use label for the column for better comprehension
# exercise:
data1["platform"].hist(edgecolor = "black")
plt.show()

