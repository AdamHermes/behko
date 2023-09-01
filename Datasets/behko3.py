from bokeh.plotting import figure, output_file, show
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("D:\HoangBach\Datasets\insurance.csv")
print(data.describe())
print(data["smoker"].value_counts())
bmi = list(data["bmi"])
plt.boxplot(bmi)
plt.show()
#print(data.groupby(["bmi","charges"]).mean())
