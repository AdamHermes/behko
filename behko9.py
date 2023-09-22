import pandas as pd
# Creation of dataframe is done by passing multiple Series into the DataFrame
# class using pd.Series method.
# Here, it is passed in the two Series objects, s1 as the first row, and s2 as the second row.
ex = pd.Series([1,2,3,4,5])
# print(ex)
# There are many ways to demonstrate data using the pd.DataFrame
# first way:
s1 = pd.Series([1,2,3,4,5,6,7,8])
s2 = pd.Series(["Anne","Bach","Catherine","Daniel","Elizabeth","Frederick","Gabriel","Hans"])
data = pd.DataFrame([s1,s2]).T
# use .T when you want to conver the data from the same row to the same column
# using this when you want to create each set of data on the same row
print(data)
df = pd.DataFrame({"Stt":s1,"Họ và Tên":s2})
print(df)
# second way:
data1 = pd.DataFrame([[1,2,3,4,5,6,7,8],["Anne","Bach","Catherine","Daniel","Elizabeth","Frederick","Gabriel","Hans"]],\
                     index=["STT","Họ và Tên"],columns= ["A","B","C","D","E","F","G","H"])
print(data1)
# if using the second way, you use list not pd.Series
# third way:
# dictionary - like container:
data2 = pd.DataFrame({"c1":[1,"Anne"],"c2": [2,"Bach"]})
print(data2)

s3 = pd.Series([48,67,54,72,56,63,78,65])
s4 = pd.Series([1.5,1.76,1.54,1.74,1.63,1.71,1.81,1.77])
data3 = pd.DataFrame([s3,s4]).T
data3.columns = ["Weight","Height"]
data3.index = ["Anne","Bach","Catherine","Daniel","Elizabeth","Frederick","Gabriel","Hans"]
print(data3)
bmi = []
for i in data3.index:
    b = (data3['Weight'][i])/((data3['Height'][i])**2)
    bmi.append(b)
print(bmi)
# if not using DataFrame, no need to use pd.Series
data3["BMI"] = bmi
# remember that data[i][j] then [i] is the column and [j] is the row and you can also assign
# a column with a specific set of data (a list) in the above code
print(data3)
max = bmi[0]
for i in range(len(bmi)):
    if bmi[i] > max:
        max = bmi[i]
print(max)








