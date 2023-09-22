import pandas as pd
import matplotlib.pyplot as plt
#The histogram represents the frequency of occurrence of specific phenomena
# which lie within a specific range of values and arranged in consecutive and fixed intervals.
data = [['E001', 'M', 34, 123, 'Normal', 350],
        ['E002', 'F', 40, 114, 'Overweight', 450],
        ['E003', 'F', 37, 135, 'Obesity', 169],
        ['E004', 'M', 30, 139, 'Underweight', 189],
        ['E005', 'F', 44, 117, 'Underweight', 183],
        ['E006', 'M', 36, 121, 'Normal', 80],
        ['E007', 'M', 32, 133, 'Obesity', 166],
        ['E008', 'F', 26, 140, 'Normal', 120],
        ['E009', 'M', 32, 133, 'Normal', 75],
        ['E010', 'M', 36, 133, 'Underweight', 40] ]
#list of list
#another way to do this:
#data = {"EMPID": ["E001","E002","E003","E004","E005","E006","E007","E008","E009","E010"],
#        "Gender": ["M","F","F","M","F","M","M","F","M","M"],
#        "Age":[34,40,37,30,44,36,32,26,32,36],
#        "Sales": [123,114,135,139,117,121,133,140,133,133],
#        "BMI":["Normal","Overweight","Obesity","Underweight","Underweight","Normal","Obesity","Normal","Normal","Underweight"],
#        "Income":[350,450,169,189,183,80,166,120,75,40]}
#df = pd.DataFrame(data)
# dictionary
df = pd.DataFrame(data, columns = ["EMPID","Gender","Age","Sales","BMI","Income"])
# create columns for the data in the DataFrame
#pd.DataFrame() create a table like an excel file.
print(df)
df.hist()
# df.hist() a function of pandas
plt.show()