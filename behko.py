from bokeh.plotting import figure, output_file, show
import numpy as np
from bokeh.layouts import gridplot
#x = np.linspace(0,10,100)#generate x values :generates an array of
# 100 equally spaced values between 0 and 10 using the `linspace`
# function from the NumPy library.
output_file("../Python/Python Files/dot.html")
d = figure(width=600, height=600)
d.circle([1, 2, 3, 4, 5], [0, 5, 9, -2, 6],
         size=10, color="navy", alpha=0.5)
l = figure(width=600, height=600)
l.line([1, 2, 3, 4, 5], [0, 3, 1, 8, 6],line_width =2,color = "blue")
grid = gridplot([[d,l]])
#The `gridplot` function in Bokeh is used to arrange multiple plots
# in a grid layout.
show(grid)