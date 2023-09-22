import pandas as pd
import matplotlib.pyplot as plt
data = {"EMPID": ["E001","E002","E003","E004","E005","E006","E007","E008","E009","E010"],
        "Gender": ["M","F","F","M","F","M","M","F","M","M"],
       "Age":[34,40,37,30,44,36,32,26,32,36],
       "Sales": [123,114,135,139,117,121,133,140,133,133],
        "BMI":["Normal","Overweight","Obesity","Underweight","Underweight","Normal","Obesity","Normal","Normal","Underweight"],
       "Income":[350,450,169,189,183,80,166,120,75,40]}
df = pd.DataFrame(data)
df.plot.bar()
# create bar chart using pandas library
# plot the bar chart will separate and give out numeric values
# create bar chart using plot between 2 attributes
# create bar chart using matplotlib library
plt.bar(df['Age'], df['Sales'])
plt.xlabel("Age")
plt.ylabel("Income")
plt.show()