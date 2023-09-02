from bokeh.plotting import figure, output_file, show
import pandas as pd
output_file("line.html")
data = pd.read_csv(r"D:\Python\PythonFiles\Datasets\US-News-Rankings-Universities-Through-2023.csv",header = None)
categories = data.iloc[0,3:8].tolist()
p = figure(title = "US Universities Ranking")
colors = ["red", "blue", "green", "orange", "purple", "yellow", "brown", "pink", "gray", "cyan"]
for i in range(1,10):
    uni = data.iloc[i,0]
    rankings = []
    for j in range(3, 8):
        rankings.append(data.iloc[i, j])
    p.line(x = categories,y = rankings, line_width = 2,color = colors[i-1],legend_label =uni)
p.legend.location = "top_right"
p.legend.label_text_font_size = "9pt"
show(p)