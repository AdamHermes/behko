from bokeh.plotting import figure, output_file, show
import os
import pandas as pd
output_file("line.html")
data = pd.read_csv(r"D:\Python\PythonFiles\Datasets\US-News-Rankings-Universities-Through-2023.csv",header = None)
#header = None để khi dùng hàm data.iloc[] có thể quét qua được dữ liệu ở hàng đầu header
# data.iloc[row,column] row đầu là 0 column đầu là 0
# xếp các dữ liệu ở hàng 1 từ cột 3 tới 8 thành một list
categories = data.iloc[0,3:8].tolist()
p = figure(title = "US Universities Ranking")
colors = ["red", "blue", "green", "orange", "purple", "yellow", "brown", "pink", "gray", "cyan"]
for i in range(1,10):
    # do có 10 uni nên cho i chạy từ 1 tới 9
    #các uni đều nằm ở column đầu tiên nên column number =0, row number = i
    uni = data.iloc[i,0]
    # tạo một list mang tên rankings
    rankings = []
    for j in range(3, 8):
        # ta đặt i là các biến dữ liệu hàng và do có 10 uni tượng trưng cho 10 hàng
        # j là các biến dữ liệu cột và do các giá trị của rankings nằm từ cột 3 tới 7
        # thêm các giá trị truy cập từ lệnh data.iloc và append
        rankings.append(data.iloc[i, j])
        print(rankings)
        #j loop trước i loop sau, i = 1, j = 3,4,5,6,7
    p.line(x = categories,y = rankings, line_width = 2,color = colors[i-1],legend_label =uni)
    #tạo một line sau mỗi lần loop với trục ox là các giá trị từ các năm còn y là các giá trị từ rankings
    # mỗi line sẽ có một màu khác nhau tương đương với các màu trong list color với index i-1
    # do đã set giá trị uni thay đổi ở trên nên dùng lệnh legend_label để tạo note các quốc gia bằng uni
p.legend.location = "top_right"
p.legend.label_text_font_size = "9pt"
#chỉnh vị trí và font của note
show(p)
