from bokeh.plotting import figure, output_file, show
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
output_file("scatterandline.html")
data = pd.read_csv("D:\copy\Datasets\insurance.csv")
#data["bmi"] = data["bmi"].astype("float")
p = figure(title = "BMI vs Charges",\
           x_axis_label = "bmi",y_axis_label = "charges",\
           width = 1200, height =600, )
p.scatter(x = data["bmi"],y = data["charges"],color = "red")
show(p)
sns.scatterplot(x=data["bmi"], y=data["charges"])
sns.regplot(x=data["bmi"], y=data["charges"], scatter=False, color = "yellow")
plt.title("BMI vs Charges")
plt.xlabel("BMI")
plt.ylabel("Charges")
plt.show()
