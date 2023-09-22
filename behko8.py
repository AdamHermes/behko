# create pie chart
import matplotlib.pyplot as plt
import pandas as pd
cars = {"Brand":["Toyota","Mazda","Mercedes","Audi","Lexus","Mitsubishi","BMW","Ford","Porsche"],
        "Number":[40,38,27,15,8,33,29,42,11],
        "Price": [25000,30000,50000,44000,56000,20000,54000,32000,68000]}
colors = ["green","blue","yellow","red","purple","pink","orange","cyan","beige"]
plt.pie(cars["Number"],autopct = '% 1.1f %%',startangle=90)
# pie chart attributes include data, autopct = '% 1.1f &&', startangle = 90
plt.show()
plt.bar(cars["Brand"],cars["Price"],width = 0.5, color = colors )
# bar chart attributes (matplotlib only) includes data for the x axis, then the y axis, width, color, etc
plt.show()

#scatter plot
# A scatter chart shows the relationship between two different variables
# and it can reveal the distribution trends.
# It should be used when there are many different data points,
# and you want to highlight similarities in the data set.
# This is useful when looking for outliers and for understanding the distribution of your data.
data = pd.read_csv("D:\Python\PythonFiles\Datasets\insurance.csv")
plt.scatter(data["bmi"],data["charges"])
plt.show()