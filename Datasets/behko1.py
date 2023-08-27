import pandas as pd
from bokeh.plotting import output_file, figure,show
from bokeh.models import ColumnDataSource
output_file("../Python/Python Files/chart.html")
data = pd.read_csv(r"/Datasets/LiveLongerData.csv")
#method read_csv có thể thay bằng các loại read khác tùy thuộc
#vào định dạng file
#data_source = ColumnDataSource(data)
data["Factor"] = data["Factor"].astype("category")
#chuyển đổi dữ liệu trong cột factor thành dữ liệu dạng category - x axis
p = figure(x_range = data["Factor"].cat.categories.tolist(),width=1600, height=600,x_axis_label = "Factor",y_axis_label = "Years gained / lost")
#data["Factor"].cat.categories.tolist() biến đổi các dữ liệu trong cột factor
# thành một list
p.vbar(x="Factor", top="Years gained / lost",source = data, width = 1,line_color = "black",line_width = 0.5)
show(p)

#.vbar(x = "", top = "", source = data, width,line_color,line_width)
# tạo một bar chart
